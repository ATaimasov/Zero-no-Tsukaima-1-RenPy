# ============================================================================
# ZERO NO TSUKAIMA - BATTLE & INVENTORY SYSTEM
# Complete battle and inventory system in PS2 JRPG style
# ============================================================================

# ============================================================================
# GLOBAL VARIABLES
# ============================================================================

# Character states: "normal", "happy", "hurt"
default character_states = {}

# Current battle
default battle_active = False
default current_turn_index = 0
default battle_phase = "player"  # "player", "enemy", "victory", "defeat"
default selected_action = None
default selected_skill = None
default selected_target = None
default current_actor = None
default battle_message = ""
default battle_message_timer = 0

# AOE casting
default aoe_casting = {}  # {character_key: {"skill": skill, "turns_left": N}}

# Defense buffs
default defense_buffs = {}  # {character_key: {"value": 50, "turns": 2}}

# Enemies
default enemies = []

# Selected item
default selected_item = None
default item_target_selection = False

# Battle preparation selected character
default selected_character = None

# Inventory lock (True = items blocked from use)
default inventory_locked = False

# ============================================================================
# ITEM DATA (EXTENDED)
# ============================================================================

default curr_items = {
    "Bread": 3,
    "Herb": 3,
    "Elixir": 3,
    "Antidote": 2,
    "Phoenix Feather": 1,
}

init python:
    import random
    
    # Full item dictionary with actions
    items = {
        "Bread": {
            "name": "Bread",
            "description": "Restores 50 HP",
            "effect_type": "hp",
            "effect_value": 50,
            "animation": "heal",
            "sound": "audio/sfx/item_use.ogg"
        },
        "Herb": {
            "name": "Herb",
            "description": "Restores 30 MP",
            "effect_type": "mp",
            "effect_value": 30,
            "animation": "mp_restore",
            "sound": "audio/sfx/item_use.ogg"
        },
        "Elixir": {
            "name": "Elixir",
            "description": "Restores 100 HP and 50 MP",
            "effect_type": "both",
            "effect_hp": 100,
            "effect_mp": 50,
            "animation": "full_restore",
            "sound": "audio/sfx/elixir.ogg"
        },
        "Antidote": {
            "name": "Antidote",
            "description": "Cures poison status",
            "effect_type": "cure_poison",
            "animation": "cure",
            "sound": "audio/sfx/cure.ogg"
        },
        "Phoenix Feather": {
            "name": "Phoenix Feather",
            "description": "Revives fallen ally with 50% HP",
            "effect_type": "revive",
            "effect_value": 0.5,
            "animation": "revive",
            "sound": "audio/sfx/revive.ogg"
        }
    }
    
    def lock_inventory():
        """Locks inventory - items cannot be used"""
        store.inventory_locked = True
    
    def unlock_inventory():
        """Unlocks inventory - items can be used"""
        store.inventory_locked = False
    
    def can_use_item_on_target(item_name, target_key):
        """Checks if item can be used on target (checks HP/MP full status)"""
        if store.inventory_locked:
            return False
        
        if item_name not in items:
            return False
        
        target = store.party_characters.get(target_key)
        if not target:
            return False
        
        item = items[item_name]
        effect_type = item.get("effect_type", "")
        
        # Check if HP item can be used (not at full HP)
        if effect_type == "hp":
            if target.get('hp', 0) >= target.get('max_hp', 0):
                return False
        
        # Check if MP item can be used (not at full MP)
        elif effect_type == "mp":
            if target.get('mp', 0) >= target.get('max_mp', 0):
                return False
        
        # Check if both HP/MP item can be used
        elif effect_type == "both":
            hp_full = target.get('hp', 0) >= target.get('max_hp', 0)
            mp_full = target.get('mp', 0) >= target.get('max_mp', 0)
            if hp_full and mp_full:
                return False
        
        # Revive only works on dead characters
        elif effect_type == "revive":
            if target.get('hp', 0) > 0:
                return False
        
        # Cure poison only works on poisoned characters
        elif effect_type == "cure_poison":
            if 'status' not in target or 'poison' not in target.get('status', set()):
                return False
        
        return True

    def use_item(item_name, target_key):
        """Applies item to character"""
        if store.inventory_locked:
            return False
        
        if item_name not in store.curr_items or store.curr_items[item_name] <= 0:
            return False
        
        if item_name not in items:
            return False
        
        if not can_use_item_on_target(item_name, target_key):
            return False
            
        item = items[item_name]
        target = store.party_characters.get(target_key)
        
        if not target:
            return False
        
        # Apply effect
        effect_type = item.get("effect_type", "")
        
        if effect_type == "hp":
            value = item.get("effect_value", 0)
            target['hp'] = min(target['hp'] + value, target['max_hp'])
        elif effect_type == "mp":
            value = item.get("effect_value", 0)
            target['mp'] = min(target['mp'] + value, target['max_mp'])
        elif effect_type == "both":
            hp_val = item.get("effect_hp", 0)
            mp_val = item.get("effect_mp", 0)
            target['hp'] = min(target['hp'] + hp_val, target['max_hp'])
            target['mp'] = min(target['mp'] + mp_val, target['max_mp'])
        elif effect_type == "revive":
            if target['hp'] <= 0:
                ratio = item.get("effect_value", 0.5)
                target['hp'] = int(target['max_hp'] * ratio)
        elif effect_type == "cure_poison":
            if 'status' in target:
                target['status'].discard('poison')
        
        # Decrease quantity
        store.curr_items[item_name] -= 1
        if store.curr_items[item_name] <= 0:
            del store.curr_items[item_name]
        
        return True

    def get_party_members():
        """Returns list of party members"""
        return [(key, char) for key, char in store.party_characters.items()]

    def get_alive_party_members():
        """Returns alive party members"""
        return [(key, char) for key, char in store.party_characters.items() 
                if char.get('hp', 0) > 0]

    def get_alive_enemies():
        """Returns alive enemies"""
        return [e for e in store.enemies if e.get('hp', 0) > 0]
    
    def get_attack_type(char_data):
        """Returns attack type based on is_mage flag"""
        if char_data.get('is_mage', False):
            return "Magic"
        else:
            return "Attack"

# ============================================================================
# SKILL DATA (EXTENDED)
# ============================================================================

