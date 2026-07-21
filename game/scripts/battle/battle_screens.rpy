# ============================================================================
# ZERO NO TSUKAIMA - BATTLE SYSTEM  (rewrite)
# FILE 3/4: SCREENS + STYLES
# ----------------------------------------------------------------------------
# All UI. The engine only sets state variables and shows / calls these screens.
#
#   battle_prep   -> pre-battle menu (Save / Start)
#   battle_hud    -> the whole battlefield. Shown persistently for display, and
#                    call'd when we need the player's action for one ally.
#                    Returns an action tuple: (kind, key, target_uid)
#                       ("skill",  skill_key, uid_or_None)
#                       ("defend", None,      None)
#                       ("item",   item_name, uid)
#
# Robustness: every image/video is guarded with renpy.loadable(); missing art
# degrades to a styled placeholder instead of crashing the battle.
# ============================================================================

# ----------------------------------------------------------------------------
# COLOR / SIZE TOKENS  (kept in one place so the whole HUD stays consistent)
# ----------------------------------------------------------------------------
define B_BG        = "#12121b"
define B_PANEL     = "#1c1c2aE6"
define B_PANEL2    = "#262636E6"
define B_LINE      = "#3a3a4f"
define B_ACCENT    = "#e0a03c"        # amber / gold
define B_ACCENT_D  = "#3a2f1c"
define B_TEXT      = "#f2ede3"
define B_MUTED     = "#9a94a6"
define B_HP        = "#4caf72"
define B_HP_LOW    = "#d0524a"
define B_MP        = "#4a90d9"
define B_ENEMY     = "#d0524a"
define B_SELECT    = "#f0c65c"

# ----------------------------------------------------------------------------
# small helpers used only by screens
# ----------------------------------------------------------------------------
init python:
    def _img_or_none(path):
        return path if (path and renpy.loadable(path)) else None

    def _hp_frac(u):
        m = max(1, u.get("max_hp", 1))
        return max(0.0, min(1.0, u.get("hp", 0) / float(m)))

    def _mp_frac(u):
        m = max(1, u.get("max_mp", 1))
        return max(0.0, min(1.0, u.get("mp", 0) / float(m)))


# ============================================================================
# PRE-BATTLE MENU
# ============================================================================
screen battle_prep(ally_keys, enemy_keys):
    modal True
    tag battle_prep
    add B_BG

    # faint battlefield preview behind the panel
    if _img_or_none(BATTLE_BG):
        add BATTLE_BG:
            fit "cover"
            xysize (config.screen_width, config.screen_height)
            alpha 0.35

    frame:
        style_prefix "prep"
        xalign 0.5
        yalign 0.5
        xsize 900
        padding (40, 36)
        background Frame(Solid(B_PANEL), 24, 24)

        vbox:
            spacing 22

            text "Battle Preparation" size 40 color B_ACCENT xalign 0.5

            text "A hostile force blocks your path. Ready yourselves." size 20 color B_MUTED xalign 0.5

            # side-by-side rosters
            hbox:
                xalign 0.5
                spacing 40

                # allies
                vbox:
                    spacing 10
                    xsize 380
                    text "Your Party" size 22 color B_TEXT xalign 0.5
                    for k in ally_keys:
                        $ c = characters.get(k, {})
                        frame:
                            background Frame(Solid(B_PANEL2), 14, 14)
                            padding (12, 10)
                            xfill True
                            hbox:
                                spacing 12
                                $ ic = _img_or_none(c.get("icon") or c.get("portrait"))
                                if ic:
                                    add ic:
                                        fit "cover"
                                        xysize (54, 54)
                                else:
                                    frame:
                                        background Solid(B_ACCENT_D)
                                        xysize (54, 54)
                                vbox:
                                    yalign 0.5
                                    text c.get("name", k) size 20 color B_TEXT
                                    text ("Magic" if c.get("is_mage") else "Attack") size 15 color B_MUTED

                # enemies
                vbox:
                    spacing 10
                    xsize 380
                    text "Enemies" size 22 color B_ENEMY xalign 0.5
                    for k in enemy_keys:
                        $ c = characters.get(k, {})
                        frame:
                            background Frame(Solid(B_PANEL2), 14, 14)
                            padding (12, 10)
                            xfill True
                            hbox:
                                spacing 12
                                $ ic = _img_or_none(c.get("icon") or c.get("sprite"))
                                if ic:
                                    add ic:
                                        fit "cover"
                                        xysize (54, 54)
                                else:
                                    frame:
                                        background Solid("#402020")
                                        xysize (54, 54)
                                vbox:
                                    yalign 0.5
                                    text c.get("name", k) size 20 color B_TEXT
                                    text ("Magic" if c.get("is_mage") else "Attack") size 15 color B_MUTED

            null height 4

            hbox:
                xalign 0.5
                spacing 20
                textbutton "Save Game":
                    style "prep_button"
                    action ShowMenu("save")
                textbutton "Begin Battle":
                    style "prep_button_primary"
                    action Return("start")

