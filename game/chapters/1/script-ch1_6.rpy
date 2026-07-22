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
            si "I-I don't know either."
            s "Huh? Weren't you there when we came to call for you?"
            si "Yes. I did let Miss Montmorency know, but as for everyone else, absolutely nothing..."
            l "So that leaves only one possible answer, doesn't it? Say, Montmorency?"
            m "...Hohoho."
            k "Now, now. I don’t know the details, but it seems things are getting rather interesting, isn’t it?"
            l "It's not like there's anything fun going on here."
            voice "ch1.6_t_002"
            t "...But I do have an interest."
            voice "ch1.6_s_011"
            s "Oh, really?"

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
            l "Oh, well. It’s not like I expect you to go home just because I tell you to."

    $ show_sprites(("l 1"))
    voice "ch1.6_l_005"
    l "Well, fine. It's like talking to a brick wall. I don't think any of you are leaving."
    l "More importantly, the problem is who this girl is."
    $ show_sprites(("l 1", "h 1 sad"))
    unk_h "Umm…? Excuse me, what on earth am I doing here…?"
    th "She looks bewildered, unable to make sense of what's going on. Not surprising, though."
    s "Well, let's see... To explain, Louise and I found you collapsed on the outskirts of town yesterday and brought you here."
    l "Incidentally, Siesta is the one who laid you in bed, and Montmorency examined you."
    ha "Oh, s-so that's how it was? My apologies, and thank you so much"
    si "Ah, no, I didn't really do anything..."
    m "Since you seemed exhausted, I simply instructed you to stay in bed and rest. That’s all I did."
    l "Now, I’d like to ask you something. Where do you come from? What’s your name?"
    ha "Y-yes. I am Haruna... 'Haruna Takanaqi"
    s "Just as I thought, Miss Takanaqi..."
    ha "You know about me? Saito... could you possibly be 'Hiraga Saito'?"
    s "Ah, that's right, I'm Saito Hiraga. It’s been a while, Takanaqi-san."
    ha "I'm so happy... To think we'd meet in a place like this!!"
    l "As I suspected! She's the girl Saito is acquainted with!"
    ha "Yes. I shared a class with Saito-kun and acted as our class president."
    l "Well, never mind. So, how did you get here?"
    ha "How... well, even if you ask me how... Out of nowhere, on a perfectly normal day, a round, mirror-like thing just appeared right before my eyes..."
    ha "The moment I touched it, it seems I ended up in this world."
    th "A round mirror... The same as what happened to me."
    ha "I had no idea where I was and was completely at a loss, when a woman who just happened to pass by stopped to help me..."
    l "But...?"
    ha "They put me in a locked room and shut me inside, just like that..."
    l "Oh? That sounds like a rather grim tale, don't you think?"
    k "Ordinarily, you'd think that woman is the mage who summoned her, but I can't say for certain."
    ha "Since I was kept confined all that while, I seized an opportunity to slip away. However..."
    l "With no acquaintances and nowhere to head to, you were simply wandering aimlessly... I guess you probably would've passed out eventually."
    ha "Y-yes."
    si "And it was you two who rescued her at that point. What incredible luck she had, honestly."
    ha "Ugh... Hiraga-kun!"
    s "Whoa!?"
    si "Wah!?"
    l "W-what is the meaning of this?! Why are you suddenly clinging to my familiar like that?! Get away from him!"
    ha "A familiar? What exactly is a 'familiar'? Hiraga-kun is a perfectly normal human being!"
    ha "To call him a familiar like that... Who do you think you are?!"
    l "Urgh!"
    k "I mean, it's not like you'd usually think of making a human into a familiar, right?"
    l "Onlookers, keep your mouths shut!"
    l "Um, this is an extremely unusual situation, but... I called Saito forth with the magic used to summon familiars, and we established a contract."
    l "So, even though Saito is human, he’s still my familiar. See? He has the familiar’s rune on his left hand."
    ha "...I see. I get that part."
    ha "I understand that, but... You have no right to interfere with me hugging Hiraga-kun!"
    l "What did you just say?!"
    ha "Saito is the very first and only acquaintance I’ve made in this world! Why shouldn’t I be glad to reunite with him?!"
    l "W-well, it’s not wrong, per se, but the way you expressed it is a bit... problematic."