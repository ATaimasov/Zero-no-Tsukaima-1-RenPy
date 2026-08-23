# утро. с кем его провести
label ch1_10:
    $ fade_fx("sky", new_music="t4", type="cg")
    
    th "Ahhh... Hmm, what a nice morning."
    th "Louise has finished her morning routine and headed out somewhere too... Hmm, it's a truly pleasant morning."
    th "Well then... what should I do next?"

    play music t3 

    $ portrait_choice([
        {"char": "louise",   "text": "Go on a date with Louise",     "target": "date_louise_1"},
        {"char": "siesta",   "text": "Go on a date with Siesta",    "target": "date_siesta_1"},
        {"char": "tabitha",  "text": "Go on a date with Tabitha",    "target": "date_tabitha_1"},
        {"char": "kirche",   "text": "Go on a date with Kirche",     "target": "date_kirche_1"},
        {"char": "haruna",   "text": "Go on a date with Haruna",     "target": "date_haruna_1"},
    ])

    jump attention

    return

label date_louise_1:
    if louise_sympathy == 100:
        call sp_l1
    else:
        $ fade_fx("louise_room", new_music="t5")
        $ show_sprites(("s 1"))
        voice "ch1.10_s_001"
        s "Hey, Louise! You in there?"

        $ show_sprites(("l 6", "s 1"))
        voice "ch1.10_l_001"
        l "What? Do you need something?"

        $ update_sympathy(20, char_key="louise")

        $ show_sprites(("l 6", "s 1 shy"))
        voice "ch1.10_s_002"
        s "Huh... oh..."

        voice "ch1.10_l_002"
        l "What? What's the matter with you? Standing there like a statue."

        $ show_sprites(("l 6", "s 3 shy"))
        voice "ch1.10_s_003"
        s "No, no, never mind... well, actually..."


        th "She's wearing something different from her usual outfit. I feel like this is the first time I've ever seen Louise in casual clothes..."
        th "It's strange... just changing her outfit makes her seem like a completely different person."

        $ show_sprites(("l 6 angry", "s 3 shy"))
        voice "ch1.10_l_003"
        l "Hey, Saito!"

        $ show_sprites(("l 6 angry", "s 1"))
        voice "ch1.10_s_004"
        s "Huh? Oh, what?"

        voice "ch1.10_l_004"
        l "It's not just 'what'. Don't you have anything to say?"

        $ show_sprites(("l 6 angry", "s 1 sad"))
        voice "ch1.10_s_005"
        s "Like, what exactly am I supposed to say...?"

        voice "ch1.10_l_005"
        l "Geez!"

        voice "ch1.10_l_006"
        l "If you're my familiar, when you notice your master is wearing something different than usual, you should at least say something, right?"

        voice "ch1.10_s_006"
        s "An opinion, huh..."
        menu:
            "You look really beautiful.":
                $ show_sprites(("l 6 angry", "s 3 shy"))
                voice "ch1.10_s_007"
                s "You look really beautiful."

                $ show_sprites(("l 6 shy", "s 3 shy"))
                voice "ch1.10_l_007"
                l "Huh? W-what's with the sudden...?"

                $ update_sympathy(20, char_key="louise")

                voice "ch1.10_s_008"
                s "You told me to give my opinion all of a sudden, so I just said honestly what I was thinking."

                voice "ch1.10_l_008"
                l "H-honestly...? I-is that so. Th...thank you."

                voice "ch1.10_s_009"
                s "No, I don't think it's something you need to thank me for."

                $ show_sprites(("l 6 angry", "s 3 shy"))
                voice "ch1.10_l_009"
                l "Ugh... It's fine! Just stay quiet!"
            

            "I don't really get it.":
                voice "ch1.10_s_012"
                s "I don't really get it."

                $ show_sprites(("l 6 sad", "s 1 sad"))
                voice "ch1.10_l_011"
                l "...Huh?{#a?}"

                $ update_sympathy(-20, char_key="louise")

                voice "ch1.10_s_013"
                s "I mean, I don't know anything about women's clothes, so when you ask me what I think, I just don't know what to tell you."

                voice "ch1.10_l_012"
                l "S-Surely you have something to say. Like, 'You look cute,' 'You look pretty,' or 'It suits you'—something like that."

                $ show_sprites(("l 6 sad", "s 3 sad"))
                voice "ch1.10_s_014"
                s "But what am I supposed to say?"

                $ show_sprites(("l 6 angry", "s 3 sad"))
                voice "ch1.10_l_013"
                l "Ugh... that's enough! You're so dense!"

            "You don't seem like Louise.":
                $ show_sprites(("l 6 sad", "s 1"))
                voice "ch1.10_s_015"
                s "Somehow, it doesn't feel like you're Louise."

                voice "ch1.10_l_014"
                l "What's that supposed to mean?! Are you saying clothes like this don't suit me?!"

                voice "ch1.10_s_016"
                s "No, I think it suits you. It's just that I'm not at all used to seeing you dressed like that..."

                $ show_sprites(("l 6 sad", "s 3"))
                voice "ch1.10_s_017"
                s "It just doesn't feel like you're the Louise I'm used to."

                $ show_sprites(("l 6 shy", "s 3"))
                voice "ch1.10_l_015"
                l "U-um...?"

                $ show_sprites(("l 6 angry", "s 3"))
                voice "ch1.10_l_016"
                l "So you're saying I don't look like my usual self!?"

                voice "ch1.10_s_018"
                s "Now that you put it that way, maybe you're right. Though maybe I'm just not used to seeing you like this... Well, I guess your usual outfit is the best after all."

                voice "ch1.10_l_017"
                l "I went out of my way to show you my new outfit, and that's all you have to say!?"

        $ show_sprites(("l 6 angry", "s 1 sad"))
        voice "ch1.10_s_010"
        s "...? Why are you getting angry?"

        voice "ch1.10_l_010"
        l "Who knows! Enough is enough, just go outside!"

        voice "ch1.10_s_011"
        s "Ah... yeah."

        call open_door("right")

        th "Did I say something wrong...?"  

    return

