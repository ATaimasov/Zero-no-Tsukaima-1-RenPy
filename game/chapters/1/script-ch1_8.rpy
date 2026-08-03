# встреча с Гишем
label ch1_8:
    $ fade_fx("hallway_down_night", new_music="t18", sprites=("g 1"))

    voice "ch1.8_g_001"
    g "Oh? I hear the four of you have been summoned by the Headmaster. What on earth happened?"

    $ show_sprites(("g 1"), mode="big")
    th "Guishe is Louise's classmate. He specializes in Earth system magic. He knows as 'Guishe the Bronze'."
    th "He's a womanizer and a show-off, but you just can't hate the guy."

    $ show_sprites(("l 1", "g 1"))
    voice "ch1.8_l_001"
    l "Listen... There was an unfortunate accident."

    $ show_sprites(("k 1", "g 1"))
    voice "ch1.8_k_001"
    k "Oh, right. Louise just accidentally destroyed a commoner's room with her magic."
    
    $ show_sprites(("k 1", "g 1 happy"))
    voice "ch1.8_g_002"
    g "Hahaha. Some things never change with Louise."

    $ show_sprites(("l 1 angry", "g 1 happy"))
    voice "ch1.8_l_002"
    l "Tch...!"
    
    th "Unable to retort, just stewing in rage. I need to make a run for it before things blow up."
    
    voice "ch1.8_g_003"
    g "By the way, where is that commoner? I, Guiche, would like to lay eyes on him just once."
    
    $ show_sprites(("l 1 angry", "m 1 sad"))
    voice "ch1.8_m_001"
    m "..."

    $ show_sprites(("l 3 happy", "m 1 sad"))
    voice "ch1.8_l_003"
    l "By the way, Montmorency... I have a question I'd like to ask you once more."
    
    voice "ch1.8_m_002"
    m "W-what is it?"
    
    $ show_sprites(("l 3", "m 1 sad"))
    voice "ch1.8_l_004"
    l "Why do you avoid eye contact, I wonder?"

    voice "ch1.8_m_003"
    m "No, not really. Just doing some neck exercises, that's all."

    $ show_sprites(("l 3 angry", "m 1 sad"))
    voice "ch1.8_l_005"
    l "Didn't I tell you to stay silent? Why are we being found out like this!"

    $ show_sprites(("l 3 angry", "m 1 happy"))
    voice "ch1.8_m_004"
    m "Ah, ahaha... Sorry, I couldn't help it."

    voice "ch1.8_l_006"
    l "Don't give me that 'slipped out' excuse. I said it was a secret! If this keeps up, our future looks bleak."

    $ show_sprites(("g 1 happy", "m 1 happy"))
    voice "ch1.8_g_004"
    g "Eh, why is it a secret? There's no way the beautiful Montmorency would keep things from me!"

    $ show_sprites(("g 1 happy", "m 1 sad"))
    voice "ch1.8_m_005"
    m "Sorry, Louise. I wish I hadn't said a word just now."

    $ show_sprites(("g 1 sad", "m 1 sad"))
    voice "ch1.8_g_005"
    g "Eh? Did I do something wrong to you!?"

    $ show_sprites(("l 1 sad", "m 1 sad"))
    voice "ch1.8_l_007"
    l "Montmorency. I feel for you."

    $ show_sprites(("s 3 sad", "m 1 sad"))
    voice "ch1.8_s_001"
    s "I agree completely."

    $ show_sprites(("g 1 angry", "m 1 sad"))
    voice "ch1.8_g_006"
    g "Whaaat!? Why is everyone ganging up on me like this!?"

    $ show_sprites(("g 1 angry", "m 1"))
    voice "ch1.8_m_006"
    m "Anyway, putting that aside. We should go see how she’s doing later. She’s due for a check-up soon."
    
    $ show_sprites(("l 1", "m 1"))
    voice "ch1.8_l_008"
    l "Agreed. Since I have a lecture, let’s agree to gather everyone once it finishes. Is that fine?"
    
    voice "ch1.8_m_007"
    m "It’s fine with me."
   
    $ show_sprites(("g 2 happy", "m 1"))
    voice "ch1.8_g_007"
    g "I’m fine with that as well."

    $ show_sprites(("k 1", "t 1"),  anim_in="slide_right", anim_out="slide_right")
    voice "ch1.8_k_002"
    k "Understood."
    t "..."

    $ show_sprites(("s 3"),  anim_in="slide_right", anim_out="slide_right")
    voice "ch1.8_s_002"
    s "It's okay by me as well... if you say so."

    th "Classes... They’re useless to me. It’s just lessons on this world’s magic and history, after all."
    th "Sorry to Louise, but I think I’ll take a short walk."
    
    menu:
        "Library":
            $ fade_fx("library", new_music="t8")
            $ show_sprites(("s 1"))

            s "Not a sound... Libraries are quiet no matter what world you're in."
            s "Oh, what's that?"

            $ fade_fx("t_library_read")
            s "Yo, Tabitha."
            t "..."
            $ update_sympathy(20, char_key="tabitha")

            th "Huh, I wonder if she didn't hear me."

            s "Hey, Tabitha!"

            $ fade_fx("t_library_read_2")
            t "......I'll close my mouth."
            s "Ah, sorry.{#var2}"

            #! звук перелистывания страницы
            t "..."
            th "She's gotten absorbed in her book again."
            s "Tabitha? Tabitha-san, hellooo?"

            #! звук перелистывания страницы
            t "..."
            th "Hmm. To be this unresponsive... I have to applaud her."
            th "Still, just what is in a book that can captivate someone so completely?"

            menu:
                "Peek at the book":
                    th "I'm curious what's inside. Shall I sneak a look from behind her?"
                    s "Well now, what do we have here...?"
                    s "...?"
                    s "Can't read a word of this."
                    th "Come to think of it, I can understand the language here, but I can't read the writing at all."
                   
                    $ fade_fx("t_library_read_2")
                    t "An overview of the latest academic theories and international debates regarding special effects generated when combining Wind and Fire magic systems."
                    
                    s "Eh?{#e?}"
                    t "That's why it's pointless for you to read it."
                    s "Ah... I see."
                    th "On top of not being able to read it in the first place, if it's a thesis on magic, then yeah, it really is meaningless to me."
                    s "Sorry for disturbing you."
                    t "No problem."
                    s "Well then, I'll be going."
                    t "..."
                    th "I thought I saw her nod slightly just now... Does that mean she understood?"
                    s "Ah well, it's fine."

                "Take away the book":
                    s "Let's see, let's see?"
                    t "..."
                    s "......?"
                    s "What the heck is this? I can't make out a single word of what's written here."
                    th "Come to think of it, I can understand what people say here, but I can't read the writing at all."
                    t "An overview of the latest academic theories and international debates regarding special effects generated when combining Wind and Fire magic systems."
                    s "Eh?"
                    t "It's something you don't need to understand."
                    s "Ah... I see."
                    th "On top of not being able to read it in the first place, if it's a thesis on magic, then yeah, it really is meaningless to me."
                    s "My bad for interrupting. Here's the book."
                    t "..."
                    th "Can't read her expressionless face, but I wonder if she's actually angry."
                    th "Now that I think about it, grabbing a book out of someone's hands without warning is pretty rude. Guess I really stepped in it."
                    s "Alright, I'm heading out."
                    t "..."
                    th "I thought I saw her nod slightly just now... Does that mean she understood?"
                    s "Well, whatever."

                "Ask about the book's contents":
                    th "Maybe I should ask Tabitha what's written in it?"
                    s "Come on, what's actually written in this thing?"
                    t "...It's something you don't need to know."
                    s "...I mean, yeah, perhaps. But..."
                    th "Come to think of it, I can't read the writing anyway."
                    s "Umm... could you at least give me an explanation?"
                    t "..."
                    s "I guess that's a no?"
                    t "An overview of the latest academic theories and international debates regarding special effects generated when combining Wind and Fire magic systems."
                    s "Eh?"
                    t "That's why it's pointless for you to read it."
                    s "Ah... I see."
                    th "On top of not being able to read it in the first place, if it's a thesis on magic, then yeah, it really is meaningless to me."
                    s "Sorry for disturbing you."
                    t "...Not really."
                    th "Maybe I shouldn't have been so persistent... She doesn't seem all that angry, though."
                    s "Alright, I'm heading out."
                    t "..."
                    th "I thought I saw her nod slightly just now... Does that mean she understood?"
                    s "Well, whatever."
                    
        "Kirche's Room":
            "n"
        
        "Louise's Room":
            "n"
        
        "Hallway":
            "n"

    jump ch1_9
    return