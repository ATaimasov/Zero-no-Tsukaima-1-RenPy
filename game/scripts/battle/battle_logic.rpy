# ============================================================================
# ZERO NO TSUKAIMA - BATTLE SYSTEM  (rewrite)
# FILE 2/4: LOGIC
# ----------------------------------------------------------------------------
# Pure state + math. Nothing here shows dialogue or screens - the engine
# (battle_engine.rpy) is responsible for pacing, speech and animations.
# These functions only read/mutate `store.party` / `store.foes` and return
# plain result dicts describing what happened.
# ============================================================================

# ---- Live battle state (rebuilt every battle) ----
default party = []          # list of live ally combatant dicts
default foes  = []          # list of live enemy combatant dicts
default battle_phase = "player"   # "player" | "enemy" | "victory" | "defeat"
default active_uid = None         # uid whose card/sprite is highlighted
default show_info_uid = None      # uid whose info panel is open in the HUD
default anim_state = None         # {"video": path|None, "label": str, "color": str} or None

init python:
    import copy
    import random

    # --------------------------------------------------------------------
    # SETUP
    # --------------------------------------------------------------------
    def make_unit(key, side, index):
        """Deep-copy a template from `characters` into a live combatant."""
        tpl = renpy.store.characters.get(key)
        if not tpl:
            return None
        u = copy.deepcopy(tpl)
        u["key"]  = key
        u["side"] = side                      # "ally" | "enemy"
        u["uid"]  = "%s__%s__%d" % (side, key, index)
        u["state"] = "normal"                 # normal | hurt | happy
        u["casting"] = None                   # {"skill": key, "turns_left": n} or None
        u["defending"] = False
        u["def_bonus"] = 0
        # Guarantee resource fields exist.
        for f in ("hp", "max_hp", "mp", "max_mp", "attack", "defense", "agility", "accuracy"):
            u.setdefault(f, 0)
        return u

    def battle_setup(ally_keys, enemy_keys):
        """Instantiate both sides from their keys and reset battle flags."""
        store.party = []
        for i, k in enumerate(ally_keys):
            u = make_unit(k, "ally", i)
            if u:
                store.party.append(u)

        store.foes = []
        for i, k in enumerate(enemy_keys):
            u = make_unit(k, "enemy", i)
            if u:
                store.foes.append(u)

        store.battle_phase = "player"
        store.active_uid = None
        store.show_info_uid = None
        store.anim_state = None

    # --------------------------------------------------------------------
    # QUERIES
    # --------------------------------------------------------------------
    def alive(units):
        return [u for u in units if u.get("hp", 0) > 0]

    def party_alive():
        return alive(store.party)

    def foes_alive():
        return alive(store.foes)

    def all_units():
        return list(store.party) + list(store.foes)

    def unit_by_uid(uid):
        for u in all_units():
            if u.get("uid") == uid:
                return u
        return None

    def allies_of(unit):
        return store.party if unit.get("side") == "ally" else store.foes

    def opponents_of(unit):
        return store.foes if unit.get("side") == "ally" else store.party

    def battle_over():
        return (not party_alive()) or (not foes_alive())

    def attack_type_label(unit):
        return "Magic" if unit.get("is_mage") else "Attack"

    # --------------------------------------------------------------------
    # COMBAT MATH
    # --------------------------------------------------------------------
    def calc_damage(attacker, defender, skill):
        base = skill.get("power", 30)
        atk = attacker.get("attack", 20)
        dfe = defender.get("defense", 10) + defender.get("def_bonus", 0)
        dmg = (base + atk * 0.5) * (100.0 / (100.0 + dfe))
        dmg = int(dmg * random.uniform(0.9, 1.1))
        return max(1, dmg)

    def roll_hit(attacker, skill):
        acc = (skill.get("accuracy", 90) + attacker.get("accuracy", 85)) / 2.0
        return random.randint(1, 100) <= acc

    def spend_mp(unit, skill):
        unit["mp"] = max(0, unit["mp"] - skill.get("consume", 0))

    def can_afford(unit, skill_key):
        sk = renpy.store.skills.get(skill_key, {})
        return unit.get("mp", 0) >= sk.get("consume", 0)

    def apply_skill_to_target(attacker, skill, target):
        """
        Resolve ONE skill against ONE target. Returns a result dict:
          {"kind": "hit",  "value": dmg, "dead": bool, "target": uid}
          {"kind": "miss", "target": uid}
          {"kind": "heal", "value": amt, "target": uid}
          {"kind": "buff", "stat": s, "value": v, "target": uid}
        Mutates target/state as needed.
        """
        kind = skill.get("kind", "damage")

        if kind == "heal":
            amt = skill.get("power", 50)
            before = target["hp"]
            target["hp"] = min(target["max_hp"], target["hp"] + amt)
            target["state"] = "happy"
            return {"kind": "heal", "value": target["hp"] - before, "target": target["uid"]}

        if kind == "buff":
            stat = skill.get("buff_stat", "accuracy")
            val = skill.get("buff_value", 10)
            target[stat] = target.get(stat, 0) + val
            target["state"] = "happy"
            return {"kind": "buff", "stat": stat, "value": val, "target": target["uid"]}

        # damage
        if not roll_hit(attacker, skill):
            target["state"] = "happy"    # dodged -> smug/relieved
            return {"kind": "miss", "target": target["uid"]}

        dmg = calc_damage(attacker, target, skill)
        target["hp"] = max(0, target["hp"] - dmg)
        target["state"] = "hurt"
        return {"kind": "hit", "value": dmg, "dead": target["hp"] <= 0, "target": target["uid"]}

    def resolve_targets(attacker, skill, single_target):
        """Return the list of targets a skill applies to."""
        tgt = skill.get("target", "enemy")
        if tgt == "all_enemies":
            return list(alive(opponents_of(attacker)))
        if tgt == "ally":
            return [single_target] if single_target else []
        # single enemy
        return [single_target] if single_target else []

    # --------------------------------------------------------------------
    # STATE HELPERS used by the engine
    # --------------------------------------------------------------------
    def clear_states():
        for u in all_units():
            u["state"] = "normal"

    def set_active(uid):
        store.active_uid = uid

    def start_defense(unit):
        unit["defending"] = True
        unit["def_bonus"] = 80          # ~ strong damage reduction
        # small MP regen as a reward for guarding
        unit["mp"] = min(unit["max_mp"], unit["mp"] + 10)

    def clear_defense(unit):
        unit["defending"] = False
        unit["def_bonus"] = 0

    def bark(unit, kind):
        """Return a random battle line for this unit/kind, or a generic one."""
        lines = unit.get("lines", {})
        pool = lines.get(kind)
        if pool:
            return random.choice(pool)
        # generic fallbacks
        generic = {
            "attack": ["Take this!", "Have at you!"],
            "cast":   ["Charging up...", "Almost ready..."],
            "hurt":   ["Ugh!", "Argh!"],
            "defend": ["Guarding.", "Bracing for impact."],
            "defeat": ["It's over for me...", "I'm done..."],
            "win":    ["Victory!", "We won!"],
        }
        pool = generic.get(kind)
        return random.choice(pool) if pool else None

    # --------------------------------------------------------------------
    # ITEMS
    # --------------------------------------------------------------------
    def can_use_item_on(item_name, unit):
        item = renpy.store.items.get(item_name)
        if not item:
            return False
        eff = item.get("effect")
        if eff == "revive":
            return unit.get("hp", 0) <= 0
        # non-revive items require a living target
        if unit.get("hp", 0) <= 0:
            return False
        if eff == "hp":
            return unit["hp"] < unit["max_hp"]
        if eff == "mp":
            return unit["mp"] < unit["max_mp"]
        if eff == "both":
            return unit["hp"] < unit["max_hp"] or unit["mp"] < unit["max_mp"]
        return True

    def apply_item(item_name, unit):
        """Apply an item to a live ally combatant. Returns a summary string."""
        item = renpy.store.items.get(item_name)
        if not item:
            return None
        eff = item.get("effect")
        msg = None
        if eff == "hp":
            before = unit["hp"]
            unit["hp"] = min(unit["max_hp"], unit["hp"] + item.get("hp", 0))
            msg = "%s recovers %d HP." % (unit["name"], unit["hp"] - before)
        elif eff == "mp":
            before = unit["mp"]
            unit["mp"] = min(unit["max_mp"], unit["mp"] + item.get("mp", 0))
            msg = "%s recovers %d MP." % (unit["name"], unit["mp"] - before)
        elif eff == "both":
            hb, mb = unit["hp"], unit["mp"]
            unit["hp"] = min(unit["max_hp"], unit["hp"] + item.get("hp", 0))
            unit["mp"] = min(unit["max_mp"], unit["mp"] + item.get("mp", 0))
            msg = "%s recovers %d HP / %d MP." % (unit["name"], unit["hp"] - hb, unit["mp"] - mb)
        elif eff == "revive":
            if unit["hp"] <= 0:
                unit["hp"] = int(unit["max_hp"] * item.get("ratio", 0.5))
                msg = "%s is revived!" % unit["name"]
        # consume
        if item_name in store.inventory:
            store.inventory[item_name] -= 1
            if store.inventory[item_name] <= 0:
                del store.inventory[item_name]
        unit["state"] = "happy"
        return msg

    # --------------------------------------------------------------------
    # ENEMY AI
    # --------------------------------------------------------------------
    def enemy_choose_action(foe):
        """
        Decide what a foe does this turn.
        Returns ("cast_tick", None) if it is mid-charge,
                ("skill", skill_key, target_or_None) otherwise.
        """
        # Already charging an AoE -> continue it.
        if foe.get("casting"):
            return ("cast_tick", None, None)

        usable = [k for k in foe.get("skills", []) if can_afford(foe, k)]
        if not usable:
            usable = [k for k in foe.get("skills", []) if renpy.store.skills.get(k, {}).get("consume", 0) == 0]
        if not usable:
            usable = ["claw"]

        skill_key = random.choice(usable)
        skill = renpy.store.skills.get(skill_key, {})

        if skill.get("target") == "all_enemies":
            return ("skill", skill_key, None)       # AoE, no single target
        # single target: pick a random living party member
        targets = party_alive()
        target = random.choice(targets) if targets else None
        return ("skill", skill_key, target)