default skills = {
    # Louise skills
    "arrow": {
        "name": "Magic Arrow",
        "consume": 30,
        "description": "Attacks a single enemy with magic arrow",
        "damage": 40,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "void",
        "accuracy": 90,
        "animation": "magic_arrow"
    },
    "heroism": {
        "name": "Heroism",
        "consume": 50,
        "description": "Powerful attack on single enemy",
        "damage": 80,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "void",
        "accuracy": 85,
        "animation": "heroism"
    },
    "meteor": {
        "name": "Meteor",
        "consume": 70,
        "description": "Attacks ALL enemies with meteors",
        "damage": 60,
        "is_aoe": True,
        "cast_turns": 2,
        "element": "void",
        "accuracy": 80,
        "animation": "meteor"
    },
    "dispel": {
        "name": "Dispel Magic",
        "consume": 30,
        "description": "Increases ally accuracy",
        "is_buff": True,
        "buff_type": "accuracy",
        "buff_value": 20,
        "is_aoe": False,
        "cast_turns": 0,
        "animation": "buff"
    },
    "heal": {
        "name": "Heal",
        "consume": 30,
        "description": "Restores ally HP",
        "is_heal": True,
        "heal_value": 60,
        "is_aoe": False,
        "cast_turns": 0,
        "animation": "heal"
    },

    # Saito skills
    "slash": {
        "name": "Slash",
        "consume": 20,
        "description": "Basic sword attack",
        "damage": 35,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "physical",
        "accuracy": 95,
        "animation": "slash"
    },
    "d_slash": {
        "name": "Double Slash",
        "consume": 40,
        "description": "Double sword strike",
        "damage": 65,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "physical",
        "accuracy": 90,
        "animation": "double_slash"
    },
    "wind_moon_slash": {
        "name": "Wind Moon Slash",
        "consume": 70,
        "description": "Powerful attack on ALL enemies",
        "damage": 50,
        "is_aoe": True,
        "cast_turns": 2,
        "element": "wind",
        "accuracy": 85,
        "animation": "wind_slash"
    },

    # Tabitha skills (wind)
    "wing": {
        "name": "Wing",
        "consume": 30,
        "description": "Wind attack",
        "damage": 35,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "wind",
        "accuracy": 90,
        "animation": "wind"
    },
    "air_needle": {
        "name": "Air Needle",
        "consume": 50,
        "description": "Air needles attack",
        "damage": 55,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "wind",
        "accuracy": 88,
        "animation": "air_needle"
    },
    "wind_break": {
        "name": "Wind Break",
        "consume": 70,
        "description": "Hurricane on ALL enemies",
        "damage": 45,
        "is_aoe": True,
        "cast_turns": 2,
        "element": "wind",
        "accuracy": 82,
        "animation": "wind_storm"
    },
    "air_force": {
        "name": "Air Force",
        "consume": 30,
        "description": "Increases ally speed",
        "is_buff": True,
        "buff_type": "agility",
        "buff_value": 15,
        "is_aoe": False,
        "cast_turns": 0,
        "animation": "buff"
    },

    # Kirche skills (fire)
    "fire": {
        "name": "Fire",
        "consume": 30,
        "description": "Fire attack",
        "damage": 40,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "fire",
        "accuracy": 88,
        "animation": "fire"
    },
    "fire_needle": {
        "name": "Fire Needle",
        "consume": 50,
        "description": "Fire needles attack",
        "damage": 60,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "fire",
        "accuracy": 85,
        "animation": "fire_needle"
    },
    "fire_arrow": {
        "name": "Fire Arrow",
        "consume": 70,
        "description": "Fire storm on ALL enemies",
        "damage": 50,
        "is_aoe": True,
        "cast_turns": 2,
        "element": "fire",
        "accuracy": 80,
        "animation": "fire_storm"
    },
    "fire_shield": {
        "name": "Fire Shield",
        "consume": 30,
        "description": "Increases ally defense",
        "is_buff": True,
        "buff_type": "defense",
        "buff_value": 25,
        "is_aoe": False,
        "cast_turns": 0,
        "animation": "buff"
    },

    # Henrietta skills (water)
    "water": {
        "name": "Water",
        "consume": 30,
        "description": "Water attack",
        "damage": 38,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "water",
        "accuracy": 90,
        "animation": "water"
    },
    "water_needle": {
        "name": "Water Needle",
        "consume": 50,
        "description": "Water needles attack",
        "damage": 55,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "water",
        "accuracy": 87,
        "animation": "water_needle"
    },
    "water_hazard": {
        "name": "Water Hazard",
        "consume": 70,
        "description": "Water storm on ALL enemies",
        "damage": 48,
        "is_aoe": True,
        "cast_turns": 2,
        "element": "water",
        "accuracy": 83,
        "animation": "water_storm"
    },
    "water_blade": {
        "name": "Water Blade",
        "consume": 30,
        "description": "Increases ally attack",
        "is_buff": True,
        "buff_type": "attack",
        "buff_value": 20,
        "is_aoe": False,
        "cast_turns": 0,
        "animation": "buff"
    }
}

# ============================================================================
# PARTY CHARACTERS - Only characters currently in party
# ============================================================================

default party_characters = {
    'saito': {
        'name': 'Saito',
        'description': "A Japanese boy who was summoned to this world by Louise.\nHe is treated as a familiar by Louise.", 
        "is_mage": False,
        "skills": ["slash", "d_slash", "wind_moon_slash"],
        'hp': 255,
        'max_hp': 255,
        'mp': 100,
        'max_mp': 100,
        'attack': 45,
        'defense': 30,
        'agility': 35,
        'accuracy': 95,
        'portrait': 'gui/portraits/s.png',
        'portrait_normal': 'gui/portraits/s.png',
        'portrait_happy': 'gui/portraits/s_happy.png',
        'portrait_hurt': 'gui/portraits/s_hurt.png',
        'cast_video': 'video/cast/saito_cast.webm',
        'state': 'normal',
        'cooldown': 0
    },
    'louise': {
        'name': 'Louise',
        "description": "The magician who summoned Saito.\nAlthough she can use Void magic,\nits true nature remains unknown.",
        "is_mage": True,
        "skills": ["arrow", "heroism", "dispel"],
        'hp': 200,
        'max_hp': 200,
        'mp': 150,
        'max_mp': 150,
        'attack': 25,
        'defense': 20,
        'agility': 30,
        'accuracy': 85,
        'portrait': 'gui/portraits/l.png',
        'portrait_normal': 'gui/portraits/l.png',
        'portrait_happy': 'gui/portraits/l_happy.png',
        'portrait_hurt': 'gui/portraits/l_hurt.png',
        'cast_video': 'video/cast/louise_cast.webm',
        'state': 'normal',
        'cooldown': 0
    }
}