style prep_button is button:
    background Frame(Solid(B_PANEL2), 12, 12)
    hover_background Frame(Solid(B_LINE), 12, 12)
    padding (28, 16)
style prep_button_text is button_text:
    size 22
    color B_TEXT
    hover_color "#ffffff"

style prep_button_primary is button:
    background Frame(Solid(B_ACCENT), 12, 12)
    hover_background Frame(Solid(B_SELECT), 12, 12)
    padding (34, 16)
style prep_button_primary_text is button_text:
    size 22
    color "#1a1408"
    hover_color "#000000"


# ============================================================================
# MAIN BATTLE HUD
# ============================================================================
screen battle_hud(awaiting=False, cur_uid=None):
    tag battle_hud
    zorder 0

    # ---- UI interaction state (screen-local; resets each call) ----
    default mode = "root"          # root | skill | item | target_enemy | target_ally
    default sel_skill = None
    default sel_item = None

    $ cur = unit_by_uid(cur_uid) if cur_uid else None

    # ---------------- background ----------------
    add B_BG
    if _img_or_none(BATTLE_BG):
        add BATTLE_BG:
            fit "cover"
            xysize (config.screen_width, config.screen_height)

    # dark vignette so HUD text stays readable
    add Solid("#00000055")

    # ============================================================
    # TOP: enemy sprites + optional enemy AoE animation stage
    # ============================================================
    fixed:
        xfill True
        ypos 20
        yanchor 0.0
        ysize 360

        # enemy row
        hbox:
            xalign 0.5
            yalign 1.0
            spacing 60
            for foe in store.foes:
                use enemy_sprite(foe, awaiting, mode, sel_skill)

        # enemy AoE animation window (top-center, over the field)
        if store.anim_state and store.anim_state.get("where") == "stage":
            fixed:
                xalign 0.5
                yalign 0.0
                use anim_window(store.anim_state)

    # ============================================================
    # CENTER: floating notice (turn change, big events)
    # ============================================================
    if store.battle_notice:
        frame:
            xalign 0.5
            ypos 300
            background Frame(Solid("#000000cc"), 16, 16)
            padding (30, 16)
            at notice_pulse
            text store.battle_notice:
                size 30
                color B_ACCENT
                xalign 0.5

    # ============================================================
    # LEFT: rolling battle log
    # ============================================================
    frame:
        xpos 18
        ypos 96
        xsize 300
        background Frame(Solid(B_PANEL), 12, 12)
        padding (14, 12)
        vbox:
            spacing 4
            text "Battle Log" size 15 color B_ACCENT
            for line in store.battle_log[-6:]:
                text line size 15 color B_TEXT

    # ============================================================
    # BOTTOM: ally cards
    # ============================================================
    hbox:
        xalign 0.5
        yalign 1.0
        yoffset -170
        spacing 18
        for ally in store.party:
            use ally_card(ally, awaiting, cur_uid, mode, sel_skill, sel_item)

    # ============================================================
    # BOTTOM BAR: action menu (only for the acting ally)
    # ============================================================
    if awaiting and cur:
        frame:
            xalign 0.5
            yalign 1.0
            xsize config.screen_width
            ysize 150
            background Frame(Solid(B_PANEL), 0, 0)

            # who is acting
            vbox:
                xpos 30
                yalign 0.5
                spacing 2
                text "Now acting" size 15 color B_MUTED
                text cur.get("name", "?") size 26 color B_ACCENT
                text ("MP %d/%d" % (cur.get("mp", 0), cur.get("max_mp", 0))) size 16 color B_MP

            # -------- ROOT menu --------
            if mode == "root":
                hbox:
                    xalign 0.98
                    yalign 0.5
                    spacing 14
                    textbutton (attack_type_label(cur)):
                        style "act_button"
                        action SetScreenVariable("mode", "skill")
                    textbutton "Defend":
                        style "act_button"
                        action Return(("defend", None, None))
                    textbutton "Item":
                        style "act_button"
                        action SetScreenVariable("mode", "item")

            # -------- SKILL list --------
            elif mode == "skill":
                use skill_bar(cur, sel_skill)

            # -------- ITEM list --------
            elif mode == "item":
                use item_bar()

            # -------- TARGETING prompts --------
            elif mode == "target_enemy":
                hbox:
                    xalign 0.98
                    yalign 0.5
                    spacing 14
                    text "Select an enemy target" size 22 color B_SELECT yalign 0.5
                    textbutton "Cancel" style "act_button_small" action [SetScreenVariable("mode", "skill"), SetScreenVariable("sel_skill", None)]
            elif mode == "target_ally":
                hbox:
                    xalign 0.98
                    yalign 0.5
                    spacing 14
                    text "Select an ally" size 22 color B_SELECT yalign 0.5
                    textbutton "Cancel":
                        style "act_button_small"
                        action [SetScreenVariable("mode", "root"), SetScreenVariable("sel_skill", None), SetScreenVariable("sel_item", None)]

    # ============================================================
    # INFO PANEL (toggled by clicking a card; never ends the turn)
    # ============================================================
    if store.show_info_uid:
        use info_panel(store.show_info_uid)


