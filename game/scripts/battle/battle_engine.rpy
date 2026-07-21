# ============================================================================
# ZERO NO TSUKAIMA - BATTLE SYSTEM  (rewrite)
# FILE 4/4: ENGINE  +  PUBLIC API
# ----------------------------------------------------------------------------
# The engine is the ONLY place that paces the fight: it drives turns, shows the
# HUD, plays barks/notices/animations and calls the logic helpers.
#
# PUBLIC ENTRY POINT (call this from your dialogue):
#
#     $ battle(["saito", "louise"], ["mage", "mage"])
#
#   arg 1 = list of ALLY character keys   (from `characters`)
#   arg 2 = list of ENEMY character keys  (from `characters`)
#
#   Shows the preparation menu, then runs the battle, then returns True on a
#   player victory and False on defeat.
# ============================================================================

# On-screen feedback state (read by battle_screens.rpy)
default battle_notice = ""       # big centered banner
default battle_log = []          # rolling text log (left panel)

init python:

    # element -> accent colour for the fallback animation window
    _ELEMENT_COLORS = {
        "fire":   "#e0603c",
        "water":  "#4a90d9",
        "wind":   "#7ec8a0",
        "void":   "#c060d0",
        "dark":   "#8a5ad0",
        "physical": "#d0a24a",
    }

    # ----- feedback helpers -------------------------------------------------
    def _hud_show():
        """(Re)show the HUD in non-interactive display mode."""
        renpy.show_screen("battle_hud", awaiting=False, cur_uid=store.active_uid)
        renpy.restart_interaction()

    def _log(text):
        if text:
            store.battle_log.append(text)
            store.battle_log = store.battle_log[-30:]

    def _notice(text, secs=0.9):
        store.battle_notice = text
        renpy.restart_interaction()
        renpy.pause(secs)
        store.battle_notice = ""
        renpy.restart_interaction()

    def _speak(unit, kind):
        """Say a battle bark as the unit (name + colour)."""
        if not unit:
            return
        txt = bark(unit, kind)
        if not txt:
            return
        who = Character(unit.get("name", "?"), color=unit.get("color", "#ffffff"))
        renpy.say(who, txt, interact=True)

    def _play_anim(caster, skill, where):
        """Show the small animation window (video if present, else a burst)."""
        elem = skill.get("element", "physical")
        store.anim_state = {
            "video":  caster.get("cast_video"),
            "label":  skill.get("name", "").upper(),
            "color":  _ELEMENT_COLORS.get(elem, B_ACCENT),
            "where":  where,
            "caster": caster.get("name", ""),
        }
        _hud_show()
        _speak(caster, "cast")
        # If a real video exists let it breathe a little longer.
        dur = 2.6 if renpy.loadable(caster.get("cast_video") or "") else 1.6
        renpy.pause(dur)
        store.anim_state = None
        _hud_show()

    # ----- damage/heal reporting -------------------------------------------
    def _report(caster, skill, target, res, bark_hurt=True):
        kind = res.get("kind")
        if kind == "miss":
            _notice("%s's %s missed %s!" % (caster["name"], skill.get("name", "attack"), target["name"]))
            _log("MISS - %s -> %s" % (caster["name"], target["name"]))
        elif kind == "hit":
            _notice("%s takes %d damage!" % (target["name"], res["value"]))
            _log("%s hits %s for %d" % (caster["name"], target["name"], res["value"]))
            _hud_show()
            if res.get("dead"):
                _log("%s is defeated!" % target["name"])
                _speak(target, "defeat")
            elif bark_hurt:
                _speak(target, "hurt")
        elif kind == "heal":
            _notice("%s recovers %d HP." % (target["name"], res["value"]))
            _log("%s heals %s (+%d HP)" % (caster["name"], target["name"], res["value"]))
        elif kind == "buff":
            _notice("%s's %s rose by %d!" % (target["name"], res["stat"], res["value"]))
            _log("%s buffs %s (+%d %s)" % (caster["name"], target["name"], res["value"], res["stat"]))

    # ----- casting a skill (shared by allies + enemies) --------------------
    def _cast_now(unit, skill_key, target_uid, charged=False):
        skill = renpy.store.skills.get(skill_key, {})
        if not charged:
            spend_mp(unit, skill)

        is_aoe = skill.get("target") == "all_enemies"
        if is_aoe:
            where = "stage" if unit.get("is_enemy") else ("card:" + str(unit["uid"]))
            _play_anim(unit, skill, where)
        else:
            _speak(unit, "attack" if skill.get("kind") == "damage" else "cast")

        target = unit_by_uid(target_uid) if target_uid else None
        targets = resolve_targets(unit, skill, target)
        if not targets:
            _notice("...but there was no target.")
            return

        for t in targets:
            res = apply_skill_to_target(unit, skill, t)
            _report(unit, skill, t, res, bark_hurt=(not is_aoe))
            _hud_show()
            renpy.pause(0.3)

    def _perform_skill(unit, skill_key, target_uid):
        skill = renpy.store.skills.get(skill_key, {})
        # AoE with a charge time -> begin channeling instead of firing now.
        if skill.get("target") == "all_enemies" and skill.get("cast_turns", 0) > 0:
            spend_mp(unit, skill)
            unit["casting"] = {"skill": skill_key, "turns_left": skill["cast_turns"]}
            _play_anim_begin(unit, skill)
            return
        _cast_now(unit, skill_key, target_uid)

    def _play_anim_begin(unit, skill):
        _speak(unit, "cast")
        _notice("%s begins charging %s! (%d turns)" % (unit["name"], skill["name"], skill["cast_turns"]))
        _log("%s starts charging %s" % (unit["name"], skill["name"]))

    def _tick_cast(unit):
        """Advance a charging AoE on the unit's turn; fire when it reaches 0."""
        c = unit.get("casting")
        if not c:
            return
        c["turns_left"] -= 1
        if c["turns_left"] > 0:
            _notice("%s keeps channeling... (%d turn(s) left)" % (unit["name"], c["turns_left"]))
            _log("%s channels (%d left)" % (unit["name"], c["turns_left"]))
            renpy.pause(0.4)
            return
        skill_key = c["skill"]
        unit["casting"] = None
        _cast_now(unit, skill_key, None, charged=True)

    # ----- turns ------------------------------------------------------------
    def _player_turn(ally):
        set_active(ally["uid"])
        clear_defense(ally)          # guard only lasts through one enemy phase

        # mid-charge: resolve the channeled AoE, no input needed
        if ally.get("casting"):
            _hud_show()
            _tick_cast(ally)
            return

        _hud_show()
        action = renpy.call_screen("battle_hud", awaiting=True, cur_uid=ally["uid"])
        _hud_show()

        kind, key, target_uid = action
        if kind == "defend":
            start_defense(ally)
            _speak(ally, "defend")
            _notice("%s raises their guard." % ally["name"])
            _log("%s defends (DEF up)" % ally["name"])
        elif kind == "item":
            target = unit_by_uid(target_uid)
            msg = apply_item(key, target)
            _hud_show()
            _notice(msg or "Nothing happened.")
            _log(msg or "")
        elif kind == "skill":
            _perform_skill(ally, key, target_uid)

    def _enemy_turn(foe):
        set_active(foe["uid"])
        _hud_show()
        renpy.pause(0.3)

        if foe.get("casting"):
            _tick_cast(foe)
            return

        act = enemy_choose_action(foe)
        if act and act[0] == "skill":
            _perform_skill(foe, act[1], act[2])

    # ----- end of battle ----------------------------------------------------
    def _resolve_end(win):
        clear_states()
        store.active_uid = None
        if win:
            for a in party_alive():
                a["state"] = "happy"
            _hud_show()
            _notice("VICTORY!", 1.4)
            champs = party_alive()
            if champs:
                _speak(champs[0], "win")
        else:
            _hud_show()
            _notice("DEFEAT...", 1.6)

    # ========================================================================
    # PUBLIC ENTRY POINT
    # ========================================================================
    def battle(ally_keys, enemy_keys):
        # 1) preparation menu (save / start)
        renpy.call_screen("battle_prep", ally_keys, enemy_keys)
        renpy.hide_screen("battle_prep")

        # 2) build the fight
        battle_setup(ally_keys, enemy_keys)
        store.battle_log = []
        store.battle_notice = ""

        _hud_show()
        _notice("Battle Start!", 1.0)

        # 3) round loop
        guard = 0
        while not battle_over() and guard < 200:
            guard += 1

            # ----- PLAYER PHASE -----
            store.battle_phase = "player"
            _hud_show()
            for ally in list(store.party):
                if battle_over():
                    break
                if ally.get("hp", 0) <= 0:
                    continue
                _player_turn(ally)
                if battle_over():
                    break

            if battle_over():
                break

            # ----- ENEMY PHASE -----
            store.battle_phase = "enemy"
            _hud_show()
            _notice("Enemy Turn", 0.7)
            for foe in list(store.foes):
                if battle_over():
                    break
                if foe.get("hp", 0) <= 0:
                    continue
                _enemy_turn(foe)
                if battle_over():
                    break

            # tidy transient hurt/happy states before the next round
            clear_states()
            _hud_show()

        # 4) wrap up
        win = bool(party_alive())
        store.battle_phase = "victory" if win else "defeat"
        _resolve_end(win)
        renpy.pause(0.4)
        renpy.hide_screen("battle_hud")
        store.active_uid = None
        store.anim_state = None
        return win