# All characters data (for reference/adding to party)
default all_characters = {
    'saito': {
        'name': 'Saito',
        'description': "A Japanese boy who was summoned to this world by Louise.\nHe is treated as a familiar by Louise.", 
        "is_mage": False,
        "skills": ["slash", "d_slash", "wind_moon_slash"],
        'hp': 255,
        'max_hp': 255,
        'mp': 100,
        'max_mp': 100,
        'attack': 45,
        'defense': 30,
        'agility': 35,
        'accuracy': 95,
        'portrait': 'gui/portraits/s.png',
        'portrait_normal': 'gui/portraits/s.png',
        'portrait_happy': 'gui/portraits/s_happy.png',
        'portrait_hurt': 'gui/portraits/s_hurt.png',
        'cast_video': 'video/cast/saito_cast.webm',
        'state': 'normal',
        'cooldown': 0
    },
    'louise': {
        'name': 'Louise',
        "description": "The magician who summoned Saito.\nAlthough she can use Void magic,\nits true nature remains unknown.",
        "is_mage": True,
        "skills": ["arrow", "heroism", "dispel"],
        'hp': 200,
        'max_hp': 200,
        'mp': 150,
        'max_mp': 150,
        'attack': 25,
        'defense': 20,
        'agility': 30,
        'accuracy': 85,
        'portrait': 'gui/portraits/l.png',
        'portrait_normal': 'gui/portraits/l.png',
        'portrait_happy': 'gui/portraits/l_happy.png',
        'portrait_hurt': 'gui/portraits/l_hurt.png',
        'cast_video': 'video/cast/louise_cast.webm',
        'state': 'normal',
        'cooldown': 0
    },
    'siesta': {
        'name': 'Siesta',
        'portrait': 'gui/portraits/si.png',
        "skills": [],
        'description': "A maid working at Tristain Academy of Magic.\nSince she is a commoner, she cannot use magic.\nShe has feelings for Saito."
    },
    'tabitha': {
        'name': "Tabitha",
        "is_mage": True,
        'portrait': 'gui/portraits/t.png',
        'portrait_normal': 'gui/portraits/t.png',
        'portrait_happy': 'gui/portraits/t_happy.png',
        'portrait_hurt': 'gui/portraits/t_hurt.png',
        'description': "Louise's classmate.\nSpecializes in wind magic.\nHer nickname is \"Tabitha of the Snow Wind\".", 
        "skills": ["wing", "air_needle", "wind_break", "air_force", "heal"],
        'hp': 180,
        'max_hp': 180,
        'mp': 180,
        'max_mp': 180,
        'attack': 20,
        'defense': 18,
        'agility': 40,
        'accuracy': 90,
        'cast_video': 'video/cast/tabitha_cast.webm',
        'state': 'normal',
        'cooldown': 0
    },
    'kirche': {
        'name': "Kirche",
        "is_mage": True,
        'portrait': 'gui/portraits/k.png',
        'portrait_normal': 'gui/portraits/k.png',
        'portrait_happy': 'gui/portraits/k_happy.png',
        'portrait_hurt': 'gui/portraits/k_hurt.png',
        'description': "Louise's classmate.\nSpecializes in fire magic.\nHer nickname is \"Kirche of the Mild Fever\".",
        "skills": ["fire", "fire_needle", "fire_arrow", "fire_shield", "heal"],
        'hp': 190,
        'max_hp': 190,
        'mp': 170,
        'max_mp': 170,
        'attack': 22,
        'defense': 22,
        'agility': 28,
        'accuracy': 88,
        'cast_video': 'video/cast/kirche_cast.webm',
        'state': 'normal',
        'cooldown': 0
    },
    'henrietta': {
        'name': "Henrietta",
        "is_mage": True,
        'portrait': 'gui/portraits/h.png',
        'portrait_normal': 'gui/portraits/h.png',
        'portrait_happy': 'gui/portraits/h_happy.png',
        'portrait_hurt': 'gui/portraits/h_hurt.png',
        'description': "Princess of the Tristain Kingdom.\nChildhood friend of Louise.\nSpecializes in water magic.",
        "skills": ["water", "water_needle", "water_hazard", "water_blade", "heal"],
        'hp': 185,
        'max_hp': 185,
        'mp': 175,
        'max_mp': 175,
        'attack': 23,
        'defense': 25,
        'agility': 32,
        'accuracy': 87,
        'cast_video': 'video/cast/henrietta_cast.webm',
        'state': 'normal',
        'cooldown': 0
    }
}

# ============================================================================
# ENEMY DATA (without exp_reward and gold_reward)
# ============================================================================

default enemy_templates = {
    "bandit": {
        "name": "Bandit",
        "hp": 80,
        "max_hp": 80,
        "mp": 20,
        "max_mp": 20,
        "attack": 25,
        "defense": 15,
        "agility": 20,
        "accuracy": 80,
        "sprite": "images/enemies/bandit.png",
        "skills": ["slash"]
    },
    "mage": {
        "name": "Dark Mage",
        "hp": 60,
        "max_hp": 60,
        "mp": 100,
        "max_mp": 100,
        "attack": 35,
        "defense": 10,
        "agility": 25,
        "accuracy": 85,
        "sprite": "images/enemies/mage.png",
        "skills": ["fire", "fire_needle"]
    },
    "golem": {
        "name": "Stone Golem",
        "hp": 150,
        "max_hp": 150,
        "mp": 0,
        "max_mp": 0,
        "attack": 40,
        "defense": 40,
        "agility": 10,
        "accuracy": 70,
        "sprite": "images/enemies/golem.png",
        "skills": ["slash"]
    }
}

# ============================================================================
# BATTLE FUNCTIONS
# ============================================================================

init python:

    def init_battle(enemy_list):
        """Initializes battle state with specified enemies"""
        store.enemies = []
        for i, enemy_type in enumerate(enemy_list):
            if enemy_type in store.enemy_templates:
                enemy = dict(store.enemy_templates[enemy_type])
                enemy['id'] = i
                enemy['key'] = "{}_{}".format(enemy_type, i)
                enemy['state'] = 'normal'
                store.enemies.append(enemy)
        
        store.battle_active = True
        store.battle_phase = "player"
        store.current_turn_index = 0
        store.aoe_casting = {}
        store.defense_buffs = {}
        
        # Reset character states
        for key in store.party_characters:
            store.party_characters[key]['state'] = 'normal'
            store.party_characters[key]['cooldown'] = 0

    def get_current_actor():
        """Gets current acting character"""
        party = get_alive_party_members()
        if store.current_turn_index < len(party):
            return party[store.current_turn_index]
        return None

    def calculate_damage(attacker, defender, skill):
        """Calculates damage"""
        base_damage = skill.get('damage', 30)
        atk = attacker.get('attack', 20)
        defense = defender.get('defense', 10)
        
        # Account for defense buffs
        def_key = None
        for k, v in store.party_characters.items():
            if v == defender:
                def_key = k
                break
        
        if def_key and def_key in store.defense_buffs:
            defense += store.defense_buffs[def_key].get('value', 0)
        
        damage = int((base_damage + atk * 0.5) * (100 / (100 + defense)))
        # Small variation
        damage = int(damage * random.uniform(0.9, 1.1))
        return max(1, damage)

    def check_hit(attacker, skill):
        """Checks if attack hits"""
        accuracy = skill.get('accuracy', 85)
        attacker_acc = attacker.get('accuracy', 80)
        final_acc = (accuracy + attacker_acc) / 2
        return random.randint(1, 100) <= final_acc

    def perform_attack(attacker_key, attacker, skill, target):
        """Performs attack"""
        skill_data = store.skills.get(skill) if isinstance(skill, str) else skill
        if not skill_data:
            return None
        
        # Check MP
        mp_cost = skill_data.get('consume', 0)
        if attacker.get('mp', 0) < mp_cost:
            return {"success": False, "reason": "not_enough_mp"}
        
        # Spend MP
        attacker['mp'] = attacker['mp'] - mp_cost
        
        results = []
        
        # AOE or single target
        if skill_data.get('is_aoe'):
            targets = get_alive_enemies() if attacker_key in store.party_characters else get_alive_party_members()
            for t in targets:
                if isinstance(t, tuple):
                    t = t[1]
                hit = check_hit(attacker, skill_data)
                if hit:
                    damage = calculate_damage(attacker, t, skill_data)
                    t['hp'] = max(0, t['hp'] - damage)
                    results.append({"target": t, "hit": True, "damage": damage})
                else:
                    results.append({"target": t, "hit": False, "damage": 0, "dodged": True})
        else:
            # Single target
            hit = check_hit(attacker, skill_data)
            if hit:
                if skill_data.get('is_heal'):
                    heal = skill_data.get('heal_value', 50)
                    target['hp'] = min(target['hp'] + heal, target['max_hp'])
                    results.append({"target": target, "hit": True, "heal": heal})
                elif skill_data.get('is_buff'):
                    # Apply buff
                    results.append({"target": target, "hit": True, "buff": skill_data.get('buff_type')})
                else:
                    damage = calculate_damage(attacker, target, skill_data)
                    target['hp'] = max(0, target['hp'] - damage)
                    results.append({"target": target, "hit": True, "damage": damage})
            else:
                results.append({"target": target, "hit": False, "damage": 0, "dodged": True})
        
        return {"success": True, "results": results, "skill": skill_data}

    def enemy_turn():
        """Enemy turn"""
        alive_enemies = get_alive_enemies()
        alive_party = get_alive_party_members()
        
        results = []
        
        for enemy in alive_enemies:
            if not alive_party:
                break
            
            # Choose random skill
            enemy_skills = enemy.get('skills', ['slash'])
            skill_key = random.choice(enemy_skills)
            skill_data = store.skills.get(skill_key, store.skills['slash'])
            
            # Choose random target
            target_key, target = random.choice(alive_party)
            
            # Attack
            result = perform_attack(enemy['key'], enemy, skill_key, target)
            if result and result.get('success'):
                results.append({
                    "attacker": enemy,
                    "skill": skill_data,
                    "target_key": target_key,
                    "target": target,
                    "results": result.get('results', [])
                })
        
        return results

    def next_turn():
        """Advance to next turn"""
        party = get_alive_party_members()
        store.current_turn_index += 1
        
        if store.current_turn_index >= len(party):
            # All characters acted - enemy turn
            store.battle_phase = "enemy"
            store.current_turn_index = 0
        
        # Check victory/defeat
        if not get_alive_enemies():
            store.battle_phase = "victory"
        elif not get_alive_party_members():
            store.battle_phase = "defeat"

    def apply_defense(char_key):
        """Applies defense to character"""
        store.defense_buffs[char_key] = {
            "value": 50,
            "turns": 2
        }
        # Restore some MP
        char = store.party_characters.get(char_key)
        if char:
            char['mp'] = min(char['mp'] + 10, char['max_mp'])

    def update_defense_buffs():
        """Updates defense buffs"""
        to_remove = []
        for key in store.defense_buffs:
            store.defense_buffs[key]['turns'] -= 1
            if store.defense_buffs[key]['turns'] <= 0:
                to_remove.append(key)
        for key in to_remove:
            del store.defense_buffs[key]

    def update_aoe_casting():
        """Updates AOE casting"""
        to_cast = []
        for key in store.aoe_casting:
            store.aoe_casting[key]['turns_left'] -= 1
            if store.aoe_casting[key]['turns_left'] <= 0:
                to_cast.append((key, store.aoe_casting[key]['skill']))
        
        for key, skill in to_cast:
            del store.aoe_casting[key]
            # Execute AOE
            char = store.party_characters.get(key)
            if char and char.get('hp', 0) > 0:
                perform_attack(key, char, skill, None)