# ----------------------------------------------------------------------------
# ENEMY SPRITE (also acts as a target button while targeting enemies)
# ----------------------------------------------------------------------------
screen enemy_sprite(foe, awaiting, mode, sel_skill):
    $ dead = foe.get("hp", 0) <= 0
    $ spr = _img_or_none(foe.get("sprite") or foe.get("icon"))
    $ is_targetable = awaiting and mode == "target_enemy" and not dead
    $ is_active = (store.active_uid == foe.get("uid"))

    button:
        style "sprite_button"
        # clicking selects target while targeting, otherwise opens info
        if is_targetable:
            action Return(("skill", sel_skill, foe.get("uid")))
        else:
            action SetVariable("show_info_uid", foe.get("uid"))

        vbox:
            spacing 4
            xsize 180

            # ally AoE animation can land on this sprite's slot? No - enemies use
            # the top stage. Here we just draw the sprite + hurt/cast tint.
            fixed:
                xysize (180, 220)
                if spr:
                    add spr:
                        fit "contain"
                        xysize (180, 220)
                        xalign 0.5
                        # visual feedback
                        if dead:
                            matrixcolor SaturationMatrix(0.0)
                            alpha 0.35
                        elif foe.get("state") == "hurt":
                            matrixcolor TintMatrix("#ff6a6a")
                else:
                    frame:
                        background Solid("#3a1f1f")
                        xysize (180, 220)
                        text foe.get("name", "?"):
                            xalign 0.5
                            yalign 0.5
                            color B_TEXT
                            size 20

                # selection ring while targeting
                if is_targetable:
                    add Solid(B_SELECT):
                        xysize (180, 220)
                        alpha 0.22
                        at target_ring

                # casting badge
                if foe.get("casting"):
                    frame:
                        background Frame(Solid("#000000cc"), 8, 8)
                        xalign 0.5
                        yalign 0.0
                        padding (8, 4)
                        text ("CHARGING (%d)" % foe["casting"].get("turns_left", 0)):
                            size 14
                            color B_SELECT

            # name + hp bar
            vbox:
                xsize 180
                spacing 2
                text foe.get("name", "?"):
                    size 17
                    color (B_MUTED if dead else B_TEXT)
                    xalign 0.5
                if not dead:
                    use mini_bar(_hp_frac(foe), B_HP if _hp_frac(foe) > 0.3 else B_HP_LOW, 180, 8)


