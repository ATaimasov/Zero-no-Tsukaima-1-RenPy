# утро. с кем его провести
label ch1_10:
    $ fade_fx("sky", new_music="t4")
    
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
    s "Hey, Louise! You in there?"
    l "What? Do you need something?"
    s "Huh... oh..."
    l "What? What's the matter with you? Standing there like a statue."
    s "No, no, never mind... well, actually..."
    th "She's wearing something different from her usual outfit. I feel like this is the first time I've ever seen Louise in casual clothes..."
    th "It's strange... just changing her outfit makes her seem like a completely different person."
    l "Hey, Saito!"
    s "Huh? Oh, what?"
    l "It's not just 'what'. Don't you have anything to say?"
    s "Like, what exactly am I supposed to say...?"
    l "Geez!"
    l "If you're my familiar, when you notice your master is wearing something different than usual, you should at least say something, right?"
    s "An opinion, huh..."
    menu:
        "You look really beautiful.":
            s "You look really beautiful."
            l "Huh? W-what's with the sudden...?"
            s "You told me to give my opinion all of a sudden, so I just said honestly what I was thinking."
            l "H-honestly...? I-is that so. Th...thank you."
            s "No, I don't think it's something you need to thank me for."
            l "Ugh... It's fine! Just stay quiet!"
            s "...? Why are you getting angry?"
            l "Who knows! Enough is enough, just go outside!"
            s "Ah... yeah."
            th "Did I say something wrong...?"

        "I don't really get it."

        "You don't seem like Louise."     

    return

label date_siesta_1:
    "s"
    return

label date_tabitha_1:
    "s"
    return

label date_kirche_1:
    "s"
    return

label date_haruna_1:
    "s"
    return


