label ch0:
    stop music fadeout 2.0
    call overlay_screen("town_square_night", "Tristania") from _call_overlay_screen
    $ blow_fx(new_music="t23", music_fadein=2)
    #$ scene_fx(effect="blow", duration=1, sound="blow", new_music="t23", music_fadein=2)
    pause(0.5)

    $ show_sprites(("npc 1 angry"), anim="dissolve")
    voice "ch0_npc1_001"
    npc1 "Where did the explosion happen?"

    $ show_sprites(("npc 1 angry", "npc 1 angry"))

    voice "ch0_npc1_002"
    npc2 "Sir—on the street facing the main avenue, multiple explosions involving explosive materials have been confirmed."

    voice "ch0_npc1_003"
    npc1 "Hurry up and dispatch the fire response team. Do not let the damage escalate."

    voice "ch0_npc1_004"
    npc2 "Yes, Sir!"

    call overlay_screen(None,  "My name is Louise Françoise Le Blanc de La Vallière", text_mode="white", delay=5.5, sound_path="ch0_l_001") from _call_overlay_screen_1
    $ dissolve_fx("town_square_night")
    $ show_sprites(("npc 1", "npc 1"), anim="dissolve")

    voice "ch0_un_001"
    unk "Hahahaha. You're always working hard."

    $ show_sprites(("npc 1 sad", "npc 1"), raise_z=False)

    voice "ch0_npc1_005"
    npc1 "Where is he?"

    $ show_sprites(("npc 1 sad", "npc 1 angry "))
    voice "ch0_npc1_006"
    npc2 "Sir, he's on top of that mansion."

    call overlay_screen(None, "The Pentagon that governs the five powers", text_mode="white", delay=3.5, sound_path="ch0_l_002") from _call_overlay_screen_2
    $ dissolve_fx("terrorist")

    voice "ch0_un_002"
    unk "Let's call it a day. Hurry up and put out the fire."

    voice "ch0_npc1_007"
    npc1 "You—what's your objective?"

    voice "ch0_un_003"
    unk "Objective? To dismantle every rule this country stands on."

    voice "ch0_npc1_008"
    npc2 "Huh?"

    voice "ch0_un_004"
    unk "Until then, you'll just have to cherish your mundane lives, won't you?"

    $ flash_fx("terrorist2")

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