# ----------------------------------------------------------------------------
# ALLY CARD (also a target button while targeting allies)
# ----------------------------------------------------------------------------
screen ally_card(ally, awaiting, cur_uid, mode, sel_skill, sel_item):
    $ uid = ally.get("uid")
    $ dead = ally.get("hp", 0) <= 0
    $ is_active = (uid == cur_uid) and awaiting
    $ ally_targetable = awaiting and mode == "target_ally"

    # If an ally AoE animation is playing on THIS card, replace the card art.
    $ anim_here = store.anim_state and store.anim_state.get("where") == ("card:" + str(uid))

    button:
        style "card_button"
        if ally_targetable:
            sensitive (not dead)
         
        if ally_targetable and not dead:
            # figure out whether we're placing a skill or an item
            if sel_item:
                action Return(("item", sel_item, uid))
            else:
                action Return(("skill", sel_skill, uid))
        else:
            action SetVariable("show_info_uid", uid)

        frame:
            xsize 190
            ysize 250
            padding (0, 0)
            if is_active:
                background Frame(Solid(B_ACCENT_D), 16, 16)
            else:
                background Frame(Solid(B_PANEL2), 16, 16)

            vbox:
                # ---- portrait / animation region ----
                fixed:
                    xysize (190, 150)
                    if anim_here:
                        fixed:
                            xalign 0.5
                            yalign 0.5
                            use anim_window(store.anim_state)
                    else:
                        $ state = ally.get("state", "normal")
                        $ port = ally.get("portrait_" + state) or ally.get("portrait")
                        $ port = _img_or_none(port) or _img_or_none(ally.get("portrait"))
                    if port:
                        add port:
                            fit "cover"
                            xysize (190, 150)
                            if dead:
                                matrixcolor SaturationMatrix(0.0)
                                alpha 0.4
                    else:
                        frame:
                            background Solid(B_ACCENT_D)
                            xysize (190, 150)
                            text ally.get("name", "?"):
                                xalign 0.5
                                yalign 0.5
                                color B_TEXT

                    # status tag
                    if dead:
                        frame:
                            background Solid("#000000aa")
                            xysize (190, 150)
                            text "DOWN" xalign 0.5 yalign 0.5 color B_HP_LOW size 26
                    elif ally.get("defending"):
                        frame:
                            background Frame(Solid("#000000aa"), 6, 6)
                            xalign 1.0
                            yalign 0.0
                            padding (6, 3)
                            text "GUARD" size 13 color B_MP
                    elif ally.get("casting"):
                        frame:
                            background Frame(Solid("#000000aa"), 6, 6)
                            xalign 1.0
                            yalign 0.0
                            padding (6, 3)
                            text ("CAST %d" % ally["casting"].get("turns_left", 0)) size 13 color B_SELECT

                # ---- name + bars ----
                frame:
                    xfill True
                    padding (12, 8)
                    background None
                    vbox:
                        spacing 4
                        text ally.get("name", "?") size 19 color B_TEXT
                        # HP
                        hbox:
                            spacing 6
                            text "HP" size 13 color B_MUTED yalign 0.5
                            use mini_bar(_hp_frac(ally), B_HP if _hp_frac(ally) > 0.3 else B_HP_LOW, 110, 10)
                            text ("%d" % ally.get("hp", 0)) size 13 color B_TEXT yalign 0.5
                        # MP
                        hbox:
                            spacing 6
                            text "MP" size 13 color B_MUTED yalign 0.5
                            use mini_bar(_mp_frac(ally), B_MP, 110, 10)
                            text ("%d" % ally.get("mp", 0)) size 13 color B_TEXT yalign 0.5


