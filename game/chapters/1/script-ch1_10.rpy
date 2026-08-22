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
        $ dissolve_fx("forest", new_music="t6", sprites=("si 1", "s 1"))
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

        voice "ch1.10_s_024"
        s "I see..."

        menu:
            "You'll make an excellent wife":
                "s"

            "Is that delicious?":
                "s"

            "You're a thrifty person, right?":
                "s"




    return

label date_tabitha_1:
    if louise_sympathy == 100:
        call sp_l1
    else:
        "s"
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


