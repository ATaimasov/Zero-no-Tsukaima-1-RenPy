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
define BATTLE_BG = "images/battle/forest_bg.webp"

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
        "name": "Slash", "consume": 30, "power": 35, "accuracy": 95,
        "element": "physical", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "slash",
        "description": "A quick sword strike on a single foe.",
    },
    "d_slash": {
        "name": "Double Slash", "consume": 50, "power": 60, "accuracy": 90,
        "element": "physical", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "double_slash",
        "description": "Two heavy strikes on a single foe.",
    },
    "wind_moon_slash": {
        "name": "Wind Moon Slash", "consume": 70, "power": 55, "accuracy": 85,
        "element": "wind", "target": "all_enemies", "kind": "damage",
        "cast_turns": 2, "anim": "wind_slash",
        "description": "Charged crescent of wind that hits ALL foes. Charges 2 turns.",
    },

    # --- Louise (void) ---
    "arrow": {
        "name": "Magic Arrow", "consume": 30, "power": 45, "accuracy": 90,
        "element": "void", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "magic_arrow",
        "description": "A bolt of void magic on a single foe.",
    },
    "heroism": {
        "name": "Heroism", "consume": 50, "power": 85, "accuracy": 85,
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
        "name": "Dispel", "consume": 30, "kind": "buff", "buff_stat": "accuracy",
        "buff_value": 20, "target": "ally", "cast_turns": 0, "anim": "buff",
        "description": "Raises one ally's accuracy.",
    },

    # --- Shared support ---
    "heal": {
        "name": "Heal", "consume": 30, "power": 70, "kind": "heal",
        "target": "ally", "cast_turns": 0, "anim": "heal",
        "description": "Restores HP to one ally.",
    },

    # --- Tabitha (wind) ---
    "wing": {
        "name": "Wing", "consume": 30, "power": 40, "accuracy": 92,
        "element": "wind", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "wind",
        "description": "A slicing gust on a single foe.",
    },
    "air_needle": {
        "name": "Air Needle", "consume": 50, "power": 58, "accuracy": 88,
        "element": "wind", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "air_needle",
        "description": "Needles of wind pierce a single foe.",
    },
    "wind_break": {
        "name": "Wind Break", "consume": 70, "power": 50, "accuracy": 82,
        "element": "wind", "target": "all_enemies", "kind": "damage",
        "cast_turns": 2, "anim": "wind_storm",
        "description": "A hurricane strikes ALL foes. Charges 2 turns.",
    },
    "air_force": {
        "name": "Air Force", "consume": 30, "kind": "buff", "buff_stat": "accuracy",
        "buff_value": 20, "target": "ally", "cast_turns": 0, "anim": "buff",
        "description": "Raises one ally's speed.",
    },

    # --- Kirche (fire) ---
    "fire": {
        "name": "Fire", "consume": 30, "power": 42, "accuracy": 88,
        "element": "fire", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "fire",
        "description": "A burst of flame on a single foe.",
    },
    "fire_needle": {
        "name": "Fire Needle", "consume": 50, "power": 60, "accuracy": 85,
        "element": "fire", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "fire_needle",
        "description": "Lances of fire pierce a single foe.",
    },
    "fire_arrow": {
        "name": "Fire Storm", "consume": 70, "power": 52, "accuracy": 80,
        "element": "fire", "target": "all_enemies", "kind": "damage",
        "cast_turns": 1, "anim": "fire_storm",
        "description": "A storm of fire engulfs ALL foes. Charges 1 turn.",
    },
    "fire_shield": {
        "name": "Fire Shield", "consume": 30, "kind": "buff", "buff_stat": "accuracy",
        "buff_value": 20, "target": "ally", "cast_turns": 0, "anim": "buff",
        "description": "Raises one ally's defence.",
    },


    # --- Henrietta (water) ---
    "water": {
        "name": "Water", "consume": 30, "power": 40, "accuracy": 90,
        "element": "water", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "water",
        "description": "A jet of water on a single foe.",
    },
    "water_needle": {
        "name": "Water Needle", "consume": 50, "power": 60, "accuracy": 85,
        "element": "water", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "fire_needle",
        "description": "Lances of water pierce a single foe.",
    },
    "water_hazard": {
        "name": "Water Hazard", "consume": 70, "power": 50, "accuracy": 83,
        "element": "water", "target": "all_enemies", "kind": "damage",
        "cast_turns": 2, "anim": "water_storm",
        "description": "A flood crashes over ALL foes. Charges 2 turns.",
    },
    "water_blade": {
        "name": "Water Blade", "consume": 30, "kind": "buff", "buff_stat": "accuracy",
        "buff_value": 20, "target": "ally", "cast_turns": 0, "anim": "buff",
        "description": "Raises one ally's attack power.",
    },

    # --- Enemy skills ---
    "claw": {
        "name": "Claw", "consume": 30, "power": 30, "accuracy": 85,
        "element": "physical", "target": "enemy", "kind": "damage",
        "cast_turns": 0, "anim": "slash",
        "description": "A savage swipe.",
    },
    "dark_bolt": {
        "name": "Dark Bolt", "consume": 50, "power": 44, "accuracy": 85,
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
}

# Inventory carried into battle (persists across battles).
default inventory = {
    "Bread": 3,
    "Herb": 3,
    "Elixir": 3,
}