# ============================================================================
# STYLES
# ============================================================================

style battle_card:
    background "#5c4033"
    padding (5, 5)

style battle_card_active:
    background "#8b6914"
    padding (5, 5)

style battle_card_inactive:
    background "#3a3a3a"
    padding (5, 5)

style battle_action_button:
    background "#8b5a2b"
    hover_background "#a06030"
    padding (15, 10)
    xsize 150
    ysize 50

style battle_action_button_text:
    color "#fff8e7"
    size 20
    bold True
    text_align 0.5

style battle_menu_button:
    background "#8b5a2b"
    hover_background "#a06030"
    padding (20, 12)
    xsize 280
    ysize 55

style battle_menu_button_text:
    color "#fff8e7"
    hover_color "#ffffff"
    size 22
    bold True
    text_align 0.5
    outlines [(1, "#3d2817", 1, 1)]

style battle_start_button:
    background "#c9763c"
    hover_background "#e08850"
    padding (20, 15)
    xsize 280
    ysize 60

style battle_start_button_text:
    color "#ffffff"
    hover_color "#ffffd0"
    size 26
    bold True
    text_align 0.5
    outlines [(2, "#5c3d2e", 0, 0)]

style battle_title_text:
    color "#fff8e7"
    size 32
    bold True
    outlines [(2, "#3d2817", 0, 0)]
    text_align 0.5

style battle_hp_bar:
    left_bar Solid("#4caf50")
    right_bar Solid("#2d2d2d")
    thumb None
    ysize 14
    xsize 140

style battle_mp_bar:
    left_bar Solid("#29b6f6")
    right_bar Solid("#2d2d2d")
    thumb None
    ysize 14
    xsize 140

style battle_bar_label:
    color "#fff8e7"
    size 14
    bold True
    outlines [(1, "#000000", 0, 0)]

style item_button_normal:
    background "#5c3d2e"
    hover_background "#a06030"
    padding (10, 8)

style item_button_selected:
    background "#8b5a2b"
    hover_background "#a06030"
    padding (10, 8)

style skill_button_enabled:
    background "#5c3d2e"
    hover_background "#7a5040"
    padding (8, 6)

style skill_button_disabled:
    background "#3a3a3a"
    padding (8, 6)

style item_button_disabled:
    background "#3a3a3a"
    padding (10, 8)


# ============================================================================
# INVENTORY SCREEN (FULL)
# ============================================================================