# ----------------------------------------------------------------------------
# SKILL SELECTION BAR
# ----------------------------------------------------------------------------
screen skill_bar(cur, sel_skill):
    viewport:
        xalign 0.98
        yalign 0.5
        xsize 900
        ysize 130
        scrollbars "horizontal"
        mousewheel True
        draggable True

        hbox:
            spacing 10
            for sk_key in cur.get("skills", []):
                $ sk = skills.get(sk_key, {})
                $ afford = can_afford(cur, sk_key)
                button:
                    style "skill_button"
                    sensitive afford
                    # set skill, then decide targeting
                    if sk.get("target") == "all_enemies":
                        action Return(("skill", sk_key, None))
                    elif sk.get("target") == "ally":
                        action [SetScreenVariable("sel_skill", sk_key), SetScreenVariable("mode", "target_ally")]
                    else:
                        action [SetScreenVariable("sel_skill", sk_key), SetScreenVariable("mode", "target_enemy")]

                    vbox:
                        xsize 200
                        spacing 2
                        hbox:
                            spacing 6
                            text sk.get("name", sk_key) size 18 color (B_TEXT if afford else B_MUTED)
                            if sk.get("target") == "all_enemies":
                                text "AoE" size 13 color B_ENEMY yalign 0.5
                        text sk.get("description", "") size 13 color B_MUTED
                        hbox:
                            spacing 10
                            text ("MP %d" % sk.get("consume", 0)) size 14 color (B_MP if afford else B_HP_LOW)
                            if sk.get("cast_turns", 0) > 0:
                                text ("Charge %d" % sk.get("cast_turns")) size 14 color B_SELECT

            textbutton "Back":
                style "act_button_small"
                yalign 0.5
                action SetScreenVariable("mode", "root")


# ----------------------------------------------------------------------------
# ITEM SELECTION BAR
# ----------------------------------------------------------------------------
screen item_bar():
    viewport:
        xalign 0.98
        yalign 0.5
        xsize 900
        ysize 130
        scrollbars "horizontal"
        mousewheel True
        draggable True

        hbox:
            spacing 10
            $ any_item = False
            for item_name, count in store.inventory.items():
                if count > 0:
                    $ any_item = True
                    $ it = items.get(item_name, {})
                    button:
                        style "skill_button"
                        action [SetScreenVariable("sel_item", item_name), SetScreenVariable("mode", "target_ally")]
                        vbox:
                            xsize 200
                            spacing 2
                            hbox:
                                spacing 6
                                text it.get("name", item_name) size 18 color B_TEXT
                                text ("x%d" % count) size 15 color B_ACCENT yalign 0.5
                            text it.get("description", "") size 13 color B_MUTED

            if not any_item:
                text "No items left." size 20 color B_MUTED yalign 0.5 xpos 10

            textbutton "Back":
                style "act_button_small"
                yalign 0.5
                action SetScreenVariable("mode", "root")


# ----------------------------------------------------------------------------
# INFO PANEL  (modal-ish overlay; closing it does NOT end the turn)
# ----------------------------------------------------------------------------
screen info_panel(uid):
    $ u = unit_by_uid(uid)
    zorder 50
    # click-off to close
    button:
        style "empty_button"
        xfill True
        yfill True
        action SetVariable("show_info_uid", None)

    if u:
        frame:
            xalign 0.5
            yalign 0.5
            xsize 640
            background Frame(Solid("#14141f"), 24, 24)
            padding (28, 24)
            vbox:
                spacing 16
                hbox:
                    spacing 18
                    # art
                    $ art = _img_or_none(u.get("portrait")) or _img_or_none(u.get("sprite")) or _img_or_none(u.get("icon"))
                    if art:
                        add art:
                            fit "cover"
                            xysize (140, 160)
                    else:
                        frame:
                            background Solid(B_ACCENT_D)
                            xysize (140, 160)
                    vbox:
                        yalign 0.5
                        spacing 4
                        text u.get("name", "?") size 32 color B_ACCENT
                        text (("Enemy - " if u.get("is_enemy") else "") + ("Magic type" if u.get("is_mage") else "Attack type")):
                            size 17 color B_MUTED
                        null height 6
                        # stat grid
                        hbox:
                            spacing 24
                            vbox:
                                text ("HP  %d / %d" % (u.get("hp", 0), u.get("max_hp", 0))) size 16 color B_TEXT
                                text ("MP  %d / %d" % (u.get("mp", 0), u.get("max_mp", 0))) size 16 color B_TEXT
                                text ("ATK %d" % u.get("attack", 0)) size 16 color B_TEXT
                            vbox:
                                text ("DEF %d" % u.get("defense", 0)) size 16 color B_TEXT
                                text ("AGI %d" % u.get("agility", 0)) size 16 color B_TEXT
                                text ("ACC %d" % u.get("accuracy", 0)) size 16 color B_TEXT

                text u.get("description", "") size 17 color B_TEXT

                # skill list
                text "Skills" size 20 color B_ACCENT
                vbox:
                    spacing 4
                    for sk_key in u.get("skills", []):
                        $ sk = skills.get(sk_key, {})
                        hbox:
                            spacing 10
                            text ("- " + sk.get("name", sk_key)) size 16 color B_TEXT
                            text ("(MP %d)" % sk.get("consume", 0)) size 14 color B_MP yalign 0.5
                            if sk.get("target") == "all_enemies":
                                text "AoE" size 13 color B_ENEMY yalign 0.5

                textbutton "Close":
                    style "act_button_small"
                    xalign 1.0
                    action SetVariable("show_info_uid", None)


