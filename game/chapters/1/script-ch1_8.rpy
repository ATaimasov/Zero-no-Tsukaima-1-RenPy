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

    $ fade_fx("hallway_night", new_music="t3")
    
    menu:
        "Library":
            $ fade_fx("library", new_music="t8")
            $ show_sprites(("s 1"))

            voice "ch1.8_s_003"
            s "Not a sound... Libraries are quiet no matter what world you're in."

            voice "ch1.8_s_004"
            s "Oh, what's that?"

            $ fade_fx("t_library_read")
            voice "ch1.8_s_005"
            s "Yo, Tabitha."
            t "..."
            $ update_sympathy(20, char_key="tabitha")

            th "Huh, I wonder if she didn't hear me."

            voice "ch1.8_s_006"
            s "Hey, Tabitha!"

            $ dissolve_fx("t_library_read_2")
            voice "ch1.8_t_001"
            t "...Silence."

            voice "ch1.8_s_007"
            s "Ah, sorry.{#var2}"

            $ dissolve_fx("t_library_read")
            pause(0.5)
            play sound read
            t "..."
            th "She's gotten absorbed in her book again."

            voice "ch1.8_s_008"
            s "Tabitha? Tabitha-san, hellooo?"

            play sound read
            pause(0.5)
            t "..."
            th "Hmm. To be this unresponsive... I have to applaud her."
            th "Still, just what is in a book that can captivate someone so completely?"

            menu:
                "See what's in the book":
                    th "I'm curious what's inside. Shall I sneak a look from behind her?"
                    
                    voice "ch1.8_s_009"
                    s "Well now, what do we have here...?"

                    voice "ch1.8_s_010"
                    s "...?"

                    voice "ch1.8_s_011"
                    s "Can't read a word of this."
                    th "Come to think of it, I can understand the language here, but I can't read the writing at all."
                   
                    $ dissolve_fx("t_library_read_2")
                    voice "ch1.8_t_002"
                    t "...A general overview of the latest theories and discussions from various countries regarding the special effects that occur when superimposing the 'fire' system onto the 'wind' system."
                    
                    voice "ch1.8_s_012"
                    s "Eh?{#e?}"

                    voice "ch1.8_t_003"
                    t "...That's why it's pointless for you to read it."

                    voice "ch1.8_s_013"
                    s "Ah... I see."
                    th "On top of not being able to read it in the first place, if it's a thesis on magic, then yeah, it really is meaningless to me."
                    
                    voice "ch1.8_s_014"
                    s "Sorry for disturbing you."

                    voice "ch1.8_t_004"
                    t "...No problem."

                "Snatch the book":
                    th "Let's see what's written here... I suppose I'll just borrow it for a moment."
                    
                    voice "ch1.8_s_009-2"
                    s "Well now, what do we have here...?"

                    $ dissolve_fx("t_library_read_3", duration=2.0)
                    t "..."

                    $ update_sympathy(-20, char_key="tabitha")
                    $ update_sympathy(20, char_key="louise")

                    voice "ch1.8_s_010-2"
                    s "...?"

                    voice "ch1.8_s_021"
                    s "What the heck is this? I can't make out a single word of what's written here."

                    th "Come to think of it, I can understand the language here, but I can't read the writing at all."
                    
                    $ dissolve_fx("t_library_read_4")
                    voice "ch1.8_t_002-2"
                    t "...A general overview of the latest theories and discussions from various countries regarding the special effects that occur when superimposing the 'fire' system onto the 'wind' system."
                    
                    voice "ch1.8_s_012-2"
                    s "Eh?"

                    voice "ch1.8_t_003-2"
                    t "...It's something you don't need to understand."

                    voice "ch1.8_s_013-3"
                    s "Ah... I see."
                    th "On top of not being able to read it in the first place, if it's a thesis on magic, then yeah, it really is meaningless to me."
                    
                    voice "ch1.8_s_022"
                    s "My bad for interrupting. Here's the book."

                    $ dissolve_fx("t_library_read")
                    t "..."
                    th "Can't read her expressionless face, but I wonder if she's actually angry."
                    th "Now that I think about it, grabbing a book out of someone's hands without warning is pretty rude. Guess I really stepped in it."

                "Inquire about the book":
                    th "Maybe I should ask Tabitha what's written in it?"
                    
                    voice "ch1.8_s_017"
                    s "Hey, what's actually written in this thing?"

                    voice "ch1.8_t_005"
                    t "...It's something you don't need to know."
                    
                    $ update_sympathy(20, char_key="tabitha")
                    $ update_sympathy(-20, char_key="louise")
                    
                    voice "ch1.8_s_018"
                    s "...I mean, yeah, perhaps. But..."
                    th "Come to think of it, I can't read the writing anyway."

                    voice "ch1.8_s_019"
                    s "Umm... could you at least give me an explanation?"
                    
                    t "..."

                    voice "ch1.8_s_020"
                    s "I guess that's a no?"

                    $ dissolve_fx("t_library_read_2")
                    voice "ch1.8_t_002-3"
                    t "...A general overview of the latest theories and discussions from various countries regarding the special effects that occur when superimposing the 'fire' system onto the 'wind' system."
                    
                    voice "ch1.8_s_012-3"
                    s "Eh?"

                    voice "ch1.8_t_003-3"
                    t "...That's why it's pointless for you to read it."

                    voice "ch1.8_s_013-3"
                    s "Ah... I see."
                    th "On top of not being able to read it in the first place, if it's a thesis on magic, then yeah, it really is meaningless to me."
                    
                    voice "ch1.8_s_014-3"
                    s "Sorry for disturbing you."

                    $ dissolve_fx("t_library_read")
                    voice "ch1.8_t_006"
                    t "...Not really."
                    th "Maybe I shouldn't have been so persistent... She doesn't seem all that angry, though."
        
            voice "ch1.8_s_015"
            s "Well then, I'll be going."

            t "..."
            th "Did she just nod a little?... So she confirmed it?"
            
            voice "ch1.8_s_016"
            s "Well, whatever."

        "Kirche's Room":
            s "Kirche, are you there?"
            k "Oh, Darling? I haven't locked the door. Feel free to come in."
            s "Well then, excuse me for coming in."
            k "Come in. This is a rare occasion. What brings you here?"
            s "Well, I don't really have any business here, but... uh..."
            s "Wha—wha-what!?"
            k "Eh? What's going on!?"
            s "What's with that outfit-!?"
            k "Huh? Is something wrong with this outfit?"
            s "Don't give me that 'is something wrong' crap—!"
                menu:
                    "Act like a gentleman and close my eyes.":
                        th "R-right, in situations like this, it's only polite to close your eyes like a gentleman. As a true gentleman!"
                        k "Oh my, what's wrong, Darling? Closing your eyes all of a sudden like that."
                        s "Anyway, hurry up and get dressed. I've got my eyes closed. If you want, I can even step outside."
                        k "Oh, you really don't need to worry about that. I'm staying like this as long as I'm in my room anyway."
                        s "Well, I agree you're free to dress however you want in your own room, but... I'm still a guy, after all."
                        k "Ah... don't tell me you're turned on?"
                        s "If I'm honest, I'm scared of what happens next, so I'll deliberately keep my mouth shut!"
                        k "What happens next'... Oh! You mean you're scared of Louise finding out!"
                        s "...I didn't say anything, you know?"
                        k "Well, fine then. Anyway, how long are you going to keep your eyes closed?"
                        s "How long? Well, until you get dressed, obviously..."
                        k "Hup!"
                        th "Wha—!? What are these two soft, warm, and absolutely blissful sensations pressing against my chest—!?"
                        k "Hehe... Do you still intend not to open your eyes, even now?"
                        s "Ugh—!? No good, I can't hold back anymore!"
                        s "W-well, in any case... I'll be heading back now."
                        k "My, my... even an innocent Darling like you is charming. Do come back again."
                        th "Haa... haa... haa... Phew, that was a dangerous situation."
                        th "My reason was about to be swept away by youthful passions that had exceeded all limits..."
                        s "...Better go back and behave myself."
                    

                    "Take this opportunity to get a good look.":
                        th "Th-this is my chance? I should take this moment to enjoy the view... No, wait, observe!"
                        th "...stares intently."
                        k "...My, my?"
                        th "Seeing it up close again, how should I put it... it's amazing... Like 'boom, squeeze, boom!' or something."
                        k "Fufu, what do you think? Are you getting turned on?"
                        s "Yeah, a lot..."
                        k "Oh my, aren't you honest."
                        k "In that case, want to get a closer look?"
                        s "E-e-even closer... What?"
                        k "Oh, I'm just teasing, Darling. Let's just focus on building up the tension between us today, shall we?"
                        s "Uh... yeah..."
                        s "W-well, in any case... I'll be heading back now."
                        k "My, my... even an innocent Darling like you is charming. Do come back again."
                        th "Haa... haa... haa... Phew, that was a dangerous situation."
                        th "My reason was about to be swept away by youthful passions that had exceeded all limits..."
                        s "...Better go back and behave myself."






                    "Scold her.":
                        s "You mustn't go out in public dressed so sloppily! Besides, it's unseemly for a girl your age to act like that!"
                        k "What's the big deal? It's perfectly fine, isn't it?"
                        s "It's not okay! You should just wear your uniform like a normal person!"
                        k "No way! It's just too hot, that's all!"
                        s "Is that really how it works?"
                        k "That's just how it is!"
                        s "Well, I guess there's no helping it then..."
                        s "W-well, in any case... I'll be heading back now."
                        k "My, my... even an innocent Darling like you is charming. Do come back again."
                        th "Haa... haa... haa... Phew, that was a dangerous situation."
                        th "My reason was about to be swept away by youthful passions that had exceeded all limits..."
                        s "...Better go back and behave myself."

        
        "Louise's Room":
            "n"
        
        "Hallway":
            $ fade_fx("hallway_down_night", new_music="t18")
            
            $ show_sprites(("s 1"))
            # !
            voice "ch1.8_s_"
            s "..."
            th "Looks like I don't know anyone here."
            # !
            voice "ch1.8_s_"
            s "..."
            th "Then again, I don't really have any business here. I suppose I should just head back."

    jump ch1_9
    return