screen inventory():
    tag menu
    modal True
    
    add "#00000088"
    
    default local_selected_item = None
    default show_target_selection = False
    default confirm_target = None
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 600
        background "#e8d5b8"
        padding (20, 20)
        
        vbox:
            spacing 15
            xfill True
            
            # Header
            frame:
                background "#8b5a2b"
                xalign 0.5
                padding (30, 10)
                text "Inventory" color "#fff8e7" size 28 bold True
            
            # Show lock status
            if inventory_locked:
                frame:
                    background "#ff4444"
                    xalign 0.5
                    padding (15, 5)
                    text "Items are currently locked" color "#ffffff" size 16
            
            hbox:
                spacing 20
                xfill True
                
                # Item list
                frame:
                    background "#dcbfa6"
                    xsize 400
                    ysize 400
                    padding (10, 10)
                    
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        
                        vbox:
                            spacing 8
                            
                            if curr_items:
                                for item_name, quantity in curr_items.items():
                                    $ is_selected = (local_selected_item == item_name)
                                    button:
                                        xfill True
                                        if is_selected:
                                            style "item_button_selected"
                                        else:
                                            style "item_button_normal"
                                        action SetScreenVariable("local_selected_item", item_name)
                                        
                                        hbox:
                                            spacing 10
                                            text item_name color "#fff8e7" size 18
                                            text "x[quantity]" color "#ffd700" size 18 xalign 1.0
                            else:
                                text "No items" color "#5c3d2e" size 18 xalign 0.5
                
                # Item info
                frame:
                    background "#dcbfa6"
                    xsize 420
                    ysize 400
                    padding (15, 15)
                    
                    vbox:
                        spacing 15
                        
                        if local_selected_item and local_selected_item in items:
                            $ item_info = items[local_selected_item]
                            
                            text local_selected_item color "#5c3d2e" size 24 bold True
                            
                            frame:
                                background "#e8d5b8"
                                xfill True
                                padding (10, 10)
                                text item_info.get('description', 'No description') color "#3d2817" size 16
                            
                            null height 20
                            
                            if not inventory_locked:
                                textbutton "Use Item":
                                    xalign 0.5
                                    style "battle_menu_button"
                                    text_style "battle_menu_button_text"
                                    action SetScreenVariable("show_target_selection", True)
                            else:
                                frame:
                                    background "#666666"
                                    xalign 0.5
                                    padding (20, 12)
                                    text "Items Locked" color "#aaaaaa" size 22
                        else:
                            text "Select an item to view details" color "#8b5a2b" size 18 xalign 0.5 yalign 0.5
            
            # Close button
            textbutton "Close":
                xalign 0.5
                style "battle_menu_button"
                text_style "battle_menu_button_text"
                action Return()
    
    # Target selection window
    if show_target_selection and local_selected_item and not inventory_locked:
        frame:
            xalign 0.5
            yalign 0.5
            xsize 500
            ysize 450
            background "#e8d5b8"
            padding (20, 20)
            
            vbox:
                spacing 15
                
                frame:
                    background "#8b5a2b"
                    xalign 0.5
                    padding (20, 8)
                    text "Select Target" color "#fff8e7" size 22 bold True
                
                text "Apply [local_selected_item] to:" color "#5c3d2e" size 18 xalign 0.5
                
                # Party member list
                vbox:
                    spacing 10
                    xalign 0.5
                    
                    for char_key, char_data in party_characters.items():
                        $ can_use = can_use_item_on_target(local_selected_item, char_key)
                        button:
                            xsize 350
                            if can_use:
                                background "#5c3d2e"
                                hover_background "#7a5040"
                            else:
                                background "#3a3a3a"
                            padding (15, 10)
                            if can_use:
                                action SetScreenVariable("confirm_target", char_key)
                            
                            hbox:
                                spacing 15
                                
                                # Mini portrait
                                frame:
                                    background "#1a1a1a"
                                    xsize 50
                                    ysize 50
                                    if char_data.get('portrait'):
                                        add char_data['portrait'] xalign 0.5 yalign 0.5 fit "contain"
                                
                                vbox:
                                    if can_use:
                                        text char_data['name'] color "#fff8e7" size 18
                                    else:
                                        text char_data['name'] color "#888888" size 18
                                    hbox:
                                        spacing 10
                                        text "HP: [char_data['hp']]/[char_data['max_hp']]" color "#4caf50" size 14
                                        text "MP: [char_data['mp']]/[char_data['max_mp']]" color "#29b6f6" size 14
                                    if not can_use:
                                        text "(Cannot use on this target)" color "#ff6666" size 12
                
                hbox:
                    spacing 20
                    xalign 0.5
                    
                    textbutton "Cancel":
                        style "battle_menu_button"
                        text_style "battle_menu_button_text"
                        action SetScreenVariable("show_target_selection", False)
    
    # Confirmation window
    if confirm_target and local_selected_item:
        $ target_name = party_characters.get(confirm_target, {}).get('name', 'Unknown')
        
        frame:
            xalign 0.5
            yalign 0.5
            xsize 400
            ysize 200
            background "#e8d5b8"
            padding (20, 20)
            
            vbox:
                spacing 20
                xalign 0.5
                
                text "Confirm" color "#5c3d2e" size 24 bold True xalign 0.5
                text "Apply [local_selected_item] to [target_name]?" color "#3d2817" size 18 xalign 0.5
                
                hbox:
                    spacing 30
                    xalign 0.5
                    
                    textbutton "Yes":
                        style "battle_menu_button"
                        text_style "battle_menu_button_text"
                        action [
                            Function(use_item, local_selected_item, confirm_target),
                            SetScreenVariable("confirm_target", None),
                            SetScreenVariable("show_target_selection", False),
                            SetScreenVariable("local_selected_item", None)
                        ]
                    
                    textbutton "No":
                        style "battle_menu_button"
                        text_style "battle_menu_button_text"
                        action SetScreenVariable("confirm_target", None)


# ============================================================================
# BATTLE PREPARATION MENU
# ============================================================================

screen battle_menu():
    tag menu
    modal True
    
    # Darkening background
    add "#00000088"
    
    # Main container
    frame:
        xfill True
        yfill True
        background None
        padding (40, 30, 40, 30)
        
        vbox:
            xfill True
            yfill True
            spacing 15
            
            # === HEADER ===
            frame:
                background "#8b5a2b"
                xalign 0.5
                padding (40, 10)
                
                text "Battle Preparation" style "battle_title_text"
            
            # === MAIN AREA ===
            hbox:
                spacing 30
                xalign 0.5
                yalign 0.5
                
                # --- LEFT MENU ---
                vbox:
                    spacing 12
                    xsize 300
                    
                    # Items/Inventory
                    textbutton "Items":
                        style "battle_menu_button"
                        text_style "battle_menu_button_text"
                        action ShowMenu("inventory")
                    
                    # View characters
                    textbutton "Characters":
                        style "battle_menu_button"
                        text_style "battle_menu_button_text"
                        action ShowMenu("characters")
                    
                    # Separator
                    null height 20
                    
                    # Back (close menu without battle)
                    textbutton "Back":
                        style "battle_menu_button"
                        text_style "battle_menu_button_text"
                        action Return("cancel")
                    
                    # Large separator before battle button
                    null height 40
                    
                    # START BATTLE - main button
                    textbutton "Start Battle":
                        style "battle_start_button"
                        text_style "battle_start_button_text"
                        action Return("start_battle")
                
                # --- RIGHT PANEL: BATTLE PARTICIPANTS ---
                frame:
                    background "#dcbfa6"
                    xsize 650
                    ysize 450
                    padding (15, 15)
                    
                    vbox:
                        spacing 15
                        xfill True
                        
                        # Panel header
                        frame:
                            background "#8b5a2b"
                            xalign 0.5
                            xsize 300
                            padding (15, 8)
                            
                            text "Battle Participants" color "#fff8e7" size 24 bold True xalign 0.5
                        
                        # Character slots
                        hbox:
                            spacing 20
                            xalign 0.5
                            yalign 0.3
                            
                            for char_key, char_data in party_characters.items():
                                use battle_character_slot(char_key, char_data)
                        
                        # Bottom info panel
                        frame:
                            background "#e8d5b8"
                            xalign 0.5
                            xsize 580
                            ysize 120
                            padding (15, 15)
                            
                            if selected_character:
                                use battle_character_info(selected_character)
                            else:
                                text "Select a character to view information" xalign 0.5 yalign 0.5 color "#8b5a2b" size 18


# === COMPONENT: CHARACTER SLOT ===
screen battle_character_slot(char_key, char_data):
    button:
        background "#5c3d2e"
        hover_background "#7a5040"
        xsize 200
        ysize 220
        padding (5, 5)
        action SetVariable("selected_character", char_data)
        
        vbox:
            spacing 8
            xalign 0.5
            
            # Character portrait
            frame:
                background "#1a1a1a"
                xsize 140
                ysize 140
                xalign 0.5
                
                if char_data.get('portrait'):
                    add char_data['portrait'] xalign 0.5 yalign 0.5 fit "contain"
                else:
                    # Color placeholder for testing
                    if char_key == "saito":
                        add Solid("#1a237e") xsize 130 ysize 130 xalign 0.5 yalign 0.5
                    else:
                        add Solid("#7b1fa2") xsize 130 ysize 130 xalign 0.5 yalign 0.5
            
            # HP bar
            hbox:
                spacing 5
                xalign 0.5
                text "HP" style "battle_bar_label"
                bar:
                    style "battle_hp_bar"
                    value char_data['hp']
                    range char_data['max_hp']
            
            # MP bar
            hbox:
                spacing 5
                xalign 0.5
                text "MP" style "battle_bar_label"
                bar:
                    style "battle_mp_bar"
                    value char_data['mp']
                    range char_data['max_mp']


