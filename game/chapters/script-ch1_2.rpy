label ch1_2:
    call overlay_screen("yard_night",  "Tristain Academy of Magic") from _call_overlay_screen_6
    pause(2)
    $ fade_clear("cg ha_sick", new_music="t28")

    thoughts "In the end, Siesta kindly let us keep the girl we'd brought back hidden in her room."
    thoughts "Since calling a doctor was out of the question, we decided to have Montmorency examine her."

    $ fade_clear("bg si_room_night")
    pause(0.2)

    $ show_sprites(("m 1", "s 1"))

    voice "ch1.2_s_001"
    s "Hey, how'd it go? Is she hurt anywhere? Any signs of illness? Nothing... serious, right?"

    voice "ch1.2_m_001"
    m "Saito, calm down. I gave her a quick check-up, and there's nothing particularly wrong. I think she's just exhausted from built-up fatigue."

    voice "ch1.2_m_002"
    m "Wouldn't it be fine to just let her sleep like this?"

    voice "ch1.2_s_002"
    s "I see... That's a relief. Thanks, Monmon."

    $ show_sprites(("m 1 angry", "s 1"))
    voice "ch1.2_m_003"
    m "My name is Montmorency! I've told you not to make up weird nicknames for me!"

    $ show_sprites(("m 1"), mode="big")

    thoughts "Montmorency is Louise's classmate. She specializes in water magic. Her nickname is \"Montmorency the Fragrance.\""
    thoughts "I call her Monmon, but she doesn't seem too fond of the nickname"

    $ show_sprites(("m 1", "s 1 sad"))

    voice "ch1.2_s_003"
    s "Ah, yeah. But seriously, thanks."

    voice "ch1.2_m_004"
    m "You're welcome. It's not like I'm under any obligation to do this, but I simply can't abandon someone who's sick."

    $ show_sprites(("l 1", "s 1 sad"))
    voice "ch1.2_l_001"
    l "Anyway, Siesta. I apologize for dragging a sick person into the room without warning."

    $ show_sprites(("l 1", "si 1"))

    #! реплика сиесты
    si "Oh, it's quite alright. Please don't worry about it, Miss Vallière. After all, it's for the sake of helping someone in need."

    $ show_sprites(("si 1"), mode="big")
    
    thoughts "Siesta is a maid working at this academy. She feels a sense of kinship with me since we're both commoners."
    thoughts "She's kind, great at cooking... I wish my master would take a page out of her book."

    $ show_sprites(("l 1", "si 1"))
    $ show_sprites(("l 1", "si 4 shy"))

    #! реплика сиесты
    si "Besides... it's what Saito asked for."

    $ show_sprites(("l 1 angry", "si 4 shy"))
    voice "ch1.2_l_002"
    l "...I see."

    $ show_sprites(("l 1 angry", "m 1 sad"))
    voice "ch1.2_m_005"
    m "But this girl... I don't recognize her from the academy. Just where on earth did you pick up this commoner?"

    $ show_sprites(("l 1", "m 1 sad"))
    voice "ch1.2_l_003"
    l "Eh?"
    
    $ show_sprites(("l 1", "m 1 angry"))
    voice "ch1.2_m_006"
    m "Don't just 'eh' at me. I'll have you know I remember the faces of almost all the commoners working at the academy."
    voice "ch1.2_m_007"
    m "Listen... Saito. Where exactly did you bring this girl from?"

    $ show_sprites(("s 1 sad", "m 1 angry"))
    voice "ch1.2_s_004"
    s "Uh, um..."

    $ result = None
    menu:
        "Blame it on Louise":
            $ result = "good"
        "Try to cover it up yourself":
            $ result = "neutral"
        "Blame it on Siesta":
            $ result = "bad"


