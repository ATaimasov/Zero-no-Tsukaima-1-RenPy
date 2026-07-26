label ch1_7:
    $ fade_fx("yard", new_music="t31")
    voice "ch1.7_o_001"
    o "So? What exactly happened here?"

    $ fade_fx("osman_cabinet", sprites=("o 1"))
    voice "ch1.7_o_002"
    o "Granted, it is only a detached building, but having one room completely wrecked is a serious matter indeed."

    $ show_sprites(("l 1 sad", "s 1 sad"), anim_out="slide_right")
    voice "ch1.7_s_001"
    s "..."

    voice "ch1.7_l_001"
    l "..."

    $ show_sprites(("si 1 sad", "s 1 sad"))
    voice "ch1.7_si_001"
    si "..."

    $ show_sprites(("si 1 sad", "k 1 sad"))
    k "..."

    $ show_sprites(("t 1", "k 1 sad"))
    t "..."

    $ show_sprites(("t 1", "m 1 sad"))
    voice ""
    m "..."

    $ show_sprites(("o 1 angry"), anim_out="slide_right")
    voice "ch1.7_o_003"
    o "I won't understand a thing if you just stay silent, you know."

    th "Even if you say that..."
    th "If I tell the truth, I’ll give Haruna away, so I can't really say anything..."

    voice "ch1.7_o_004"
    o "Judging by the state of the room... Yes, indeed... What exactly happened, Miss Vallière?"

    $ show_sprites(("l 1 sad", "s 1 sad"), anim_out="slide_right")
    voice "ch1.7_l_002"
    l "Yes! Um, well..."

    th "Hmm, as expected of the Headmaster."
    th "You've figured out at a glance that the magic that destroyed Siesta's room was Louise's, and you're trying to get an explanation or a confession from her!"

    voice "ch1.7_l_003"
    l "During a magic experiment, the magic accidentally went out of control and caused an explosion."

    $ show_sprites(("l 1 sad", "s 1 angry"))
    voice "ch1.7_s_002"
    s "Huh?{#e}"

    $ show_sprites(("l 1 angry", "s 1 angry"))
    voice "ch1.7_l_004"
    l "Saito!? Is something wrong?"

    $ show_sprites(("l 1 angry", "s 1 sad"))
    voice "ch1.7_s_003"
    s "No, it's nothing."

    th "Well, that's true. She can't really say, 'I let magic get out of control out of some inexplicable jealousy.'"

    $ show_sprites(("o 1"), anim_out="slide_right")
    voice "ch1.7_o_005"
    o "Hmm... an experiment, huh? And you all participated in it too?"

    $ show_sprites(("m 1"), anim_out="slide_right")
    voice "ch1.7_m_002"
    m "Y-yes."

    $ show_sprites(("k 1", "t 1"), anim_out="slide_right")
    voice "ch1.7_k_001"
    k "Oh, I was just an observer."

    voice "ch1.7_t_001"
    t "The same"

    $ show_sprites(("si 1 sad"), anim_out="slide_right")
    voice "ch1.7_si_002"
    si "Well, I..."

    $ show_sprites(("o 1"), anim_out="slide_right")
    voice "ch1.7_o_006"
    o "Ah... As for the fact that you provided this room, there is no need to trouble yourself with forced explanations."

    th "For some reason, I get the sense that the Headmaster knows it all and is feigning ignorance... Conveniently enough, though."

    voice "ch1.7_o_007"
    o "I am indeed quite curious as to what kind of experiment you were conducting..."

    voice "ch1.7_o_008"
    o "However, if it had been the main building, that would be one thing, but wrecking a commoner's private room is hardly commendable."

    $ show_sprites(("l 1 sad"), anim_out="slide_right")
    voice "ch1.7_l_005"
    l "I-I'm sorry."

    $ show_sprites(("o 1"), anim_out="slide_right")
    voice "ch1.7_o_009"
    o "Well, think nothing of it. If it was indeed a magical experiment, then it is, after all, a student's proper duty."

    ##! пару строк пропущено 

    menu:
        "Can't something be done, Headmaster?":
            "sss"

        "What about Kirche's room?":
            "sss"

        "You can come to my room.":
            "sss"


    #! дошел до нового дня и выбрал табиту, сработал  цундере ивент с луизой с кормежкой в столовке!!! Видимо зависит от симпатии персонажа,  у нее симпатия на максимуме была. 