# === COMPONENT: CHARACTER INFO ===
screen battle_character_info(char_data):
    hbox:
        spacing 20
        xfill True
        
        # Mini portrait
        frame:
            background "#5c3d2e"
            xsize 80
            ysize 80
            padding (5, 5)
            
            if char_data.get('portrait'):
                add char_data['portrait'] xalign 0.5 yalign 0.5 fit "contain"
            else:
                add Solid("#333333") xsize 70 ysize 70 xalign 0.5 yalign 0.5
        
        # Info
        vbox:
            spacing 5
            
            text char_data.get('name', 'Unknown') color "#5c3d2e" size 20 bold True
            
            # Attack type based on is_mage
            $ attack_type = get_attack_type(char_data)
            text "Type: [attack_type]" color "#8b5a2b" size 16
            
            hbox:
                spacing 20
                text "HP: [char_data['hp']]/[char_data['max_hp']]" color "#4caf50" size 16
                text "MP: [char_data['mp']]/[char_data['max_mp']]" color "#29b6f6" size 16


# === CHARACTERS SCREEN ===
screen characters():
    tag menu
    modal True
    
    add "#00000088"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 550
        background "#e8d5b8"
        padding (20, 20)
        
        vbox:
            spacing 15
            
            frame:
                background "#8b5a2b"
                xalign 0.5
                padding (30, 10)
                text "Party Members" color "#fff8e7" size 28 bold True
            
            hbox:
                spacing 20
                xalign 0.5
                
                for char_key, char_data in party_characters.items():
                    use character_detail_card(char_key, char_data)
            
            textbutton "Close":
                xalign 0.5
                style "battle_menu_button"
                text_style "battle_menu_button_text"
                action Return()


# Character card for characters screen
screen character_detail_card(char_key, char_data):
    frame:
        background "#dcbfa6"
        xsize 200
        ysize 320
        padding (10, 10)
        
        vbox:
            spacing 8
            xalign 0.5
            
            # Portrait
            frame:
                background "#5c3d2e"
                xsize 100
                ysize 100
                xalign 0.5
                padding (5, 5)
                
                if char_data.get('portrait'):
                    add char_data['portrait'] xalign 0.5 yalign 0.5 fit "contain"
                else:
                    add Solid("#333333") xsize 90 ysize 90 xalign 0.5 yalign 0.5
            
            text char_data.get('name', 'Unknown') color "#5c3d2e" size 16 bold True xalign 0.5
            
            # Attack type based on is_mage
            $ attack_type = get_attack_type(char_data)
            text "[attack_type]" color "#8b5a2b" size 12 xalign 0.5
            
            if char_data.get('hp') is not None and char_data.get('max_hp') is not None:
                text "HP: [char_data['hp']]/[char_data['max_hp']]" color "#4caf50" size 12 xalign 0.5
            
            if char_data.get('mp') is not None and char_data.get('max_mp') is not None:
                text "MP: [char_data['mp']]/[char_data['max_mp']]" color "#29b6f6" size 12 xalign 0.5
            
            if char_data.get('attack') is not None:
                text "ATK: [char_data['attack']]" color "#ff6b6b" size 12 xalign 0.5
            
            if char_data.get('defense') is not None:
                text "DEF: [char_data['defense']]" color "#4dabf7" size 12 xalign 0.5


# ============================================================================
# BATTLE SCREEN
# ============================================================================

