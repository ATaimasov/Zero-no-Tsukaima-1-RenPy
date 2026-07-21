# ============================================================================
# ZERO NO TSUKAIMA - BATTLE SYSTEM  (rewrite)
# FILE 1/4: DATA
# ----------------------------------------------------------------------------
# Single source of truth for every combatant (allies AND enemies), every
# skill and every item. Nothing about a unit lives anywhere else.
#
# A "template" here is plain, save-safe data (strings / numbers / lists /
# dicts). At the start of a battle each template is deep-copied into a live
# "combatant" instance (see battle_logic.rpy -> make_unit).
# ============================================================================

# Background shown behind the battle HUD.
define BATTLE_BG = "images/battle/forest_bg.png"

# ----------------------------------------------------------------------------
# SKILLS
# ----------------------------------------------------------------------------
# Fields:
#   name        - display name
#   consume     - MP cost
#   description - shown in tooltips / info panel
#   power       - base damage / heal amount
#   accuracy    - base hit chance (0-100); combined with the caster's accuracy
#   element     - flavour tag
#   target      - "enemy" (single foe) | "all_enemies" (AoE) | "ally" (single ally)
#   kind        - "damage" | "heal" | "buff"
#   buff_stat   - for kind=="buff": which stat is raised
#   buff_value  - for kind=="buff": by how much
#   cast_turns  - 0 = resolves instantly. 1-2 = AoE that "charges" for N of the
#                 caster's own turns before it fires (plays the cast video).
#   anim        - short label used on the animation window when no video exists
# ----------------------------------------------------------------------------
define skills = {
    # --- Saito (physical) ---
    "slash": {
        "name": "Slash", "consume": 0, "power": 35, "accuracy": 95,
        "element": "physical", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "slash",
        "description": "A quick sword strike on a single foe.",
    },
    "d_slash": {
        "name": "Double Slash", "consume": 20, "power": 60, "accuracy": 90,
        "element": "physical", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "double_slash",
        "description": "Two heavy strikes on a single foe.",
    },
    "wind_moon_slash": {
        "name": "Wind Moon Slash", "consume": 60, "power": 55, "accuracy": 85,
        "element": "wind", "target": "all_enemies", "kind": "damage",
        "cast_turns": 2, "anim": "wind_slash",
        "description": "Charged crescent of wind that hits ALL foes. Charges 2 turns.",
    },

    # --- Louise (void) ---
    "arrow": {
        "name": "Magic Arrow", "consume": 20, "power": 45, "accuracy": 90,
        "element": "void", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "magic_arrow",
        "description": "A bolt of void magic on a single foe.",
    },
    "heroism": {
        "name": "Heroism", "consume": 45, "power": 85, "accuracy": 85,
        "element": "void", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "heroism",
        "description": "A powerful void blast on a single foe.",
    },
    "meteor": {
        "name": "Meteor", "consume": 70, "power": 65, "accuracy": 80,
        "element": "void", "target": "all_enemies", "kind": "damage",
        "cast_turns": 2, "anim": "meteor",
        "description": "Calls meteors down on ALL foes. Charges 2 turns.",
    },
    "dispel": {
        "name": "Dispel", "consume": 25, "kind": "buff", "buff_stat": "accuracy",
        "buff_value": 20, "target": "ally", "cast_turns": 0, "anim": "buff",
        "description": "Raises one ally's accuracy.",
    },

    # --- Shared support ---
    "heal": {
        "name": "Heal", "consume": 25, "power": 70, "kind": "heal",
        "target": "ally", "cast_turns": 0, "anim": "heal",
        "description": "Restores HP to one ally.",
    },

    # --- Tabitha (wind) ---
    "wing": {
        "name": "Wing", "consume": 20, "power": 40, "accuracy": 92,
        "element": "wind", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "wind",
        "description": "A slicing gust on a single foe.",
    },
    "air_needle": {
        "name": "Air Needle", "consume": 35, "power": 58, "accuracy": 88,
        "element": "wind", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "air_needle",
        "description": "Needles of wind pierce a single foe.",
    },
    "wind_break": {
        "name": "Wind Break", "consume": 65, "power": 50, "accuracy": 82,
        "element": "wind", "target": "all_enemies", "kind": "damage",
        "cast_turns": 2, "anim": "wind_storm",
        "description": "A hurricane strikes ALL foes. Charges 2 turns.",
    },

    # --- Kirche (fire) ---
    "fire": {
        "name": "Fire", "consume": 20, "power": 42, "accuracy": 88,
        "element": "fire", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "fire",
        "description": "A burst of flame on a single foe.",
    },
    "fire_needle": {
        "name": "Fire Needle", "consume": 35, "power": 60, "accuracy": 85,
        "element": "fire", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "fire_needle",
        "description": "Lances of fire pierce a single foe.",
    },
    "fire_arrow": {
        "name": "Fire Storm", "consume": 65, "power": 52, "accuracy": 80,
        "element": "fire", "target": "all_enemies", "kind": "damage",
        "cast_turns": 1, "anim": "fire_storm",
        "description": "A storm of fire engulfs ALL foes. Charges 1 turn.",
    },

    # --- Henrietta (water) ---
    "water": {
        "name": "Water", "consume": 20, "power": 40, "accuracy": 90,
        "element": "water", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "water",
        "description": "A jet of water on a single foe.",
    },
    "water_hazard": {
        "name": "Water Hazard", "consume": 65, "power": 50, "accuracy": 83,
        "element": "water", "target": "all_enemies", "kind": "damage",
        "cast_turns": 2, "anim": "water_storm",
        "description": "A flood crashes over ALL foes. Charges 2 turns.",
    },

    # --- Enemy skills ---
    "claw": {
        "name": "Claw", "consume": 0, "power": 30, "accuracy": 85,
        "element": "physical", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "slash",
        "description": "A savage swipe.",
    },
    "dark_bolt": {
        "name": "Dark Bolt", "consume": 15, "power": 44, "accuracy": 85,
        "element": "dark", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "magic_arrow",
        "description": "A bolt of dark magic.",
    },
    "dark_nova": {
        "name": "Dark Nova", "consume": 40, "power": 45, "accuracy": 80,
        "element": "dark", "target": "all_enemies", "kind": "damage",
        "cast_turns": 2, "anim": "meteor",
        "description": "A dark explosion hits the whole party. Charges 2 turns.",
    },
    "smash": {
        "name": "Smash", "consume": 0, "power": 48, "accuracy": 75,
        "element": "physical", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "double_slash",
        "description": "A heavy crushing blow.",
    },
}

