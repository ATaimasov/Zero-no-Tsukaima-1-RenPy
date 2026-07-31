# Battle System (rewrite)

A clean, turn-based battle system for the Zero no Tsukaima Ren'Py game.
Drop these 4 files into your project and call `battle(...)` from any dialogue.

## Files

| File                 | Responsibility                                                                                                     |
| -------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `battle_data.rpy`    | **Single source of truth.** `characters` (allies AND enemies), `skills`, `items`, `inventory`.                     |
| `battle_logic.rpy`   | Pure state + math: setup, damage/heal/buff resolution, items, enemy AI. No UI.                                     |
| `battle_screens.rpy` | All UI: prep menu, HUD (enemy sprites + ally cards), skill/item/target bars, info panel, animation window, styles. |
| `battle_engine.rpy`  | Pacing: turn loop, barks, notices, animations, and the public `battle()` function.                                 |

## Usage

Call it exactly as requested, from a Ren'Py dialogue script:

```renpy
label some_event:
    "A pack of dark mages ambushes you!"

    $ battle(["saito", "louise"], ["mage", "mage"])
    # arg 1 = your party keys, arg 2 = enemy keys (both from `characters`)

    # battle() returns True on victory, False on defeat:
    $ won = battle(["saito", "louise", "tabitha"], ["golem", "bandit"])
    if won:
        "We won!"
    else:
        "We were overwhelmed..."
```

`battle()` first shows the **preparation menu** (Save / Begin Battle), then runs the fight, then returns the result.

## Design highlights (matches the requested behaviour)

- **One registry.** Everything about a combatant lives in `characters` in `battle_data.rpy`: description, skills, portrait, state portraits, mini `icon`, enemy `sprite`, `cast_video`, and battle `lines`. Enemies are just characters with `is_enemy: True`.
- **Party as cards, enemies as sprites.** Allies render as info cards (portrait + HP/MP bars) along the bottom; enemies render as sprites on the main field.
- **Actions:** `Attack` (opens the skill list), `Defend` (self only, skips the turn and raises DEF + small MP regen), `Item` (choose from `items`, then target any ally).
- **Targeting rules:**
  - Item -> any one of your allies.
  - Defend -> self only.
  - Single-target skill -> click one enemy (or one ally for heal/buff).
  - AoE skill (`target: "all_enemies"`) -> hits every foe, no target pick.
- **AoE charge time.** Skills with `cast_turns` 1-2 "charge" for that many of the caster's turns before firing (shown as a `CHARGE`/`CAST` badge). This applies to enemies too (e.g. `dark_nova`).
- **Animation window.** When an AoE fires it plays `cast_video` in a small window (not fullscreen): over the **caster's card** for allies, and on a **top-center stage** for enemies. If the video file is missing it degrades to an animated elemental burst with the skill name.
- **Miss / hit / defend feedback.** Center banner notice + rolling battle log on the left. Turn changes are announced too.
- **Barks.** Allies and enemies speak during attacks, casting, being hurt, defending, defeat and victory (from each character's `lines`).
- **Info panel.** Click any ally card or enemy sprite (when not currently choosing a target) to see full stats, description and skills.

## Adding content

- **New character / enemy:** add an entry to `characters`. Set `is_enemy` and `is_mage`, list `skills` keys, and point at art. Missing art is handled gracefully.
- **New skill:** add to `skills`. For an AoE, set `target: "all_enemies"` and (optionally) `cast_turns`. For support, use `kind: "heal"` or `kind: "buff"` with `target: "ally"`.
- **New item:** add to `items` and give the player some in `inventory`.

## Expected assets (optional)

All art is optional — anything missing falls back to a styled placeholder, so the battle never crashes.

- `images/battle/forest_bg.webp` — battle background (`BATTLE_BG` in `battle_data.rpy`).
- `images/enemies/<enemy>.webp` — enemy sprites.
- `gui/system/portraits/<x>.webp`, `..._happy.webp`, `..._hurt.webp` — ally card art + state variants.
- `video/cast/<name>_cast.webm` — AoE cast videos.

## Integration note

`battle_data.rpy` defines `default inventory`, `define skills`, `define items` and `define characters`.
If your existing scripts already define any of these names, **remove the old definitions** (or rename them) so there is only one source of truth. That is the whole point of the rewrite: no combatant data anywhere except `characters`.