screen battle_screen():
    tag battle
    modal True
    
    # Battle background - fallback solid color first, then image on top
    add Solid("#2d4a2d")
    add "images/battle/forest_bg.png" xalign 0.5 yalign 0.5
    
    default action_menu = "main"  # main, attack, skills, items, target_enemy, target_ally, defense_target
    default local_selected_skill = None
    default local_selected_item = None
    default show_char_info = None
    default battle_log = []
    
    # Enemies (top of screen)
    hbox:
        xalign 0.5
        yalign 0.2
        spacing 100
        
        for enemy in enemies:
            if enemy.get('hp', 0) > 0:
                button:
                    background None
                    if action_menu == "target_enemy":
                        action [
                            Function(execute_player_attack, local_selected_skill, enemy),
                            SetScreenVariable("action_menu", "main"),
                            SetScreenVariable("local_selected_skill", None)
                        ]
                    
                    vbox:
                        spacing 5
                        
                        # Enemy sprite
                        frame:
                            background None
                            xsize 200
                            ysize 250
                            
                            # Placeholder if no sprite
                            add Solid("#4a3a5a") xsize 150 ysize 200 xalign 0.5 yalign 0.5
                            
                            if enemy.get('sprite'):
                                add enemy['sprite'] xalign 0.5 yalign 0.5 fit "contain"
                        
                        # Enemy name and HP (visible when targeting)
                        if action_menu == "target_enemy":
                            frame:
                                background "#000000aa"
                                padding (10, 5)
                                xalign 0.5
                                
                                vbox:
                                    spacing 3
                                    text enemy['name'] color "#ffffff" size 16 xalign 0.5
                                    bar:
                                        value enemy['hp']
                                        range enemy['max_hp']
                                        xsize 120
                                        ysize 10
                                        left_bar Solid("#ff4444")
                                        right_bar Solid("#333333")
    
    # Character cards (bottom)
    hbox:
        xalign 0.5
        yalign 0.85
        spacing 20
        
        $ party = get_alive_party_members()
        $ current_actor_data = get_current_actor()
        
        for idx, (char_key, char_data) in enumerate(party):
            $ is_active = (battle_phase == "player" and idx == current_turn_index)
            
            button:
                if is_active:
                    style "battle_card_active"
                elif battle_phase != "player":
                    style "battle_card_inactive"
                else:
                    style "battle_card"
                xsize 180
                ysize 220
                action SetScreenVariable("show_char_info", char_key if show_char_info != char_key else None)
                
                vbox:
                    spacing 5
                    xalign 0.5
                    
                    # Portrait
                    frame:
                        background "#1a1a1a"
                        xsize 120
                        ysize 120
                        xalign 0.5
                        
                        # Select portrait based on state
                        $ portrait_key = 'portrait_' + char_data.get('state', 'normal')
                        $ portrait = char_data.get(portrait_key, char_data.get('portrait'))
                        
                        if portrait:
                            add portrait xalign 0.5 yalign 0.5 fit "contain"
                        else:
                            add Solid("#333355") xsize 110 ysize 110 xalign 0.5 yalign 0.5
                    
                    # HP bar
                    hbox:
                        spacing 5
                        xalign 0.5
                        text "HP" color "#ffffff" size 12 bold True
                        bar:
                            value char_data['hp']
                            range char_data['max_hp']
                            xsize 100
                            ysize 12
                            left_bar Solid("#4caf50")
                            right_bar Solid("#2d2d2d")
                    
                    # MP bar
                    hbox:
                        spacing 5
                        xalign 0.5
                        text "MP" color "#ffffff" size 12 bold True
                        bar:
                            value char_data['mp']
                            range char_data['max_mp']
                            xsize 100
                            ysize 12
                            left_bar Solid("#29b6f6")
                            right_bar Solid("#2d2d2d")
                    
                    # Defense status
                    if char_key in defense_buffs:
                        frame:
                            background "#ffd700aa"
                            padding (5, 2)
                            xalign 0.5
                            vbox:
                                text "Defense" color "#000000" size 10 xalign 0.5
                                text "+50" color "#000000" size 10 xalign 0.5
                                text "Boost" color "#006400" size 8 xalign 0.5
    
    # Action menu (right side)
    if battle_phase == "player" and current_actor_data:
        $ actor_key, actor = current_actor_data
        
        frame:
            xalign 0.95
            yalign 0.4
            background "#8b5a2bcc"
            padding (15, 15)
            
            vbox:
                spacing 10
                
                # Main menu
                if action_menu == "main":
                    text "[actor['name']]'s Turn" color "#fff8e7" size 18 bold True xalign 0.5
                    
                    null height 10
                    
                    textbutton "Attack":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "skills")
                    
                    textbutton "Defense":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "defense_target")
                    
                    textbutton "Items":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "items")
                
                # Skills menu
                elif action_menu == "skills":
                    text "Select Skill" color "#fff8e7" size 18 bold True xalign 0.5
                    
                    null height 5
                    
                    for skill_key in actor.get('skills', []):
                        if skill_key in skills:
                            $ skill_data = skills[skill_key]
                            $ can_use = actor['mp'] >= skill_data.get('consume', 0)
                            
                            button:
                                xsize 180
                                if can_use:
                                    style "skill_button_enabled"
                                else:
                                    style "skill_button_disabled"
                                
                                if can_use:
                                    if skill_data.get('is_aoe'):
                                        action [
                                            SetScreenVariable("local_selected_skill", skill_key),
                                            Function(execute_aoe_attack, actor_key, skill_key),
                                            SetScreenVariable("action_menu", "main")
                                        ]
                                    elif skill_data.get('is_heal') or skill_data.get('is_buff'):
                                        action [
                                            SetScreenVariable("local_selected_skill", skill_key),
                                            SetScreenVariable("action_menu", "target_ally")
                                        ]
                                    else:
                                        action [
                                            SetScreenVariable("local_selected_skill", skill_key),
                                            SetScreenVariable("action_menu", "target_enemy")
                                        ]
                                
                                vbox:
                                    spacing 2
                                    $ text_color = "#fff8e7" if can_use else "#888888"
                                    $ mp_color = "#29b6f6" if can_use else "#555555"
                                    text skill_data['name'] color text_color size 14
                                    hbox:
                                        spacing 10
                                        text "MP: [skill_data['consume']]" color mp_color size 12
                                        if skill_data.get('cast_turns', 0) > 0:
                                            text "Cast: [skill_data['cast_turns']]" color "#ffd700" size 12
                    
                    null height 10
                    
                    textbutton "Back":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "main")
                
                # Target selection for attack
                elif action_menu == "target_enemy":
                    text "Select Enemy" color "#fff8e7" size 18 bold True xalign 0.5
                    text "(Click on enemy sprite)" color "#cccccc" size 14 xalign 0.5
                    
                    null height 10
                    
                    textbutton "Back":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "skills")
                
                # Ally selection (heal/buff)
                elif action_menu == "target_ally":
                    text "Select Ally" color "#fff8e7" size 18 bold True xalign 0.5
                    
                    for ally_key, ally_data in party:
                        button:
                            xsize 180
                            background "#5c3d2e"
                            hover_background "#7a5040"
                            padding (8, 6)
                            action [
                                Function(execute_support_skill, actor_key, local_selected_skill, ally_key),
                                SetScreenVariable("action_menu", "main"),
                                SetScreenVariable("local_selected_skill", None)
                            ]
                            
                            hbox:
                                spacing 10
                                text ally_data['name'] color "#fff8e7" size 14
                                text "HP:[ally_data['hp']]" color "#4caf50" size 12
                    
                    null height 10
                    
                    textbutton "Back":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "skills")
                
                # Defense target selection
                elif action_menu == "defense_target":
                    text "Defend Who?" color "#fff8e7" size 18 bold True xalign 0.5
                    
                    for ally_key, ally_data in party:
                        button:
                            xsize 180
                            background "#5c3d2e"
                            hover_background "#7a5040"
                            padding (8, 6)
                            action [
                                Function(apply_defense, ally_key),
                                Function(next_turn),
                                SetScreenVariable("action_menu", "main")
                            ]
                            
                            text ally_data['name'] color "#fff8e7" size 14
                    
                    null height 10
                    
                    textbutton "Back":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "main")
                
                # Items menu
                elif action_menu == "items":
                    text "Select Item" color "#fff8e7" size 18 bold True xalign 0.5
                    
                    if curr_items:
                        for item_name, quantity in curr_items.items():
                            button:
                                xsize 180
                                background "#5c3d2e"
                                hover_background "#7a5040"
                                padding (8, 6)
                                action [
                                    SetScreenVariable("local_selected_item", item_name),
                                    SetScreenVariable("action_menu", "item_target")
                                ]
                                
                                hbox:
                                    spacing 10
                                    text item_name color "#fff8e7" size 14
                                    text "x[quantity]" color "#ffd700" size 14
                    else:
                        text "No items" color "#888888" size 14 xalign 0.5
                    
                    null height 10
                    
                    textbutton "Back":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "main")
                
                # Item target selection
                elif action_menu == "item_target":
                    text "Use [local_selected_item] on:" color "#fff8e7" size 16 bold True xalign 0.5
                    
                    for ally_key, ally_data in party:
                        $ can_use = can_use_item_on_target(local_selected_item, ally_key)
                        button:
                            xsize 180
                            if can_use:
                                background "#5c3d2e"
                                hover_background "#7a5040"
                            else:
                                background "#3a3a3a"
                            padding (8, 6)
                            if can_use:
                                action [
                                    Function(use_item_in_battle, local_selected_item, ally_key),
                                    SetScreenVariable("action_menu", "main"),
                                    SetScreenVariable("local_selected_item", None)
                                ]
                            
                            hbox:
                                spacing 10
                                if can_use:
                                    text ally_data['name'] color "#fff8e7" size 14
                                else:
                                    text ally_data['name'] color "#888888" size 14
                                text "HP:[ally_data['hp']]" color "#4caf50" size 12
                    
                    null height 10
                    
                    textbutton "Back":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "items")
    
    # Process enemy turn automatically when it's their phase
    if battle_phase == "enemy":
        timer 0.5 action Function(process_enemy_turns)
    
    # Action message (center of screen)
    if battle_message:
        frame:
            xalign 0.5
            yalign 0.5
            background "#000000cc"
            padding (30, 15)
            
            text battle_message color "#ffffff" size 24 bold True
    
    # Victory screen
    if battle_phase == "victory":
        frame:
            xalign 0.5
            yalign 0.4
            background "#ffd700ee"
            padding (60, 40)
            
            vbox:
                spacing 20
                
                text "VICTORY!" color "#3d2817" size 48 bold True xalign 0.5
                
                textbutton "Continue":
                    xalign 0.5
                    style "battle_start_button"
                    text_style "battle_start_button_text"
                    action Return("victory")
    
    # Defeat screen
    if battle_phase == "defeat":
        frame:
            xalign 0.5
            yalign 0.4
            background "#8b0000ee"
            padding (60, 40)
            
            vbox:
                spacing 20
                
                text "DEFEAT" color "#ffffff" size 48 bold True xalign 0.5
                
                textbutton "Retry":
                    xalign 0.5
                    style "battle_start_button"
                    text_style "battle_start_button_text"
                    action Return("defeat")
    
    # Character info window
    if show_char_info:
        $ info_char = party_characters.get(show_char_info, {})
        
        frame:
            xalign 0.05
            yalign 0.3
            xsize 280
            background "#e8d5b8ee"
            padding (15, 15)
            
            vbox:
                spacing 8
                
                text info_char.get('name', 'Unknown') color "#5c3d2e" size 22 bold True
                
                # Attack type based on is_mage
                $ attack_type = get_attack_type(info_char)
                text "Type: [attack_type]" color "#8b5a2b" size 14
                
                null height 5
                
                # Status Panel
                text "--- Status Panel ---" color "#5c3d2e" size 14 bold True
                text "HP: [info_char['hp']]/[info_char['max_hp']]" color "#4caf50" size 16
                text "MP: [info_char['mp']]/[info_char['max_mp']]" color "#29b6f6" size 16
                $ cooldown = info_char.get('cooldown', 0)
                if cooldown > 0:
                    text "[cooldown] Turns Wait" color "#ffd700" size 14
                else:
                    text "0 Turns Wait (Ready)" color "#4caf50" size 14
                
                null height 5
                
                text "Attack Power: [info_char.get('attack', 0)]" color "#ff6b6b" size 14
                text "Defense: [info_char.get('defense', 0)]" color "#4dabf7" size 14
                text "Agility: [info_char.get('agility', 0)]" color "#69db7c" size 14
                text "Accuracy: [info_char.get('accuracy', 0)]%" color "#fcc419" size 14
                
                null height 10
                
                text "Skills:" color "#5c3d2e" size 16 bold True
                
                for skill_key in info_char.get('skills', []):
                    if skill_key in skills:
                        $ s = skills[skill_key]
                        vbox:
                            spacing 2
                            text "* [s['name']]" color "#3d2817" size 12
                            text "  MP: [s['consume']] - [s.get('description', '')]" color "#666666" size 10
                
                null height 10
                
                textbutton "Close":
                    xalign 0.5
                    background "#5c3d2e"
                    hover_background "#7a5040"
                    padding (10, 5)
                    action SetScreenVariable("show_char_info", None)
                    text_color "#fff8e7"
                    text_size 14