# ----------------------------------------------------------------------------
# ITEMS  (usable on any ally during the "Item" action)
# ----------------------------------------------------------------------------
# effect: "hp" | "mp" | "both" | "revive"
define items = {
    "Bread":      {"name": "Bread",      "effect": "hp",     "hp": 60,             "description": "Restores 60 HP to one ally."},
    "Herb":       {"name": "Herb",       "effect": "mp",     "mp": 40,             "description": "Restores 40 MP to one ally."},
    "Elixir":     {"name": "Elixir",     "effect": "both",   "hp": 120, "mp": 60,  "description": "Restores 120 HP and 60 MP to one ally."},
    "Phoenix Feather": {"name": "Phoenix Feather", "effect": "revive", "ratio": 0.5, "description": "Revives a fallen ally with 50% HP."},
}

# Inventory carried into battle (persists across battles).
default inventory = {
    "Bread": 3,
    "Herb": 2,
    "Elixir": 1,
    "Phoenix Feather": 1,
}

# ----------------------------------------------------------------------------
# CHARACTERS  -  the single registry. Allies AND enemies live here together.
# ----------------------------------------------------------------------------
# Fields:
#   name, color            - name + speech colour (used for battle barks)
#   description            - shown in the info panel
#   is_mage                - True -> "Magic" type, False -> "Attack" type
#   is_enemy               - True for foes (drawn as sprites, not cards)
#   skills                 - list of skill keys from `skills`
#   hp/max_hp/mp/max_mp    - resources
#   attack/defense/agility/accuracy - stats
#   portrait               - card / info art (allies)
#   portrait_normal/hurt/happy - state art (allies, optional)
#   icon                   - mini icon (falls back to portrait)
#   sprite                 - full battle sprite (enemies)
#   cast_video             - webm played in the animation window on AoE
#   lines                  - optional battle barks: {attack, cast, hurt, defend, defeat, win}
# ----------------------------------------------------------------------------
define characters = {

    # ===================== ALLIES =====================
    "saito": {
        "name": "Saito", "color": "#3874a3",
        "description": "A Japanese boy summoned to this world by Louise and treated as her familiar. The legendary 'Gandalfr'.",
        "is_mage": False, "is_enemy": False,
        "skills": ["slash", "d_slash", "wind_moon_slash"],
        "hp": 255, "max_hp": 255, "mp": 100, "max_mp": 100,
        "attack": 45, "defense": 30, "agility": 35, "accuracy": 95,
        "portrait": "gui/portraits/s.png",
        "portrait_normal": "gui/portraits/s.png",
        "portrait_happy": "gui/portraits/s_happy.png",
        "portrait_hurt": "gui/portraits/s_hurt.png",
        "icon": "gui/portraits/s.png",
        "cast_video": "video/cast/saito_cast.webm",
        "lines": {
            "attack": ["Here goes!", "Take this!", "Derf, back me up!"],
            "cast": ["Wind Moon Slash... charging up!", "Give me a second!"],
            "hurt": ["Guh!", "That stings!"],
            "defend": ["I'll hold the line.", "Come at me!"],
            "defeat": ["Damn... it...", "Louise... run..."],
            "win": ["Phew, that's over.", "We did it!"],
        },
    },
    "louise": {
        "name": "Louise", "color": "#fd7589",
        "description": "The mage who summoned Saito. She wields the lost element of Void, though its true nature is unknown.",
        "is_mage": True, "is_enemy": False,
        "skills": ["arrow", "heroism", "meteor", "dispel", "heal"],
        "hp": 200, "max_hp": 200, "mp": 150, "max_mp": 150,
        "attack": 25, "defense": 20, "agility": 30, "accuracy": 85,
        "portrait": "gui/portraits/l.png",
        "portrait_normal": "gui/portraits/l.png",
        "portrait_happy": "gui/portraits/l_happy.png",
        "portrait_hurt": "gui/portraits/l_hurt.png",
        "icon": "gui/portraits/l.png",
        "cast_video": "video/cast/louise_cast.webm",
        "lines": {
            "attack": ["Don't underestimate me!", "You asked for this!"],
            "cast": ["I'm gathering my power... wait!", "The Void answers me!"],
            "hurt": ["Kyaa!", "How dare you!"],
            "defend": ["I'll guard myself.", "Hmph, come on then."],
            "defeat": ["I... I can't...", "Saito..."],
            "win": ["Of course I won.", "Was there ever any doubt?"],
        },
    },
    "tabitha": {
        "name": "Tabitha", "color": "#b4dfec",
        "description": "Louise's classmate. A quiet chevalier who specialises in wind magic. Nicknamed 'Tabitha of the Snow Wind'.",
        "is_mage": True, "is_enemy": False,
        "skills": ["wing", "air_needle", "wind_break", "heal"],
        "hp": 180, "max_hp": 180, "mp": 180, "max_mp": 180,
        "attack": 20, "defense": 18, "agility": 40, "accuracy": 90,
        "portrait": "gui/portraits/t.png",
        "portrait_normal": "gui/portraits/t.png",
        "portrait_happy": "gui/portraits/t_happy.png",
        "portrait_hurt": "gui/portraits/t_hurt.png",
        "icon": "gui/portraits/t.png",
        "cast_video": "video/cast/tabitha_cast.webm",
        "lines": {
            "attack": ["...Wind.", "Sylphid."],
            "cast": ["...Charging.", "...Wait for it."],
            "hurt": ["...!", "..."],
            "defend": ["...Guard."],
        },
    },
    "kirche": {
        "name": "Kirche", "color": "#e36566",
        "description": "Louise's rival and classmate. A passionate fire mage nicknamed 'Kirche of the Mild Fever'.",
        "is_mage": True, "is_enemy": False,
        "skills": ["fire", "fire_needle", "fire_arrow", "heal"],
        "hp": 190, "max_hp": 190, "mp": 170, "max_mp": 170,
        "attack": 22, "defense": 22, "agility": 28, "accuracy": 88,
        "portrait": "gui/portraits/k.png",
        "portrait_normal": "gui/portraits/k.png",
        "portrait_happy": "gui/portraits/k_happy.png",
        "portrait_hurt": "gui/portraits/k_hurt.png",
        "icon": "gui/portraits/k.png",
        "cast_video": "video/cast/kirche_cast.webm",
        "lines": {
            "attack": ["Feel the heat, darling!", "Burn!"],
            "cast": ["Let me warm things up...", "Almost ready~"],
            "hurt": ["Ouch!", "You'll pay for that."],
            "defend": ["I'll cover myself."],
        },
    },
    "henrietta": {
        "name": "Henrietta", "color": "#782163",
        "description": "Princess of Tristain and Louise's childhood friend. A gentle water mage.",
        "is_mage": True, "is_enemy": False,
        "skills": ["water", "water_hazard", "heal"],
        "hp": 185, "max_hp": 185, "mp": 175, "max_mp": 175,
        "attack": 23, "defense": 25, "agility": 32, "accuracy": 87,
        "portrait": "gui/portraits/h.png",
        "portrait_normal": "gui/portraits/h.png",
        "portrait_happy": "gui/portraits/h_happy.png",
        "portrait_hurt": "gui/portraits/h_hurt.png",
        "icon": "gui/portraits/h.png",
        "cast_video": "video/cast/henrietta_cast.webm",
        "lines": {
            "attack": ["Forgive me.", "For Tristain!"],
            "cast": ["Grant me strength...", "One moment."],
            "hurt": ["Ah!", "I mustn't fall here."],
            "defend": ["I'll protect myself."],
        },
    },

    # ===================== ENEMIES =====================
    "mage": {
        "name": "Dark Mage", "color": "#d82b2b",
        "description": "A hooded caster of Reconquista. Wields dark magic and can charge a nova that hits the whole party.",
        "is_mage": True, "is_enemy": True,
        "skills": ["dark_bolt", "dark_nova"],
        "hp": 90, "max_hp": 90, "mp": 120, "max_mp": 120,
        "attack": 35, "defense": 12, "agility": 25, "accuracy": 85,
        "sprite": "images/enemies/mage.png",
        "icon": "images/enemies/mage.png",
        "cast_video": "video/cast/enemy_cast.webm",
        "lines": {
            "attack": ["Kneel.", "Foolish commoners."],
            "cast": ["Darkness, gather...", "You cannot stop this."],
            "hurt": ["Gah!", "Impossible..."],
            "defeat": ["Reconquista... will...", "This isn't over."],
        },
    },
    "bandit": {
        "name": "Bandit", "color": "#8b5a2b",
        "description": "A roadside brigand. Not clever, but quick with a blade.",
        "is_mage": False, "is_enemy": True,
        "skills": ["claw"],
        "hp": 80, "max_hp": 80, "mp": 0, "max_mp": 0,
        "attack": 28, "defense": 15, "agility": 22, "accuracy": 80,
        "sprite": "images/enemies/bandit.png",
        "icon": "images/enemies/bandit.png",
        "lines": {
            "attack": ["Yer coin or yer life!", "Ha!"],
            "hurt": ["Argh!"],
            "defeat": ["Blast..."],
        },
    },
    "golem": {
        "name": "Stone Golem", "color": "#5e5b51",
        "description": "An animated construct of stone. Slow, but immensely tough and heavy-hitting.",
        "is_mage": False, "is_enemy": True,
        "skills": ["smash"],
        "hp": 160, "max_hp": 160, "mp": 0, "max_mp": 0,
        "attack": 42, "defense": 40, "agility": 8, "accuracy": 70,
        "sprite": "images/enemies/golem.png",
        "icon": "images/enemies/golem.png",
        "lines": {
            "attack": ["...GRRR", "*crush*"],
            "hurt": ["*crack*"],
            "defeat": ["*crumbles*"],
        },
    },
}