# ----------------------------------------------------------------------------
# ANIMATION WINDOW  (video if available, else animated label)
# ----------------------------------------------------------------------------
screen anim_window(state):
    $ vid = _img_or_none(state.get("video"))
    frame:
        background Frame(Solid("#000000e0"), 12, 12)
        xsize 260
        ysize 175
        padding (6, 6)
        at anim_pop
        fixed:
            xfill True
            yfill True
            if vid:
                add Movie(play=state.get("video")):
                    fit "contain"
                    xysize (248, 140)
                    xalign 0.5
                    yalign 0.0
            else:
                # graceful fallback: colored burst + label
                frame:
                    background Solid(state.get("color", B_ACCENT))
                    xysize (248, 140)
                    xalign 0.5
                    yalign 0.0
                    at anim_flash
                    text state.get("label", "SKILL"):
                        xalign 0.5
                        yalign 0.5
                        size 26
                        color "#1a1408"
            text state.get("caster", ""):
                xalign 0.5
                yalign 1.0
                size 15
                color B_SELECT


# ----------------------------------------------------------------------------
# small reusable HP/MP bar
# ----------------------------------------------------------------------------
screen mini_bar(frac, color, width, height):
    fixed:
        xsize width
        ysize height
        yalign 0.5
        add Frame(Solid("#00000066"), 2, 2):
            xsize width
            ysize height
        bar:
            value frac
            range 1.0
            xsize width
            ysize height
            left_bar Frame(Solid(color), 2, 2)
            right_bar Frame(Solid("#00000000"), 2, 2)
            thumb None
            thumb_shadow None


# ----------------------------------------------------------------------------
# TRANSFORMS
# ----------------------------------------------------------------------------
transform notice_pulse:
    alpha 0.0 zoom 0.9
    easein 0.15 alpha 1.0 zoom 1.0
    pause 0.6
    easeout 0.2 alpha 0.85

transform anim_pop:
    alpha 0.0 zoom 0.8
    easein 0.2 alpha 1.0 zoom 1.0

transform anim_flash:
    alpha 0.6
    block:
        easein 0.25 alpha 1.0
        easeout 0.25 alpha 0.6
        repeat

transform target_ring:
    linear 0.5 alpha 0.12
    linear 0.5 alpha 0.34
    repeat


# ----------------------------------------------------------------------------
# STYLES
# ----------------------------------------------------------------------------
style act_button is button:
    background Frame(Solid(B_PANEL2), 12, 12)
    hover_background Frame(Solid(B_ACCENT), 12, 12)
    padding (26, 16)
style act_button_text is button_text:
    size 22
    color B_TEXT
    hover_color "#1a1408"

style act_button_small is button:
    background Frame(Solid(B_PANEL2), 10, 10)
    hover_background Frame(Solid(B_LINE), 10, 10)
    padding (16, 10)
style act_button_small_text is button_text:
    size 17
    color B_TEXT
    hover_color "#ffffff"

style skill_button is button:
    background Frame(Solid(B_PANEL2), 10, 10)
    hover_background Frame(Solid(B_ACCENT_D), 10, 10)
    insensitive_background Frame(Solid("#1a1a2266"), 10, 10)
    padding (14, 10)

style sprite_button is button:
    background None
    hover_background None

style card_button is button:
    background None
    hover_background None

style empty_button is button:
    background None
    hover_background None