# ============================================================================
# BATTLE SCREEN FUNCTIONS
# ============================================================================

init python:
    def execute_player_attack(skill_key, target_enemy):
        """Executes player attack on enemy"""
        actor_data = get_current_actor()
        if not actor_data:
            return
        
        actor_key, actor = actor_data
        skill_data = store.skills.get(skill_key)
        
        if not skill_data:
            return
        
        # Show message
        store.battle_message = "{} uses {}!".format(actor['name'], skill_data['name'])
        
        # Execute attack
        result = perform_attack(actor_key, actor, skill_key, target_enemy)
        
        if result and result.get('success'):
            for res in result.get('results', []):
                if res.get('dodged'):
                    target_enemy['state'] = 'happy'
                    store.battle_message = "The character ({}) successfully dodged the attack!".format(target_enemy['name'])
                elif res.get('hit'):
                    target_enemy['state'] = 'hurt'
                    dmg = res.get('damage', 0)
                    store.battle_message = "{} deals {} damage to {}!".format(actor['name'], dmg, target_enemy['name'])
        
        # Next turn
        next_turn()
        
        # Clear message after a delay (use timer in real game)
        store.battle_message = ""

    def execute_aoe_attack(actor_key, skill_key):
        """Executes AOE attack"""
        actor = store.party_characters.get(actor_key)
        skill_data = store.skills.get(skill_key)
        
        if not actor or not skill_data:
            return
        
        cast_turns = skill_data.get('cast_turns', 0)
        
        if cast_turns > 0:
            # Start casting
            store.aoe_casting[actor_key] = {
                'skill': skill_key,
                'turns_left': cast_turns
            }
            actor['cooldown'] = cast_turns
            store.battle_message = "{} is casting {}... ({} turns)".format(actor['name'], skill_data['name'], cast_turns)
        else:
            # Instant AOE
            store.battle_message = "{} uses {}!".format(actor['name'], skill_data['name'])
            result = perform_attack(actor_key, actor, skill_key, None)
        
        next_turn()
        store.battle_message = ""

    def execute_support_skill(actor_key, skill_key, target_key):
        """Executes support skill"""
        actor = store.party_characters.get(actor_key)
        target = store.party_characters.get(target_key)
        skill_data = store.skills.get(skill_key)
        
        if not actor or not target or not skill_data:
            return
        
        store.battle_message = "{} uses {} on {}!".format(actor['name'], skill_data['name'], target['name'])
        
        result = perform_attack(actor_key, actor, skill_key, target)
        
        if result and result.get('success'):
            for res in result.get('results', []):
                if res.get('heal'):
                    store.battle_message = "{} recovered {} HP!".format(target['name'], res['heal'])
                elif res.get('buff'):
                    store.battle_message = "{}'s {} increased!".format(target['name'], res['buff'])
        
        next_turn()
        store.battle_message = ""

    def use_item_in_battle(item_name, target_key):
        """Uses item in battle (character loses turn)"""
        actor_data = get_current_actor()
        if not actor_data:
            return
        
        actor_key, actor = actor_data
        target = store.party_characters.get(target_key)
        
        if not target:
            return
        
        store.battle_message = "{} uses {} on {}!".format(actor['name'], item_name, target['name'])
        
        success = use_item(item_name, target_key)
        
        if success:
            target['state'] = 'happy'
        
        next_turn()
        store.battle_message = ""

    def process_enemy_turns():
        """Processes enemy turns"""
        results = enemy_turn()
        
        for r in results:
            enemy = r['attacker']
            skill = r['skill']
            target = r['target']
            
            store.battle_message = "{} uses {}! Target: {}".format(enemy['name'], skill['name'], target['name'])
            
            for res in r.get('results', []):
                if res.get('dodged'):
                    target['state'] = 'happy'
                elif res.get('hit') and res.get('damage'):
                    target['state'] = 'hurt'
        
        # Check victory/defeat after enemy turn
        if not get_alive_enemies():
            store.battle_phase = "victory"
        elif not get_alive_party_members():
            store.battle_phase = "defeat"
        else:
            # Return turn to player
            store.battle_phase = "player"
            store.current_turn_index = 0
        
        # Update buffs
        update_defense_buffs()
        update_aoe_casting()
        
        store.battle_message = ""


# ============================================================================
# USAGE EXAMPLE - CORRECT WAY TO USE
# ============================================================================

# In your script.rpy, use like this:
#
# label forest_battle:
#     # Show battle preparation menu
#     call screen battle_menu
#     
#     if _return == "start_battle":
#         # Initialize battle state
#         $ init_battle(["mage", "mage"])
#         
#         # Show battle screen and get result
#         call screen battle_screen
#         
#         if _return == "victory":
#             "You won the battle!"
#         else:
#             "Game Over..."
#     elif _return == "cancel":
#         "You decided not to fight."
#     
#     return
#
# 
# To lock/unlock inventory from anywhere:
#     $ lock_inventory()
#     $ unlock_inventory()
#
# To add a character to party:
#     $ party_characters['tabitha'] = dict(all_characters['tabitha'])
#
# To remove a character from party:
#     $ del party_characters['tabitha']
