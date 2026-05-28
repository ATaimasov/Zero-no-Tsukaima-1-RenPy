label ch1_2:
    call overlay_screen("yard_night",  "Tristain Academy of Magic") from _call_overlay_screen_6
    pause(2)
    play music audio.t28 fadein 1.0
    scene cg ha_sick at bg_center with fade

    thoughts "In the end, Siesta kindly let us keep the girl we'd brought back hidden in her room."
    thoughts "Since calling a doctor was out of the question, we decided to have Montmorency examine her."

    show bg si_room_night at bg_center with fade
    pause(0.2)

    # !!! слайд из лева два перса и один на левую сторону а второй на правую
    show s 1 at normal_right with dissolve
    show m 1 at normal_left with dissolve

    voice "ch1.2_s_001"
    s "Hey, how'd it go? Is she hurt anywhere? Any signs of illness? Nothing... serious, right?"

    voice "ch1.2_m_001"
    m "Saito, calm down. I gave her a quick check-up, and there's nothing particularly wrong. I think she's just exhausted from built-up fatigue."

    