label date_siesta_1:
    if louise_sympathy == 100:
        call sp_l1
    else:
        $ fade_fx("forest", new_music="t6", sprites=("si 1", "s 1"))
        voice "ch1.10_si_001"
        si "I'm sorry, Saito-san, for making you come all the way here with me."

        $ update_sympathy(20, char_key="siesta")

        $ show_sprites(("si 1", "s 1 happy"))
        voice "ch1.10_s_020"
        s "It's okay. I was the one who decided to tag along, even though you were busy with work."

        $ show_sprites(("si 1", "s 1"))
        voice "ch1.10_s_021"
        s "But you come out to this forest alone every time?"

        voice "ch1.10_si_002"
        si "Yes. Since this area is close to the Academy, there's no particular danger."

        voice "ch1.10_s_022"
        s "Hmm. Siesta, it seems like you're always working."

        $ show_sprites(("si 1 happy", "s 1"))
        voice "ch1.10_si_003"
        si "Well, it's my job. Besides, I do take proper breaks between work quite often."

        voice "ch1.10_si_004"
        si "So I'm fine. Besides, Saito-san, you work nonstop too, don't you?"

        $ show_sprites(("si 1 happy", "s 3 happy"))
        voice "ch1.10_s_023"
        s "Ah, well, I'm basically a househusband, so I don't really think much of it."

        $ show_sprites(("si 1", "s 3 happy"))
        voice "ch1.10_si_005"
        si "{i}Sighs{/i}... Oh, there it is. Saito-san, I found it."

        $ show_sprites(("si 1", "s 1 happy"))
        voice "ch1.10_s_024"
        s "Oh, wild edible plants."

        voice "ch1.10_si_006"
        si "Yes. The kinds you can gather differ depending on the season, but I often come here like this to pick wild edible plants."

        $ show_sprites(("si 1 happy", "s 1 happy"))
        voice "ch1.10_si_007"
        si "The nobles don't seem to care for them, but we often use them in our cooking. If they're prepared properly, they're actually pretty good."

        voice "ch1.10_s_025"
        s "I see..."

        menu:
            "You'll make an excellent wife":
                $ show_sprites(("si 1 happy", "s 3"))
                voice "ch1.10_s_026"
                s "I have to say, I'm impressed. Siesta, you'd make a good wife."

                $ show_sprites(("si 4 shy", "s 3"))
                voice "ch1.10_si_008"
                si "Huh?{#e}"

                $ update_sympathy(20, char_key="siesta")

                $ show_sprites(("si 1 happy", "s 1"))
                voice "ch1.10_s_027"
                s "Hm? What's wrong?"

                $ show_sprites(("si 1 shy", "s 1"))
                voice "ch1.10_si_009"
                si "U-Um... S-Saito-san, what did you just say...?"

                voice "ch1.10_s_028"
                s "I just said you'd make a good wife. You're good at cooking, but you're good at housework too, and you're so dependable..."

                voice "ch1.10_s_029"
                s "I think the guy who marries Siesta is definitely going to be a lucky man."

                $ show_sprites(("si 4 shy", "s 1"))
                voice "ch1.10_si_010"
                si "N-No, don't say that... Saito-san..."

                $ show_sprites(("si 4 shy", "s 1 sad"))
                voice "ch1.10_s_030"
                s "What's wrong, Siesta? Your face looks kind of red."

                voice "ch1.10_si_011"
                si "I-I... well... N-Next time, I'll make some dishes with wild mountain greens for you too, Saito-san!"

                $ show_sprites(("si 4 shy", "s 1"))
                voice "ch1.10_s_031"
                s "Huh? Yeah, I'll look forward to it."

            "Is that delicious?":
                voice "ch1.10_s_033"
                s "Is that tasty?"

                voice "ch1.10_si_014"
                si "It is. It's just right. I'll make some for you next time."

                voice "ch1.10_s_034"
                s "Really? Is that okay?"

                $ show_sprites(("si 4 shy", "s 1"))
                voice "ch1.10_si_015"
                si "Yes. You seem to enjoy the dishes from my hometown, Saito-san."

                $ show_sprites(("si 4 happy", "s 1"))
                voice "ch1.10_si_016"
                si "I know quite a few wild-vegetable recipes that my mother and the others taught me, so I can make all sorts of things."

                voice "ch1.10_s_035"
                s "Oh, that's something to look forward to."

            "So you're a thrifty person.":
                voice "ch1.10_s_036"
                s "You're pretty thrifty, Siesta."

                $ show_sprites(("si 1", "s 1"))

                voice "ch1.10_si_017"
                si "It's not really about being thrifty... It just seems like such a waste when something is perfectly edible."

                $ update_sympathy(-20, char_key="siesta")

                $ show_sprites(("si 1", "s 3"))
                voice "ch1.10_s_037"
                s "I think that's what you call being thrifty, though."

                voice "ch1.10_si_018"
                si "I-Is that so?"

                $ show_sprites(("si 1", "s 1"))
                voice "ch1.10_s_038"
                s "Yeah.{#var2}"

                $ show_sprites(("si 4 sad", "s 1"))
                voice "ch1.10_si_019"
                si "I see... I thought this was just normal."

        $ show_sprites(("si 1", "s 1"))
        voice "ch1.10_si_012"
        si "Come on, let's keep picking and take plenty home!"

        $ show_sprites(("si 1", "s 3 happy"))
        voice "ch1.10_s_032"
        s "Got it. I'll carry the wild greens we pick, so don't hold back."

        $ show_sprites(("si 1 happy", "s 3 happy"))
        voice "ch1.10_si_013"
        si "Thank you. Ufufu... I'll pick lots of them today."

    return

