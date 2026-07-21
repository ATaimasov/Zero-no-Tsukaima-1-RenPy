label ch1_6:
    $ fade_fx("si_room", new_music="t18", sprites=("h 1 sad", "s 1"))

    voice "ch1.6_s_001"
    s "H-hey, where did you come from? What's your name?"

    unk_h "Huh?!"

    voice "ch1.6_s_002"
    s "Are you from the same world as me? Are you Japanese too? Could you possibly be one of my classmates?"

    unk_h "Ah, um, wait a moment..."
    
    voice "ch1.6_k_001"
    unk_k "Honestly, Darling. Bombarding a woman with questions all at once is a total no-no."

    $ show_sprites(("h 1 sad", "s 1 sad"))
    voice "ch1.6_s_003"
    s "Eh?{#e?}"

    $ show_sprites(("k 1 happy", "s 1 sad"))
    voice "ch1.6_k_002"
    k "Be gentler. A man must elegantly lead a woman, you know."

    $ show_sprites(("k 1 happy", "s 3 sad"))
    voice "ch1.6_s_004"
    s "I-is that so? I'll be careful."

    $ show_sprites(("k 1 happy", "s 3 angry"))
    voice "ch1.6_s_005"
    s "Hold on a second! Hey, Kirche. What are you doing here?"

    voice "ch1.6_k_003"
    k "Oh, please, I'm not the only one, you know. See?"

    voice "ch1.6_s_006"
    s "Eh?"

    $ show_sprites(("t 1", "m 1"),  anim_in="slide_right", anim_out="slide_right")
    t "..."

    voice "ch1.6_m_001"
    m "Umm... Ah, right, right. Looks like she's doing well now."

    $ show_sprites(("l 3 angry", "s 3 sad"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.6_l_001"
    l "Why have so many people gathered here since this morning!"

    $ show_sprites(("k 1", "t 1"),  anim_in="slide_right", anim_out="slide_right")

    th "Kirche and Tabitha are Louise's classmates, having arrived as exchange students from Germania and Gallia, respectively."

    $ show_sprites(("k 1"), mode="big", anim_in="slide_right", anim_out="slide_right")
    th "Kirche excels in the fire element of magic. She is known as 'Kirche the Ardent'."
    th "She and Louise are simply on bad terms because of some ongoing friction over family lineage or place of origin."
    $ show_sprites(("t 1"), mode="big", anim_in="slide_left", anim_out="slide_left")
    th "Tabitha excels in the wind element of magic. She is known as 'Tabitha the Snowstorm'."
    th "Always taciturn and devoid of expression. What goes on in her mind is a mystery. Yet, she and Kirche are surprisingly close..."
    
    $ show_sprites(("k 1", "t 1"))
    th "Kirche being curious is one thing, but it's rare for Tabitha, who is always quietly reading a book, to actually show up."
    th "I wonder why they came here..."

    menu:
        "Ask Tabitha":
            $ show_sprites(("s 3 sad", "t 1"))
            voice "ch1.6_s_007-2"
            s "Hey, Tabitha. Why are you here?"

            voice "ch1.6_t_001"
            t "...I asked Montmorency, and Kirche brought me here."

            $ update_sympathy(-20, char_key="louise")
            $ update_sympathy(20, char_key="tabitha")

            voice "ch1.6_s_010"
            s "Thank you for the clear answer."

            voice "ch1.6_t_002"
            t "...But I do have an interest."

            voice "ch1.6_s_011"
            s "Oh, really?"

        "Ask Siesta":
            $ show_sprites(("si 1 sad", "s 3 sad"))
            voice "ch1.6_s_007-3"
            s "Hey, Siesta. Why are there so many people here?"

        "Ask Louise":
            $ show_sprites(("l 3 angry", "s 3 sad"))
            voice "ch1.6_s_007-4"
            s "Hey, Louise. Why are there so many people here?"

            voice "ch1.6_l_002"
            l "As if I'd know, considering I came here with you!"

            voice "ch1.6_s_008"
            s "Yeah, that's a perfectly valid point, but I thought that perhaps only Louise could share this feeling of having nowhere to turn."

            voice "ch1.6_l_003"
            l "Well, I suppose that's true. But I know what the cause is."

            $ update_sympathy(20, char_key="louise")

            voice "ch1.6_s_009"
            s "Eh?{#e?}"

            $ show_sprites(("l 3", "s 3 sad"))
            voice "ch1.6_l_004"
            l  "Tell me, Siesta. It wasn't this bustling before you came to fetch us, was it?"

        "Ask Kirche":
            $ show_sprites(("k 1", "s 3 sad"))
            voice "ch1.6_s_007"
            s "Hey, Kirche. Why are you here?"
            k "Oh, there's no particular reason, really"

            k "I heard you and Louise were doing something amusing, so I just dropped by to see for myself."
            s "Heard it...? From whom?"
            l "It goes without saying, doesn’t it? Say, Montmorency?"
            m "...Ohohoho."
            k "Come on. I may not know the circumstances, but it looks like you're having some fun, doesn't it?"
            l "There's nothing fun about it, really."
    $ show_sprites(("l 1"))
    voice "ch1.6_l_005"
    l "Well, fine. It's like talking to a brick wall. I don't think any of you are leaving."
    