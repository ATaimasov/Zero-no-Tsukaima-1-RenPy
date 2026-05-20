label louise_outfit_choice:
    menu:
        "I thoughts it's good!":
            $ choice_result = "good"
        "I don't care":
            $ choice_result = "neutral"
        "It's terrible!":
            $ choice_result = "bad"
    return

label ch1_main:

    call overlay_screen("overlay",  "Chapter 1 \"Louise of Zero\"", isUseBlur=False, text_mode="black")
    pause(2)
    play music audio.t18 fadein 1.0
    scene bg forest at bg_center with dissolve
    
    call overlay_screen("forest",  "The Road (Highway)")
    pause(2)
    scene cg l_s_forest at bg_center with dissolve

    l "....."
    voice "ch1_s_001"
    s "……Hey, Louise-san, can you hear me?"

    voice "ch1_l_001"
    l "What?"

    voice "ch1_s_002"
    s "I was wondering…"

    scene cg l_s_forest_l_speak at bg_center with dissolve

    voice "ch1_l_002"
    l "……go ahead and say it"

    voice "ch1_s_003"
    s "If I recall correctly, this morning you said, \"It's been forever since I've gone out shopping in town on a day off!\""

    voice "ch1_s_004"
    s "…or something along those lines, didn't you say? I seem to recall it sounded like you were having quite a bit of fun."

    scene cg l_s_forest at bg_center with dissolve

    voice "ch1_l_003"
    l "I wonder if something like that really happened..."

    scene cg l_s_forest_s_speak at bg_center with dissolve

    voice "ch1_s_005"
    s "No, no, no, of course I'm curious! You seemed to be having so much fun back then—why on earth are you in such a bad mood now?"

    voice "ch1_l_004"
    l "Well, of course YOU had a great time. You were going all lovey-dovey with every girl in sight..."

    voice "ch1_l_005"
    l "Really, nothing could be more unseemly!"

    scene cg l_s_forest at bg_center with dissolve

    voice "ch1_s_006"
    s "I wasn't being all lovey-dovey or anything! Wait… could it be you're jealous?"

    scene cg l_s_forest_l_speak at bg_center with dissolve

    voice "ch1_l_006"
    l "Th-th-that's ridiculous, of course not!"

    voice "ch1_l_007"
    l "If my stupid familiar goes around causing trouble everywhere, it'll reflect badly on me—your master! It's not like I'm jealous or anything, okay!"

    scene cg l_s_forest_s_speak at bg_center with dissolve
    
    voice "ch1_s_007"
    s "Is that so, huh?"

    voice "ch1_l_008"
    l "That's exactly right!"

    scene bg forest at bg_center with fade
    show s 1 at normal_center with dissolve
    thoughts "My name is Hiraga Saito. I was supposed to be just an ordinary high school student... or so I thought."
    hide s 1
    show l 1 at normal_center with dissolve
    thoughts "But now, I'm with this willful master — Louise Françoise Le Blanc de La Vallière..."
    thoughts "Long story short: thanks to Louise's summoning spell, I — who got called here as a familiar — am now living in her room."

    hide l 1
    show bg sky at bg_center with fade
    thoughts "In another world, \"Halkeginia\", where mages rule the land as nobility... It was a world entirely unlike Japan."
    thoughts "What's more, the country we live in—Tristain—suddenly came under invasion from \"Reconquista\"."
    thoughts "Using the Zero fighter found in Siesta's hometown and the power of Louise's \"Void\" magic, we somehow managed to repel Reconquista's massive fleet."
    thoughts "Having suffered devastating losses, Reconquista won't be launching another invasion anytime soon."
    thoughts "Well, I guess this is what they call a fleeting moment of peace…"
    thoughts "But when will I ever be able to return to Japan..."
    thoughts "Well, I guess it'll all work out somehow… It's always been like that up to now, anyway…"
    thoughts "Then again, my lower back really aches… I still haven't gotten used to riding a horse…"

    scene cg l_s_forest at bg_center with fade

    voice "ch1_s_008"
    s "Still, she went on a bit of a weird clothes-shopping spree this time. And it takes forever to pick anything out... Honestly, I was just killing time the whole way through..."

    scene cg l_s_forest_l_speak at bg_center with dissolve

    voice "ch1_l_009"
    l "W-well, it's not like it's a bad thing! What's so wrong with me dressing up!?"

    thoughts "Louise actually looks really nice..."

    #choise
    call louise_outfit_choice

    if choice_result == "good":

        voice "ch1_s_009"
        s "I thoughts it's great! You've got good looks to begin with. So paying more attention to your appearance is totally fine."
        scene cg l_s_forest at bg_center with dissolve

        voice "ch1_l_010"
        l "I-is that so...?"

        $ update_sympathy(20)

        voice "ch1_s_010"
        s "But why do girls take so long just picking out clothes? I just don't get it at all..."
    elif choise_result == "neutral": 

        ## симпатия луизы не меняется

        voice "ch1_s_011"
        s "Either one's fine. It's got nothing to do with me, anyway."

        voice "ch1_s_012"
        s "Just one thing though: don't go dumping any extra hassle on me, alright?"
    elif choise_result == "bad":

        scene cg l_s_forest_s_speak at bg_center with dissolve
        voice "ch1_s_013"
        s "Of course it's no good, right? Do you really want to dress up so badly that you'd go to the trouble of putting me through all this, huh?"

        $ update_sympathy(-20)
    else:
        "ERR"

    ## louise shows tsun-tsun side in any case :)

    scene cg l_s_forest_l_speak at bg_center with dissolve

    voice "ch1_l_011"
    l "Ugh, what is it, what is it?! You've done nothing but complain this whole time! Hello? You're my familiar, aren't you? So stop whining and get to work!"

    voice "ch1_l_012"
    l "For one thing, I go out of my way to try on clothes at the shop, and you can't even bother to look properly—or tell me what you think!"

    voice "ch1_s_014"
    s "Hm? What was that?"

    voice "ch1_l_013"
    l "It's nothing, really! I've been making sure you eat properly these days, so the least you can do is obediently listen to your master!"

    voice "ch1_s_015"
    s "Yeah yeah, sure thing~"

    scene cg l_s_forest at bg_center with dissolve
    thoughts "Jeez... She's got such a cute look going for her. If only her personality had even a tiny bit of that same charm, I wouldn't have a single complaint..."
    scene cg l_s_forest_l_speak at bg_center with dissolve

    voice "ch1_l_014"
    l "Did you say something!?"

    voice "ch1_s_016"
    s "N-no, nothing at all!"

    scene bg forest at bg_center with fade

    show d 1 happy at slide_left_to_center_in
    voice "ch1_d_001"
    d "Hah hah haa! Still getting bossed around by her, huh, partner?"

    show d 1 at normal_center
    voice "ch1_l_015"
    l "I do NOT boss him around!"

    voice "ch1_s_017"
    s "I'm NOT being bossed around, okay?!"

    show d 1 at close_center with dissolve
    thoughts "This is Derflinger. As you can see, a talking sword. Well, he's my partner, I guess."
    thoughts "It's good that he told me I'm the legendary familiar 'Gandálfr', but he just won't give me any details."
    thoughts "Partner says he's simply forgotten everything, but... I wonder if he'll remember anything at all..."

    show d 1 happy at normal_center with dissolve
    voice "ch1_d_002"
    d "Well, well, you two are getting along nicely, huh? I was starting to sweat, wondering when my turn would ever come!"

    show d 1 at normal_center
    voice "ch1_d_003"
    d "See, a mage and their familiar—they're one-of-a-kind partners, that's the thing. So you two getting along? That's a good thing, y'know!"

    voice "ch1_d_004"
    d "Besides, when a noble young lady goes out of her way to dress up for her partner's sake — that's quite the gesture, y'know!"

    show d 1 shy at normal_center with dissolve
    voice "ch1_d_005"

    # !!!
    if choice_result == "good":
        d "See? That’s it. A real man knows to offer a gentle word when it counts—that’s what being a man’s all about, huh?"
    else:
        d "C'mon, partner — a real man at least offers a gentle word when it counts, yeah?"

    voice "ch1_l_016"
    l "If you run your mouth one more time, I'll melt you down into scrap iron and bury you in the academy's backyard — got it?!"

    show d 1 sad at normal_center with dissolve
    voice "ch1_d_006"
    d "Whoa, scary! Partner, I'll just take a little nap for now — so when my cue comes, give me a holler, yeah?"
    show d at slide_center_to_right_out   
    pause 0.4                   
    hide d 

    voice "ch1_s_018"
    s "Sheesh..."

    show l 3 at slide_left_to_center_in
    thoughts "My master, Louise... she's stubborn, fiercely proud, and quick to anger..."
    thoughts "Well, regarding the fact that she... ahem, has no chest... since she seriously stresses over it, I'd better keep quiet..."
    thoughts "But sometimes she's unexpectedly gentle... and honestly, she looks pretty cute at times."
    thoughts "Anyway, I just can't leave her be... Must be the classic curse of a guy who's lost his heart."

    scene cg l_s_forest_l_s_speak at bg_center with fade
    play music audio.t27 fadein 1.0

    
    thoughts "Hm...? Someone's collapsed."

    voice "ch1_l_017"
    l "Hey, Saito? What's wrong?"

    voice "ch1_s_019"
    s "Over there... Isn't someone lying at the foot of that tree?"

    scene cg l_s_forest_s_speak at bg_center with dissolve

    voice "ch1_l_018"
    l "What? Where?"

    voice "ch1_s_020"
    s "Hey, over there... nah, better to see for myself. My bad, Louise! I'm going first!"

    scene cg l_forest at bg_center with dissolve

    voice "ch1_l_019"
    s "Ah—wait, Saito! Ugh, what is wrong with you?!"

    scene cg ha_forest at bg_center with fade

    voice "ch1_s_021"
    s "Just as I thought... There really is someone collapsed... I wonder if she is okay... wait—huh, hey!?"

    voice "ch1_l_020"
    l "Seriously, Saito! What are you doing leaving your master behind?! ...Wait, there really is someone collapsed..."

    voice "ch1_l_021"
    l "This girl... she's wearing such unfamiliar clothes. Just what country could she be from, I wonder?"

    thoughts "That blazer she's wearing... now that I look closer, isn't that the uniform from the school I used to go to?"
    thoughts "Why is this girl wearing these clothes? Could it be... she's from Japan too, just like me...?"
    thoughts "No, no... this girl... It’s like I’ve met her somewhere before..."
    thoughts "Where, exactly? Back at my school in Japan?"
    thoughts "I remember now. No doubt about it. She’s \"Haruna Takana\", our class representative...?"
    thoughts "No, wait... Get a grip, me. What the hell is Takana-san doing in this world?"

    voice "ch1_l_022"
    l "Hey, Saito. What's with you staring at this girl so intently?"

    voice "ch1_s_022"
    s "Ah, uh—my bad, my bad. First things first, I should help her out..."

    voice "ch1_s_023"
    s "First, check pulse and heartbeat..., loosen her clothes to keep the airway clear..."

    # !!!
    play sound "audio/sfx/punch.ogg"
    scene cg ha_forest at bg_center with hit_shake
    pause(0.5)

    voice "ch1_l_023"
    l "Saito, what do you think you're doing?! Trying to take off a girl's clothes?!"




        
    return