label date_tabitha_1:
    if louise_sympathy == 100:
        call sp_l1
    else:
        $ fade_fx("bg tabitha_room", new_music="t8", sprites=("s 1"))

        voice "ch1.10_s_039"
        s "Yo, Tabitha."

        $ fade_fx("t_library_read_2", type="cg")
        voice "ch1.10_t_001"
        t "…What do you want?"

        $ update_sympathy(20, char_key="tabitha")

        voice "ch1.10_s_040"
        s "Hmm, well, not really anything in particular, but since we're here, why don't we go somewhere?"

        voice "ch1.10_t_002"
        t "…I'd rather read a book."

        voice "ch1.10_s_041"
        s "Ah… I see."

        th "Books, huh… I still can't read the writing here."

        $ dissolve_fx("t_library_read", type="cg")
        t "..."

        th "Wait, the conversation's already over, and she's reading a book!"

        play sound read
        t "..."

        voice "ch1.10_s_042"
        s "…Hey. Is there anything I can help you with?"

        voice "ch1.10_t_003"
        t "…Everything that needs to be done can be done with magic. So, not really."

        voice "ch1.10_s_043"
        s "Is that so?{#ver2}"

        play sound read

        voice "ch1.10_t_004"
        t "…Yes."

        th "Even so… If I just go home like this, I'll feel like an idiot."

        voice "ch1.10_s_044"
        s "Oh, that's right."

        menu:
            "Let me turn the pages for you.":
                voice "ch1.10_s_045"
                s "Want me to turn the pages for you?"

                voice "ch1.10_t_005"
                t "…No."

                voice "ch1.10_s_046"
                s "Don't be shy."

                $ dissolve_fx("t_library_read_2", type="cg")

                voice "ch1.10_t_006"
                t "…I don't think you could turn the pages at the same speed I read."

                voice "ch1.10_s_047"
                s "Hmph. When you put it that way, I guess I'm not so sure."

                voice "ch1.10_s_048"
                s "Then I'll watch you for a while so I can get a feel for your pace, Tabitha."

                
                voice "ch1.10_t_007"
                t "…Yes."

                $ dissolve_fx("t_library_read", type="cg")
                play sound read
                t "..."

                play sound read
                t "..."

                th "Hmm. I don't really get it, but she reads at a pretty fast pace."

                play sound read
                t "..."

                play sound read
                t "..."

                voice "ch1.10_s_049"
                s "Come to think of it, what kind of book is this?"

                voice "ch1.10_t_008"
                t "…A spellbook."

                voice "ch1.10_s_050"
                s "I see."

                play sound read
                t "..."

                th "Somehow, I feel like just watching Tabitha read like this isn't such a bad idea."

                play sound read
                t "..."

            "Let me massage your shoulders.":
                voice "ch1.10_s_051"
                s "I'll give your shoulders a massage."

                voice "ch1.10_t_009"
                t "…No."

                voice "ch1.10_s_052"
                s "Don't be shy. I won't disturb your reading."

                t "..."

                $ fade_fx("t_massage", type="cg")
                voice "ch1.10_s_053"
                s "There we go. I guess I'll start around here."

                th "Rub, rub, rub…"

                play sound read
                t "..."

                voice "ch1.10_s_054"
                s "Whoa, you've got quite a lot of tension in your shoulders! Is your posture usually not very good?"

                play sound read
                t "..."

                th "Rub, rub, rub, rub…"

                play sound read
                t "..."

                voice "ch1.10_s_055"
                s "Hmm, maybe around here…"

                play sound read
                t "..."

                th "Rub, rub, rub, rub, rub…"

                $ dissolve_fx("t_massage_2", type="cg")
                voice "ch1.10_t_010"
                t "…A little higher."

                $ update_sympathy(20, char_key="tabitha")

                voice "ch1.10_s_056"
                s "Eh?{#e?}"

                voice "ch1.10_s_057"
                s "Oh, a little higher. Got it."

                th "Rub, rub, rub, rub, rub, rub…"

                $ dissolve_fx("t_massage_3", type="cg")
                play sound read
                t "..."

                voice "ch1.10_s_058"
                s "Like this?"

                play sound read
                t "..."

                $ fade_fx("t_library_read", type="cg")
               
            "Let me hold you.":
                voice "ch1.10_s_059"
                s "Want me to carry you?"

                voice "ch1.10_t_011"
                t "…No."

                $ update_sympathy(-20, char_key="tabitha")

                voice "ch1.10_s_060"
                s "Don't be shy."

                voice "ch1.10_t_012"
                t "…I'm not."

                voice "ch1.10_s_061"
                s "All right! Up you go."

                $ fade_fx("bg tabitha_room")
                t "..."

                voice "ch1.10_s_062"
                s "How's this?"

                play sound read 
                t "..."

                s "..."

                play sound read 
                t "..."

                s "..."

                play sound read 
                t "..."

                s "..."

                voice "ch1.10_t_013"
                t "…It's hard to read."

                voice "ch1.10_s_063"
                s "I see.{#ver2}"

                voice "ch1.10_t_014"
                t "…Put me down."

                voice "ch1.10_s_064"
                s "Okay."

                $ fade_fx("t_library_read", type="cg")

                play sound read
                t "..."

        play sound read
        t "..."
        th "In the end, all I did was watch Tabitha read her book. Well, I guess some days are like this."
    return

label date_kirche_1:
    if louise_sympathy == 100:
        call sp_l1
    else:
        "s"
    return

label date_haruna_1:
    if louise_sympathy == 100:
        call sp_l1
    else:
        "s"
    return


