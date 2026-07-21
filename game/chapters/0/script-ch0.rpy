label ch0:
    stop music fadeout 2.0
    call overlay_screen("town_square_night", "Tristania") from _call_overlay_screen
    play sound blow
    $ flash_clear("town_square_night")
    with explosion_shake
    pause(0.5)

    play music audio.t23 fadein 1.0
    
    show npc 1 angry as npc_left at close_center with dissolve

    #$ show_sprites(("npc 1 angry"))
    voice "ch0_npc1_001"
    npc1 "Where did the explosion happen?"

    #$ show_sprites(("npc 1 angry", "npc 1 angry"))

    show npc 1 angry as npc_left at close_left_npc

    show npc 1 angry as npc_right at close_right_npc with dissolve
    voice "ch0_npc1_002"
    npc2 "Sir—on the street facing the main avenue, multiple explosions involving explosive materials have been confirmed."

    voice "ch0_npc1_003"
    npc1 "Hurry up and dispatch the fire response team. Do not let the damage escalate."

    voice "ch0_npc1_004"
    npc2 "Yes, Sir!"

    #hide npc_left with dissolve
    #hide npc_right with dissolve
    #$ clear_chars(anim="dissolve")

    call overlay_screen(None,  "My name is Louise Françoise Le Blanc de La Vallière", text_mode="white", delay=5.5, sound_path="ch0_l_001") from _call_overlay_screen_1
    scene bg town_square_night at bg_center with dissolve

    show npc 1 as npc_left at close_left_npc with dissolve
    show npc 1 as npc_right at close_right_npc with dissolve

    voice "ch0_un_001"
    unknown "Hahahaha. You're always working hard."

    show npc 1 sad as npc_left at close_left_npc
    voice "ch0_npc1_005"
    npc1 "Where is he?"

    show npc 1 angry as npc_right at close_right_npc
    voice "ch0_npc1_006"
    npc2 "Sir, he's on top of that mansion."

    call overlay_screen(None, "The Pentagon that governs the five powers", text_mode="white", delay=3.5, sound_path="ch0_l_002") from _call_overlay_screen_2
    scene cg terrorist at bg_center with dissolve

    voice "ch0_un_002"
    unknown "Let's call it a day. Hurry up and put out the fire."

    voice "ch0_npc1_007"
    npc1 "You—what's your objective?"

    voice "ch0_un_003"
    unknown "Objective? To dismantle every rule this country stands on."

    voice "ch0_npc1_008"
    npc2 "Huh?"

    voice "ch0_un_004"
    unknown "Until then, you'll just have to cherish your mundane lives, won't you?"

    scene cg terrorist2 at bg_center with flash

    voice "ch0_npc1_009"
    npc2 "He... did he just vanish?"

    voice "ch0_npc1_010"
    npc1 "Hey! Apprehend him immediately!"

    voice "ch0_npc1_011"
    npc2 "Yes, Sir!"

    call overlay_screen(None, "Bestow blessings upon this one, and make them my familiar", delay=4.5, text_mode="white", sound_path="ch0_l_003") from _call_overlay_screen_3
    stop music fadeout 1.0
    pause(1)
    call intro from _call_intro_1

    jump ch1