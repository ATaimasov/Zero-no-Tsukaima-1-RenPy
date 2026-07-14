# Combined Ren'Py Scripts

Объединенный файл скриптов (с учетом вложенных папок).

*Примечание: при сборке были намеренно проигнорированы папки: tl, cache.*

## Файл: `chapters\0\script-ch0.rpy`

```renpy
label ch0:
    stop music fadeout 2.0
    call overlay_screen("town_square_night", "Tristania") from _call_overlay_screen
    play sound blow
    $ flash_clear("town_square_night")
    with explosion_shake
    pause(0.5)

    play music audio.t23 fadein 1.0
    
    show npc 1 angry as npc_left at close_center with dissolve

    #$ show_sprites(("npc 1 angry"))
    voice "ch0_npc1_001"
    npc1 "Where did the explosion happen?"

    #$ show_sprites(("npc 1 angry", "npc 1 angry"))

    show npc 1 angry as npc_left at close_left_npc

    show npc 1 angry as npc_right at close_right_npc with dissolve
    voice "ch0_npc1_002"
    npc2 "Sir—on the street facing the main avenue, multiple explosions involving explosive materials have been confirmed."

    voice "ch0_npc1_003"
    npc1 "Hurry up and dispatch the fire response team. Do not let the damage escalate."

    voice "ch0_npc1_004"
    npc2 "Yes, Sir!"

    hide npc_left with dissolve
    hide npc_right with dissolve

    call overlay_screen(None,  "My name is Louise Françoise Le Blanc de La Vallière", text_mode="white", delay=5.5, sound_path="ch0_l_001") from _call_overlay_screen_1
    scene bg town_square_night at bg_center with dissolve

    show npc 1 as npc_left at close_left_npc with dissolve
    show npc 1 as npc_right at close_right_npc with dissolve

    voice "ch0_un_001"
    unknown "Hahahaha. You're always working hard."

    show npc 1 sad as npc_left at close_left_npc
    voice "ch0_npc1_005"
    npc1 "Where is he?"

    show npc 1 angry as npc_right at close_right_npc
    voice "ch0_npc1_006"
    npc2 "Sir, he's on top of that mansion."

    call overlay_screen(None, "The Pentagon that governs the five powers", text_mode="white", delay=3.5, sound_path="ch0_l_002") from _call_overlay_screen_2
    scene cg terrorist at bg_center with dissolve

    voice "ch0_un_002"
    unknown "Let's call it a day. Hurry up and put out the fire."

    voice "ch0_npc1_007"
    npc1 "You—what's your objective?"

    voice "ch0_un_003"
    unknown "Objective? To dismantle every rule this country stands on."

    voice "ch0_npc1_008"
    npc2 "Huh?"

    voice "ch0_un_004"
    unknown "Until then, you'll just have to cherish your mundane lives, won't you?"

    scene cg terrorist2 at bg_center with flash

    voice "ch0_npc1_009"
    npc2 "He... did he just vanish?"

    voice "ch0_npc1_010"
    npc1 "Hey! Apprehend him immediately!"

    voice "ch0_npc1_011"
    npc2 "Yes, Sir!"

    call overlay_screen(None, "Bestow blessings upon this one, and make them my familiar", delay=4.5, text_mode="white", sound_path="ch0_l_003") from _call_overlay_screen_3
    stop music fadeout 1.0
    pause(1)
    call intro from _call_intro_1

    jump ch1
```

## Файл: `chapters\1\script-ch1_1.rpy`

```renpy
label forest_battle:
    call screen battle_menu
    
    if _return == "start_battle":
        # Initialize battle state
        $ init_battle(["mage", "mage"])
        
        # Show battle screen and get result
        call screen battle_screen
        
        if _return == "victory":
            return 
        elif _return == "defeat":
            "Game Over..."
            
    elif _return == "cancel":
        "test"
        # action Rollback()
    return

# forest
label ch1:
    call overlay_screen("overlay",  "Chapter One: \"Louise of Zero\"", isUseBlur=False, text_mode="black") from _call_overlay_screen_4
    pause(2)
    play music audio.t18 fadein 1.0
    scene bg forest at bg_center with dissolve
    
    call overlay_screen("forest",  "The Road (Highway)") from _call_overlay_screen_5
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
    s "If I recall correctly, this morning you said, 'It's been forever since I've gone out shopping in town on a day off!'"

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
    $ show_sprites("s 1", mode="big")

    th "My name is Hiraga Saito. I was supposed to be just an ordinary high school student... or so I thought."
    $ show_sprites("l 1", mode="big")
    th "But now, I'm with this willful master — Louise Françoise Le Blanc de La Vallière..."
    th "Long story short: thanks to Louise's summoning spell, I — who got called here as a familiar — am now living in her room."

    $ fade_clear("bg sky")

    th "In another world, \"Halkeginia\", where mages rule the land as nobility... It was a world entirely unlike Japan."
    th "What's more, the country we live in—Tristain—suddenly came under invasion from \"Reconquista\"."
    th "Using the Zero fighter found in Siesta's hometown and the power of Louise's \"Void\" magic, we somehow managed to repel Reconquista's massive fleet."
    th "Having suffered devastating losses, Reconquista won't be launching another invasion anytime soon."
    th "Well, I guess this is what they call a fleeting moment of peace…"
    th "But when will I ever be able to return to Japan..."
    th "Well, I guess it'll all work out somehow… It's always been like that up to now, anyway…"
    th "Then again, my lower back really aches… I still haven't gotten used to riding a horse…"

    scene cg l_s_forest at bg_center with fade

    voice "ch1_s_008"
    s "Still, she went on a bit of a weird clothes-shopping spree this time. And it takes forever to pick anything out... Honestly, I was just killing time the whole way through..."

    scene cg l_s_forest_l_speak at bg_center with dissolve

    voice "ch1_l_009"
    l "W-well, it's not like it's a bad thing! What's so wrong with me dressing up!?"

    th "Louise actually looks really nice..."

    # ==== CHOISE 1 ====
    $ choise_result = None
    menu:
        "I thoughts it's good!":
            $ choise_result = "good"
        "I don't care":
            $ choise_result = "neutral"
        "It's terrible!":
            $ choise_result = "bad"

    if choise_result == "good":

        voice "ch1_s_009"
        s "I thoughts it's great! You've got good looks to begin with. So paying more attention to your appearance is totally fine."
        scene cg l_s_forest at bg_center with dissolve

        voice "ch1_l_010"
        l "I-is that so...?"

        window hide
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

        window hide
        $ update_sympathy(-20)
    else:
        "ERR"

    #$ show_sympathy_hud()

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
    th "Jeez... She's got such a cute look going for her. If only her personality had even a tiny bit of that same charm, I wouldn't have a single complaint..."
    scene cg l_s_forest_l_speak at bg_center with dissolve

    voice "ch1_l_014"
    l "Did you say something!?"

    voice "ch1_s_016"
    s "N-no, nothing at all!"

    #scene bg forest at bg_center with fade
    $ fade_clear("bg forest")

    $ show_sprites("d 1 happy")
    pause(0.2)
    voice "ch1_d_001"
    #! тут быстрая прокручивание диалогов колесиком мыши или ctrl делает спрайты прозрачным
    d "Hah hah haa! Still getting bossed around by her, huh, partner?"

    $ show_sprites(("l 3 angry", "d 1"))
    voice "ch1_l_015"
    l "I do NOT boss him around!"

    $ show_sprites(("l 3 angry", "d 1", "s 3 angry"))
    voice "ch1_s_017"
    s "I'm NOT being bossed around, okay?!"

    #! тут нужен скейл плавный
    $ show_sprites("d 1")
    $ show_sprites("d 1", mode="big", anim="slide")

    th "This is Derflinger. As you can see, a talking sword. Well, he's my partner, I guess."
    th "It's good that he told me I'm the legendary familiar 'Gandálfr', but he just won't give me any details."
    th "Partner says he's simply forgotten everything, but... I wonder if he'll remember anything at all..."

    $ show_sprites("d 1 happy")
    voice "ch1_d_002"
    d "Well, well, you two are getting along nicely, huh? I was starting to sweat, wondering when my turn would ever come!"

    $ show_sprites("d 1")
    voice "ch1_d_003"
    d "See, a mage and their familiar—they're one-of-a-kind partners, that's the thing. So you two getting along? That's a good thing, y'know!"

    voice "ch1_d_004"
    d "Besides, when a noble young lady goes out of her way to dress up for her partner's sake — that's quite the gesture, y'know!"

    $ show_sprites("d 1 shy")
    voice "ch1_d_005"

    # !!!
    if choise_result == "good":
        d "See? That’s it. A real man knows to offer a gentle word when it counts—that’s what being a man’s all about, huh?"
    else:
        d "C'mon, partner — a real man at least offers a gentle word when it counts, yeah?"

    $ show_sprites(("l 3 angry", "d 1 shy"))
    voice "ch1_l_016"
    l "If you run your mouth one more time, I'll melt you down into scrap iron and bury you in the academy's backyard — got it?!"

    $ show_sprites(("l 3 angry", "d 1 sad"), side="center")
    voice "ch1_d_006"
    d "Whoa, scary! Partner, I'll just take a little nap for now — so when my cue comes, give me a holler, yeah?"

    $ show_sprites(("l 3 angry", "s 1 sad"))

    voice "ch1_s_018"
    s "Sheesh..."

    $ show_sprites("l 3", mode="big")
    th "My master, Louise... she's stubborn, fiercely proud, and quick to anger..."
    th "Well, regarding the fact that she... ahem, has no chest... since she seriously stresses over it, I'd better keep quiet..."
    th "But sometimes she's unexpectedly gentle... and honestly, she looks pretty cute at times."
    th "Anyway, I just can't leave her be... Must be the classic curse of a guy who's lost his heart."

    # ==== SUBCHAPTER 2 ====
    $ fade_clear("cg l_s_forest_l_s_speak", new_music="t27") 
    
    th "Hm...? Someone's collapsed."

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
    l "Ah—wait, Saito! Ugh, what is wrong with you?!"

    $ fade_clear("cg ha_forest")

    voice "ch1_s_021"
    s "Just as I thought... There really is someone collapsed... I wonder if she is okay... wait—huh, hey!?"

    voice "ch1_l_020"
    l "Seriously, Saito! What are you doing leaving your master behind?! ...Wait, there really is someone collapsed..."

    voice "ch1_l_021"
    l "This girl... she's wearing such unfamiliar clothes. Just what country could she be from, I wonder?"

    th "That blazer she's wearing... now that I look closer, isn't that the uniform from the school I used to go to?"
    th "Why is this girl wearing these clothes? Could it be... she's from Japan too, just like me...?"
    th "No, no... this girl... It’s like I’ve met her somewhere before..."
    th "Where, exactly? Back at my school in Japan?"
    th "I remember now. No doubt about it. She’s \"Haruna Takana\", our class representative...?"
    th "No, wait... Get a grip, me. What the hell is Takana-san doing in this world?"

    voice "ch1_l_022"
    l "Hey, Saito. What's with you staring at this girl so intently?"

    voice "ch1_s_022"
    s "Ah, uh—my bad, my bad. First things first, I should help her out..."

    voice "ch1_s_023"
    s "First, check pulse and heartbeat..., loosen her clothes to keep the airway clear..."

    # !!!
    #play sound "audio/sfx/punch.ogg"
    #scene cg ha_forest at bg_center with hit_shake

    $ shake_scene(effect="shake", sound="punch")
    pause(0.5)

    voice "ch1_l_023"
    l "Saito, what do you think you're doing?! Trying to take off a girl's clothes?!"

    voice "ch1_s_024"
    s "Huh!? I-It's a misunderstanding! I was just trying to take care of this girl!"

    voice "ch1_l_024"
    l "It doesn't look that way at all! I'll examine her myself, so you just go away!"

    voice "ch1_s_025"
    s "...Yeah, yeah."

    voice "ch1_l_025"
    l "It looks like she's just unconscious. No head trauma... Saito, hurry and head to the academy!"

    # !!! Эээ - сайто
    voice "ch1_s_026"
    s "Eh?"

    voice "ch1_l_026"
    l "No time for 'Eh?' — we can't exactly drag an unconscious person along, can we?"

    voice "ch1_l_027"
    l "I meant we should call for reinforcements! Surely you don't need me to spell out every last detail before you get it, right?"

    voice "ch1_s_027"
    s "Ah, yeah... You're right."

    th "There's a lot I want to ask... but first things first — her condition."

    # ==== SUBCHAPTER 3 ====

    $ fade_clear("bg forest", new_music="t17")

    $ show_sprites("mage")
    voice "ch1_mage_001"
    mage "So there you are."

    $ show_sprites(("mage", "s 1 angry"))

    #show mage at slide_center_to_left #slide_center_to_left
    #pause(0.2)
    #show s 1 angry at slide_center_to_right with dissolve #slide_center_to_right
    # !!! удивление вздох - сайто
    voice "ch1_s_028"
    s "Gah?!"

    $ show_sprites(("mage", "l 1 angry"))

    #hide s with dissolve
    #pause(0.2)
    #show l 1 angry at slide_center_to_right with dissolve
    voice "ch1_l_028"
    l "What?! Who are you people?!"

    voice "ch1_mage_002"
    mage "Hand over that girl."


    $ show_sprites(("mage", "s 1 angry"))
    voice "ch1_s_029"
    s "Who are you people? Do you know this girl?"

    voice "ch1_mage_003"
    mage "You have no need to know. Leave quietly, and we'll spare your lives."

    voice "ch1_s_030"
    s "What did you just say?!"

    window hide

    # ==== CHOISE 2 ====
    $ choise_result = None
    $ louise = "l 1 angry"
    menu:
        "Let me think for a moment.":
            $ choise_result = "neutral"
        "Like hell I'd do that!":
            $ choise_result = "good"
        "Alright... I'll hand her over.":
            $ choise_result = "bad" 

    if choise_result == "good":
        voice "ch1_s_036"
        s "Like hell I can do that! You just pop out of nowhere, dressed all suspiciously — did you really think I'd just hand her over without a second thought?!"
        
        $ louise = "l 1 sad"
        $ show_sprites((louise, "s 1 angry"))
        voice "ch1_l_031"
        l "Saito..."
        pause(1)

        window hide
        $ update_sympathy(20)
    elif choise_result == "neutral": 
        $ show_sprites(("mage", "s 1 sad"))

        voice "ch1_s_031"
        s "W-wait... let me think for a moment."

        $ louise = "l 1 angry"
        $ show_sprites((louise, "s 1 sad"))
        
        voice "ch1_l_029"
        l "What are you even thinking about?! This is obviously a 'no way' situation, got it?!"

        $ show_sprites((louise, "s 3 sad"))

        voice "ch1_s_032"
        s "Ah, yeah... You're right.{#var_2}"

    elif choise_result == "bad":
        voice "ch1_s_037"
        $ show_sprites(("mage", "s 1 sad"))

        s "Understood. You can have this girl."
        
        $ show_sprites(("l 3 angry", "s 1 sad"))

        voice "ch1_l_032"
        l "Wait, Saito! You can't possibly mean you're going to entrust this girl to these suspicious strangers we know nothing about?!"
        
        window hide
        $ update_sympathy(-20)

        $ show_sprites(("l 3 angry", "s 3 sad"))

        voice "ch1_s_038"
        s "Huh? Ah, no... Um, well, you see... I was just testing them, okay?!"

        $ louise = "l 1"
        $ show_sprites(("l 1", "s 3 sad"))
        voice "ch1_l_033"
        l "Is that so...?"

    
    $ show_sprites((louise, "s 1 angry"))    

    voice "ch1_s_033"
    s "Hey, you guys! Listen up good."

    voice "ch1_s_034"
    s "I'm not handing this girl over to you. Leave — now!"

    $ show_sprites((louise, "d 1 happy", "s 1 angry"), center_front=True)    
    voice "ch1_d_007"
    d "Heh heh heh... That's what I like to see, partner! Thought my edge'd never see action again."

    $ show_sprites(("mage", "d 1", "s 1 angry"))    
    voice "ch1_mage_004"
    mage "Hmph... How foolish. A mere commoner dares to stand in our way? Very well — then you shall receive a fitting recompense."

    # !!! звук доставания меча
    $ show_sprites(("mage", "s 7 angry"))    
    voice "ch1_s_035"
    s "Louise! I'm counting on you!"

    $ show_sprites(("l 2 angry", "s 7 angry")) 
    voice "ch1_l_030"
    l "I know! Getting dragged into something like this... Saito, you're going to pay for this later!"

    th "Like hell I'd give this important clue to getting back to Japan to these sketchy characters!"

    voice "ch1_d_008"
    d "Seems like the other side's fixin' to act, partner."  

    # call screen battle_menu

    # ==== BATTLE ==== 

    $ clear_chars()
    #call forest_battle from _call_forest_battle

    # ==== SUBCHAPTER 4 ====

    $ fade_clear("bg forest", new_music="t24")
    $ show_sprites(("mage", "s 1 angry"), anim="dissolve") 

    voice "ch1_mage_005"
    mage "To think I'd struggle against such a little girl and a commoner... Retreat!"

    voice "ch1_s_039"
    s "Hey, wait! Don't you run away!"

    $ flash_clear("bg forest")
    $ show_sprites(("s 1 angry"), anim="dissolve", side="right") 

    # !!! Сайто восклицает э VOICE_ID.BIN_00002A44.wav
    voice "ch1_s_063"
    s "Ah!?"

    $ show_sprites(("d 1 angry", "s 1 angry")) 
    voice "ch1_d_009"
    d "Hey now. They've escaped."

    $ show_sprites(("l 3 angry", "d 1 angry", "s 1 angry")) 

    voice "ch1_l_034"
    l "As if I'd let them get away! We're pursuing them, Saito!"

    $ show_sprites(("l 3 angry", "d 1", "s 1 angry"), center_front=True) 
    voice "ch1_d_010"
    d "Hey, hold on, cool it."

    $ show_sprites(("l 3 angry", "d 1", "s 1 angry")) 
    voice "ch1_l_035"
    l "Hey, are you really planning to just leave them alone?"

    $ show_sprites(("l 3 angry", "d 1 happy", "s 1 angry"), center_front=True) 
    voice "ch1_d_011"
    d "If we go charging after them without thinking and they've got reinforcements waiting, we could end up on the receiving end. Let's call it good that we scared them off and leave it at that."

    # Луиза на первый план
    $ show_sprites(("l 1 sad", "d 1 happy", "s 1 angry"))
    voice "ch1_l_036"
    l "...Well, I suppose you might be right. But still, something about this just doesn't sit right with me."

    $ fade_clear("cg ha_forest")

    voice "ch1_s_040"
    s "There, there. But more importantly, I think what we really need here is artificial respiration..."

    voice "ch1_l_037"
    l "You're so persistent!"

    # !!!
    #play sound "audio/sfx/punch.ogg"
    $ shake_scene(effect="shake", sound="punch")
    scene cg ha_forest at bg_center with hit_shake
    pause(0.5)

    voice "ch1_s_041"
    s "Ooow! My head hurts like hell, like it's about to burst!"

    voice "ch1_l_038"
    l "If you try that again, I really will break (your head). Anyway, Saito, what do we do now?"

    $ fade_clear("bg forest")
    $ show_sprites(("l 1 sad", "s 1 angry"), anim="dissolve")

    voice "ch1_s_042"
    s "Huh? What do you mean, 'what do we do?'... About what, exactly?"

    voice "ch1_s_043"
    l "If those guys were targeting her for a reason, then she's not just an ordinary girl, right? It's not certain that we can handle this on our own."

    $ show_sprites(("l 3 sad", "s 1 angry"))
    voice "ch1_l_039"
    l "There's also the option of heading back to town once and asking them to put this girl under protection, right?"

    $ show_sprites(("l 3 sad", "d 1", "s 1 angry"))
    voice "ch1_d_012"
    d "Well, that's the common-sense judgment, I suppose."

    $ show_sprites(("l 3 sad", "s 1 angry"))
    voice "ch1_s_044"
    s "N-no, we can't! We can't just abandon this girl halfway!"

    voice "ch1_l_040"
    l "...Why do you care so much about her, anyway?"

    pause(0.2)
    $ show_sprites(("l 3 sad", "s 3 sad"))
    pause(0.2)
    voice "ch1_s_045"
    s "W-well, that's... Once we've gotten involved, it's only right to see things through to the end and take care of her, isn't it?"

    th "Besides, who knows... maybe this could give me a clue on how to get back to Japan."

    $ show_sprites(("l 3 angry", "s 3 sad"))
    voice "ch1_l_041"
    l "Something's fishy here! Saito, spill it — what have you done to her?!"

    $ show_sprites(("l 3 angry", "s 3 angry"))
    voice "ch1_s_046"
    s "N-no, hold on! What are you even saying I did to this girl we just found a moment ago?!"

    $ show_sprites(("l 1 angry", "s 3 angry"))
    voice "ch1_l_042"
    l "You've known her for five minutes and you're already acting like this! She's got a big chest — which is exactly what you like — AND black hair just like Siesta's! Coincidence? I think not!"    
    
    voice "ch1_s_047"
    s "Uh! If you put it that way... I suppose you're right."

    $ show_sprites(("l 3 angry", "s 3 angry"))
    voice "ch1_l_043"
    l "Alright, spill it! What exactly have you done to her, huh?!"

    # ==== CHOISE 3 ==== 
    $ choise_result = None
    menu:
        "I don't recall":
            $ choise_result = "bad"
        "I didn't do anything!":
            $ choise_result = "good"

    if choise_result == "bad":
        $ show_sprites(("l 3 angry", "s 3 happy"))
        voice "ch1_s_048"
        s "I have absolutely no recollection of that. No, truly. Seriously!"
        $ show_sprites(("l 1 angry", "s 3 happy"))
        voice "ch1_l_044"
        l "...It's exactly that way of speaking that makes me unable to trust you. You don't even intend to answer seriously, do you? Is that how it is?"
        $ update_sympathy(-20)

        $ show_sprites(("l 1 angry", "s 3"))
        voice "ch1_s_049"
        s "No, wait, really! I'm telling you, I'm not lying! Please calm down, Louise-san."

        voice "ch1_l_045"
        l "No arguments!"
        
        # !!!
        play sound punch

        # ! поправить , сейчас все спрайты пропадают
        $ shake_scene(effect="shake", sound="punch")
        $ show_sprites(("l 1 angry", "s 3 angry"), anim=None)
        voice "ch1_s_050"
        s "Nooooooo!"

        voice "ch1_l_046"
        l "Haa... haa... haa..."
        $ show_sprites(("l 1 angry", "d 1 happy", "s 3 angry"))
        voice "ch1_d_013"
        d "...Haa. Hey, you still alive there, partner?"

        $ show_sprites(("l 1 angry", "d 1", "s 1 sad"))
        voice "ch1_s_051"
        s "...I'm dead."

        $ show_sprites(("l 1", "s 1 sad"))
        voice "ch1_l_047"
        l "Oh well, it's fine. I was planning to do that anyway, so let's just take her to the academy for now."

        voice "ch1_s_052"
        s "...Please."

        $ show_sprites(("l 3 angry", "s 1 sad"))
        voice "ch1_l_048"
        l "It's not like I'm doing this for you, you know. If you so much as lay a finger on this girl, I won't hold back next time — got it?"

        $ show_sprites(("l 3 angry", "s 3 sad"))
        pause(0.2)
        voice "ch1_s_053"
        s "I'm telling you, it's a misunderstanding!"

    if choise_result == "good":
        $ show_sprites(("l 3 angry", "s 3 angry"))
        voice "ch1_s_056"
        s "I didn't do anything! This girl — I swear, I just met her for the first time!"

        $ show_sprites(("l 3 sad", "s 3 angry"))
        voice "ch1_l_053"
        l "...Really? Then why are you so eager about it, hmm?"

        $ show_sprites(("l 3 sad", "s 1"))
        voice "ch1_s_057"
        s "This girl... she really reminds me of a classmate from my hometown."
        voice "ch1_s_058"
        s "So basically... if this isn't just some crazy person's prank, then..."

        $ show_sprites(("l 3 sad", "s 1 sad"))
        voice "ch1_s_059"
        s "There's a chance she holds a key to my world... that's what I'm thinking."

        pause(0.2)
        $ show_sprites(("l 1 sad", "s 1 sad"))
        voice "ch1_l_054"
        l "Ah..."

        ## тут 3 раза подряд если повысили то уже максимум должен быть
        $ update_sympathy(20)
        $ show_sprites(("l 1 sad", "s 1 angry"))
        voice "ch1_s_060"
        s "I want any clue I can get to return to my original world. ...Ah, but of course, it's also true that I really do want to help her. That part's completely genuine."

        voice "ch1_l_055"
        l "..."

        $ show_sprites(("l 1 sad", "s 1"))
        voice "ch1_s_061"
        s "It's the honest-to-god truth."

        $ show_sprites(("l 1 angry", "s 1"))
        voice "ch1_l_056"
        l "Ugh, fine, I get it! I was planning to do that anyway, so let's just take her to the Academy for now."

        voice "ch1_s_062"
        s "I'm sorry to ask, but... please."


    $ show_sprites(("l 1", "s 1"))
    voice "ch1_l_049"
    l "Those people from earlier might attack again, so I'm putting this girl on my horse. I'll move the luggage attached here over to your side, alright?"

    
    # !!! Если ответ положительный то вместо хаи он охает
    if choise_result == "good":
        #! звука нет
        voice "ch1_s_063"
        s "Yeah."
    if choise_result == "bad":
        voice "ch1_s_054"
        s "...Alright..."

    voice "ch1_l_050"
    l "But, I know the circumstances are... well, complicated. Still, just letting a commoner into the academy on our own — if the teachers find out, that could be real trouble, probably."

    voice "ch1_l_051"
    l "She does need treatment, but... I wonder what we should do about it."

    voice "ch1_s_055"
    s "About that... let's think it over once we get back."

    voice "ch1_l_052"
    l "Honestly... why am I the one stuck doing this...?"

    window hide
    $ fade_clear(stop_music=True)

    jump ch1_2

    return
```

## Файл: `chapters\1\script-ch1_2.rpy`

```renpy
# siesta's room night
label ch1_2:
    window hide
    call overlay_screen("yard_night",  "Tristain Academy of Magic") from _call_overlay_screen_6
    pause(2)
    $ fade_clear("cg ha_sick", new_music="t28")

    th "In the end, Siesta kindly let us keep the girl we'd brought back hidden in her room."
    th "Since calling a doctor was out of the question, we decided to have Montmorency examine her."

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

    th "Montmorency is Louise's classmate. She specializes in water magic. Her nickname is \"Montmorency the Fragrance.\""
    th "I call her Monmon, but she doesn't seem too fond of the nickname"

    $ show_sprites(("m 1", "s 1 sad"))

    voice "ch1.2_s_003"
    s "Ah, yeah. But seriously, thanks."

    voice "ch1.2_m_004"
    m "You're welcome. It's not like I'm under any obligation to do this, but I simply can't abandon someone who's sick."

    $ show_sprites(("l 1", "s 1 sad"))
    voice "ch1.2_l_001"
    l "Anyway, Siesta. I apologize for dragging a sick person into the room without warning."

    $ show_sprites(("l 1", "si 1"))

    voice "ch1.2_si_01"
    si "Oh, it's quite alright. Please don't worry about it, Miss Vallière. After all, it's for the sake of helping someone in need."

    $ show_sprites(("si 1"), mode="big")
    
    th "Siesta is a maid working at this academy. She feels a sense of kinship with me since we're both commoners."
    th "She's kind, great at cooking... I wish my master would take a page out of her book."

    $ show_sprites(("l 1", "si 1"))
    $ show_sprites(("l 1", "si 4 shy"))

    voice "ch1.2_si_02"
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
            $ show_sprites(("l 3", "s 3 happy"))
            voice "ch1.2_s_005"
            s "Um... Louise, what was our story again?"

            voice "ch1.2_l_004"
            l "Um, th-that's right! I met her today when I went out to town. Apparently, she's a commoner from my hometown!"

            $ update_sympathy(20)

            voice "ch1.2_l_005"
            l "She said her purse was stolen on the way and she had nowhere to go, so I thought I'd take her in for a while."

            $ show_sprites(("m 4 sad", "s 3 happy"))

            voice "ch1.2_m_008"
            m "Hmm... Well, she certainly does look terribly exhausted. If that's the case, I suppose it can't be helped."

            th "Nice one, Louise!"
            
        "Try to cover it up yourself":
            $ show_sprites(("l 3", "s 3 sad"))
            voice "ch1.2_s_007"
            s "Um, um, y-yeah, that's right! I ran into her in town, and she looked like she was going through a lot, so I just brought her along!"

            $ update_sympathy(-20)

            $ show_sprites(("m 1 sad", "s 3 sad"))
            voice "ch1.2_m_014"
            m "Is that so? But bringing a commoner along so suddenly like that is quite improper, you know."

            $ show_sprites(("m 1 sad", "s 3 happy"))
            voice "ch1.2_s_011"
            s "Hahaha. I'm such a naughty boy, huh..."

            $ show_sprites(("m 4 sad", "s 3 happy"))
            voice "ch1.2_m_015"
            m "...Well, I'll do you the favor of just leaving it at that."
            

        "Blame it on Siesta":
            voice "ch1.2_s_006"
            s "Um... Siesta, what was our story again?"

            $ show_sprites(("si 1 angry", "s 3 sad"))
            voice "ch1.2_si_03"
            si "Um, y-yes, that's right! She's a distant relative from my home village."

            $ update_sympathy(20, char_key="siesta")
            # не показывается ui сердце
            $ show_sprites(("si 1", "s 3 sad"))
            voice "ch1.2_si_04"
            si "She ran away from home, so I figured I'd let her stay for a few days."


            $ show_sprites(("m 4 angry", "s 3 sad"))
            voice "ch1.2_m_016"
            m "Hmm... Well, I suppose you're right. You two do have the exact same eye color and everything. If she really is a relative, then I suppose it can't be helped."

            $ show_sprites(("m 4 angry", "s 3 happy"))

            th "Thank you, Siesta!"
            
    # continue
    voice "ch1.2_m_009"
    m "For now, just let her get some rest. I doubt her condition will change anytime soon, but let me know if anything happens."

    $ show_sprites(("m 4 sad", "s 1"))

    voice "ch1.2_s_008"
    s "Yeah. I owe you one, Monmon."

    $ show_sprites(("m 1 angry", "s 1"))
    voice "ch1.2_m_010"
    m "I told you, it's Montmorency!"

    $ show_sprites(("m 1", "s 1"))
    voice "ch1.2_s_009"
    s "So... I have a favor to ask"

    voice "ch1.2_m_011"
    m "What is it?"

    $ show_sprites(("m 1", "s 3 sad"))
    voice "ch1.2_s_010"
    s "Actually, I'd like to keep her presence here a secret from the others at the academy."

    $ show_sprites(("m 1 angry", "s 3 sad"))
    voice "ch1.2_m_012"
    m "A secret? Why should I have to promise you anything?!"

    $ show_sprites(("m 1 angry", "l 3 sad"))
    voice "ch1.2_l_006"
    l "Montmorency, I'm asking you too... could you please keep this a secret?"

    $ show_sprites(("m 1", "l 3 sad"))

    voice "ch1.2_m_013"
    m "...Well, fine. I'll keep your secret. Now then, I'm heading back to my room."

    $ show_sprites(("si 1", "l 3 sad"))
    voice "ch1.2_si_05"
    si "That's a relief. Saito-san, Miss Variere"

    $ show_sprites(("si 1", "s 3"))
    voice "ch1.2_s_012"
    s "Well, at least her life isn't in danger, right? That's a relief."

    th "But could she really be Takanagi-san? If that's the case... how did she end up in this world..."
    th "Well, once she wakes up, I'll be able to figure everything out..."

    $ show_sprites(("l 1 sad", "s 3"))
    voice "ch1.2_l_007"
    l "Now we just have to hope she wakes up... I wonder what we should do?"

    $ show_sprites(("si 1", "s 3"))
    voice "ch1.2_si_06"
    si "I'll stay here and look after her. You two should get some rest now."

    voice "ch1.2_s_013"
    s "Is that so? Sorry about that, Siesta. I'm causing you a lot of trouble."

    $ show_sprites(("l 1 sad", "s 3"))
    voice "ch1.2_l_008"
    l "Really, I know I'm causing you extra trouble because of Saito, but I'm counting on you."

    $ show_sprites(("si 4 shy", "s 3"))
    voice "ch1.2_si_07"
    si "It's really no trouble at all. I'm just glad I can be of help to Saito-san."

    $ show_sprites(("si 4 shy", "s 3 shy"))
    voice "ch1.2_s_014"
    s "Huh? Ah, th-thanks..."

    $ show_sprites(("l 1 angry", "s 3 shy"))
    voice "ch1.2_l_009"
    l "Come on, Saito! Siesta went out of her way to be nice about it, so we're heading back to the room!"

    ## тряска и персонажи исчезают
    $ shake_scene(effect="shake")
    $ clear_chars(anim="slide", direction="slide_right")
    #$ show_sprites((None, None))

    voice "ch1.2_s_015"
    s "Hey, wait! Don't pull me so hard! Ow, ow, ow! I said it hurts!"

    ## затухание
    ## сцена с луной 

    jump ch1_3
    return
        



```

## Файл: `chapters\1\script-ch1_3.rpy`

```renpy
# hallway night
label ch1_3:
    $ fade_clear("sky_night", new_music="t19")
    th "Phew... what a crazy day..."
    $ fade_clear("hallway_night")

    $ show_sprites(("s 3 sad"))
    th "Maybe I should go somewhere before going to bed?"

    $ fade_clear("hallway_night", new_music="t3")
    $ show_sprites(("si 1"), side="right")
    ## меню выбора особое, выбор слева а персонаж справа к кому идем 
    ## музыка t3.ogg

    menu:
        "Siesta's Room":
            call si_room_ch1_3
        "Louise's Room":
            call l_room_ch1_3
        "Hallway": ## Тут спрайт монморанси
            call hallway_ch1_3

    #Варианты выбора (куда пойти перед сном):
    #Комната Сиесты (シエスタの部屋)
    #Комната Луизы (ルイズの部屋)
    #Коридор (廊下)

    jump ch1_4
    return


label si_room_ch1_3:
    $ fade_clear("hallway_night", new_music="t6")
    $ show_sprites(("s 1"))
    #! звук стука

    # ! сиеста да
    voice "ch1.3_si_001"
    si "Yes?"

    voice "ch1.3_s_019"
    s "Ah, Siesta? It's me... mind if I come in?"

    voice "ch1.3_si_002"
    si "Ah, Saito-san? Please, come in."

    # звук открытия двери и сайто уходит вправо
    $ clear_chars()
    pause(1.0)
    
    $ fade_clear("si_room_night")
    pause(1.0)
    # звук закрытия двери
    $ show_sprites(("si 1", "s 1"))
    voice "ch1.3_si_003"
    si "What's the matter, Saito? Did you happen to forget something, perhaps?"

    voice "ch1.3_s_020"
    s "No, not really... I just felt like dropping by, I guess."

    $ show_sprites(("si 1", "s 3"))
    voice "ch1.3_s_021"
    s "I just wanted to drop by one last time before bed, that's all. Hope I'm not bothering you?"

    $ show_sprites(("si 1 shy", "s 3"))
    voice "ch1.3_si_004"
    si "Oh, no, not at all! I could never think of you as a bother. I... well, actually, you are more than welcome."

    $ update_sympathy(20, char_key="siesta")
    
    voice "ch1.3_s_022"
    s "R-really? But I'm sorry about that... dropping a sick person on you so suddenly and all."

    $ show_sprites(("si 1", "s 3"))
    voice "ch1.3_si_005"
    si "No, please don't worry about that. We help each other out in times of need. Besides, I'm worried too, since she still hasn't woken up."

    voice "ch1.3_si_006"
    si "I'll nurse her whenever I have a free moment from my chores. So please, Saito-san, just go to sleep and don't worry about a thing."

    $ show_sprites(("si 1", "s 1"))
    voice "ch1.3_s_023"
    s "Got it. Thank you, Siesta."

    voice "ch1.3_si_007"
    si "Oh, geez. I've told you time and time again, but please don't worry about it at all, okay?"

    voice "ch1.3_s_024"
    s "Yeah. But I just really felt like I had to thank you, you know?"

    $ show_sprites(("si 1 happy", "s 1"))
    voice "ch1.3_si_008"
    si "...Hehe."

    $ show_sprites(("si 1", "s 1"))
    voice "ch1.3_si_009"
    si "But... This person's hair and skin color. They're the same as Saito-san's and mine, aren't they?"

    voice "ch1.3_s_025"
    s "Yeah..."

    voice "ch1.3_si_010"
    si "This is just my imagination... but is this person from the same country as Saito-san and my great-grandfather?"

    voice "ch1.3_s_026"
    s "That is..."

    menu:
        "You might be right.":
            voice "ch1.3_s_027"
            s "Probably, that might be the case. But you won't know the details unless you ask the person themselves."

            voice "ch1.3_si_011"
            si "Is that so... Someone from the same country as Saito-san... Then, Saito-san must be curious too, right?"

            $ update_sympathy(20, char_key="siesta")
            $ update_sympathy(-20, char_key="louise")

            $ show_sprites(("si 1", "s 3 sad"))
            voice "ch1.3_s_028"
            s "Eh? W-well, yeah."

            voice "ch1.3_s_029"
            s "But right now, I have no idea what's going on at all."

            voice "ch1.3_si_012"
            si "I suppose so."
        #neutral
        "I doubt it's just a coincidence.":
            $ show_sprites(("si 1", "s 3 sad"))
            voice "ch1.3_s_035"
            s "I don't think it's a coincidence. I doubt there are many people in the same circumstances as me."

            voice "ch1.3_si_018"
            si "I suppose so."
        "I don't really know.{var2}":
            voice "ch1.3_s_036"
            s "I wonder... I don't really understand it myself either."

            $ show_sprites(("si 1 sad", "s 1"))
            voice "ch1.3_si_019"
            si "Is that so?"

            $ update_sympathy(-20, char_key="siesta")
            $ update_sympathy(20, char_key="louise")

            $ show_sprites(("si 1 sad", "s 3 sad"))
            voice "ch1.3_s_037"
            s "Just like Siesta, there's also the possibility that their grandfather or father was from the same country as me. But you won't know unless you ask."

            $ show_sprites(("si 1", "s 3 sad"))
            voice "ch1.3_si_020"
            si "Ah, you're right."


    voice "ch1.3_si_013"
    si "This hair color and skin color. And also, the clothes from Saito-san's hometown..."

    $ show_sprites(("si 1 sad", "s 3 sad"))
    voice "ch1.3_si_014"
    si "...That's a bit too much of a coincidence to just be a coincidence, don't you think?"

    $ show_sprites(("si 1 sad", "s 1"))
    voice "ch1.3_s_030"
    s "Yeah. Maybe. But I don't want to get my hopes up just to be let down."

    voice "ch1.3_si_015"
    si "I thought so... You still want to keep hoping, don't you?"

    voice "ch1.3_s_031"
    s "W-well, I guess. It could be the lead I need to get back to my own world."

    voice "ch1.3_si_016"
    si "Your original world... is that so?"

    
    $ show_sprites(("si 1 sad", "s 3 sad"))
    voice "ch1.3_s_032"
    s "Ah, oh no. Is it already this late?"

    $ show_sprites(("si 1 sad", "s 3"))
    voice "ch1.3_s_033"
    s "Sorry for showing up so late. Anyway, see you tomorrow."

    $ show_sprites(("si 1", "s 3"))
    voice "ch1.3_si_017"
    si "Ah, right. Good night, Saito-san."

    voice "ch1.3_s_034"
    s "Ah, good night, Siesta."

    $ clear_chars(direction="right", anim="slide_right")
    #! персонажи в одну сторону уходят. звук открытия и закрытия двери
    pause(1.0)
    $ fade_clear("si_room_night")

    return
label l_room_ch1_3:
    $ fade_clear("louise_room_night", new_music="t5")

    $ show_sprites(("s 1"))
    voice "ch1.3_s_038"
    s "Phew, good grief."

    $ show_sprites(("l 1 angry", "s 1"))
    $ update_sympathy(20)

    voice "ch1.3_l_001"
    l "No 'good grief' for you. You'll rest when you finish your work!"
    
    $ show_sprites(("l 1 angry", "s 3 angry"))
    voice "ch1.3_s_039"
    s "What!? That's not fair, wifey!?"

    voice "ch1.3_l_002"
    l "Who are you calling wifey!"

    voice "ch1.3_l_003"
    l "Did you do the laundry? Did you clean your room? Did you put away the things you bought?"

    $ show_sprites(("l 1 angry", "s 1 angry"))
    voice "ch1.3_s_040"
    s "Ah, geez, don't dump it all on me at once! I can't possibly finish that many chores in one go."

    $ show_sprites(("l 3 angry", "s 1 angry"))
    voice "ch1.3_l_004"
    l "Then stop talking and get to work! No rest until you're done!"

    $ show_sprites(("l 3 angry", "s 3 sad"))
    voice "ch1.3_s_041"
    s "Huh?{#eee}"

    voice "Do you have any complaints!?"
    l "ch1.3_l_005"

    $ show_sprites(("l 3 angry", "s 1 sad"))
    voice "ch1.3_s_042"
    s "...Alright, alright."

    # ! возможно этот диалог потому что он признался что девушку взял потому что похожа на одноклассницу
    $ show_sprites(("l 1 sad", "s 1 sad"))
    voice "ch1.3_l_006"
    l "..."

    voice "ch1.3_s_043"
    s "...Louise? What's wrong?"

    voice "ch1.3_l_007"
    l "Um... um, you know? I was just wondering if I could ask you something."

    $ show_sprites(("l 1 sad", "s 1"))
    voice "ch1.3_s_044"
    s "What is it?"

    voice "ch1.3_l_008"
    l "Saito... Do you... want to go back home? To your world?"

    $ show_sprites(("l 1 sad", "s 3 sad"))
    s "Huh...?"

    menu:
        "Yeah, I want to go back.":
            $ show_sprites(("l 1 sad", "s 3"))
            voice "ch1.3_s_045"
            s "Ah, I really want to go home. I don't know when that'll be, but I'm definitely going back. That's my main goal right now, after all."

            voice "ch1.3_l_009"
            l " ...Yes. That's right, isn't it... As I thought."

            $ show_sprites(("l 1 sad", "s 1"))
            voice "ch1.3_s_046"
            s "What's wrong with that?"

            voice "ch1.3_l_010"
            l "It's nothing!"

        "I've already forgotten about my world.":
            $ show_sprites(("l 1 sad", "s 1"))
            voice "ch1.3_s_049"
            s "I've already forgotten about my original world. This place is my home now."

            $ show_sprites(("l 3", "s 1"))
            voice "ch1.3_l_013"
            l "...Liar."

            $update_sympathy(-20)
            $ show_sprites(("l 3", "s 3 angry"))
            voice "ch1.3_s_050"
            s "What's with that? I thought you were gonna ask me a question, but instead you're calling me a liar."

            voice "ch1.3_l_014"
            l "Saying you don't want to go back to your original world is obviously a lie."
            $ show_sprites(("l 3", "s 3 sad"))
            voice "ch1.3_s_051"
            s "...That is, well..."

            voice "ch1.3_l_015"
            l "You shouldn't tell such transparent lies. You realize how disrespectful that is, right?"

            $ show_sprites(("l 3", "s 1 sad"))
            voice "ch1.3_s_052"
            s "...Sorry."

            $ show_sprites(("l 1", "s 1 sad"))
            voice "ch1.3_l_016"
            l "Just forget it."

        "I don't really know.":
            voice "ch1.3_s_053"
            s "«I don't really know right now. I mean, of course I want to go back, but..."

            voice "ch1.3_l_017"
            l "But?"

            $ show_sprites(("l 1 sad", "s 3 happy"))
            voice "ch1.3_s_054"
            s "Looks like I've already finished everything I was supposed to do in this world."

            $ show_sprites(("l 1 sad", "s 1"))
            voice "ch1.3_s_055"
            s "Honestly, I don't know if it's right to just abandon everything here and go back."

            $ show_sprites(("l 1", "s 1"))
            voice "ch1.3_l_018"
            l "Hmm.."

            $update_sympathy(20)

            
    $ show_sprites(("l 3", "s 1"))
    voice "ch1.3_l_011"
    l "Right then. You still have business to attend to, so hurry up and get to it!"

    $ show_sprites(("l 3", "s 1 angry"))
    voice "ch1.3_s_047"
    s "Wh-what the hell! Then don't talk to me!"

    $ show_sprites(("l 3 angry", "s 1 angry"))
    voice "ch1.3_l_012"
    l "Shut up, shut up! Hurry up and do your work!"

    $ show_sprites(("l 3 angry", "s 3"))
    voice "ch1.3_s_048"
    s "Yeah, yeah."

    $ clear_chars(direction="right", anim="slide_right")

    return
label hallway_ch1_3:
    $ fade_clear("hallway_down_night", new_music="t28")
    $ show_sprites(("m 1"))
    voice "ch1.3_m_001"
    m "Oh? What are you doing in a place like this?"

    $ show_sprites(("m 1", "s 1"))
    voice "ch1.3_s_001"
    s "Huh? Mont... morency."

    $ show_sprites(("m 1 angry", "s 1"))
    voice "ch1.3_m_002"
    m "That awkward pause just now is bugging me a little, but... whatever. What are you doing here at this hour? You're going to have Louise kicking up a fuss again."

    voice "ch1.3_s_002"
    s "Hmm, well, I just thought I'd take a stroll around here, that's all."

    $ show_sprites(("m 1", "s 1"))    
    voice "ch1.3_m_003"
    m "Hmm.."

    $ show_sprites(("m 1", "s 1 happy"))
    voice "ch1.3_s_003"
    s "Anyway, thanks a lot for earlier."

    voice "ch1.3_m_004"
    m "It's no big deal. You don't need to be so grateful, you know."

    voice "ch1.3_m_005"
    m "Commoner or noble, I'd never abandon someone who's sick."

    $ show_sprites(("m 1", "s 1"))
    voice "ch1.3_s_004"
    s "Yeah, well, that's true, but..."

    $ show_sprites(("m 1 happy", "s 1"))
    voice "ch1.3_m_006"
    m "Oh my?"

    $ show_sprites(("m 1 happy", "s 3 sad"))
    voice "ch1.3_s_005"
    s "W-what is it...? What's with that oddly amused look in your eyes?"

    voice "ch1.3_m_007"
    m "Saito. You... don't tell me you've fallen for that girl?"

    $ show_sprites(("m 1 happy", "s 3 shy"))
    voice "ch1.3_s_006"
    s "Eh!?"

    menu:
        "How did you know!?{var1}":
            voice "ch1.3_s_008"
            s "How did you know!?{var1}"

            $ show_sprites(("m 1 shy", "s 3 shy"))
            voice "ch1.3_m_008"
            m "Oh my? So it really was true? I was just trying to fish for a reaction..."
            $ update_sympathy(-20)

            $ show_sprites(("m 1 shy", "s 3"))
            voice "ch1.3_s_009"
            s "No, no, it's just a joke. We just met today, so there's no way that's true, right?"

            $ show_sprites(("m 4", "s 3"))
            voice "ch1.3_m_009"
            m "My, my, my. I wonder if that's really true?"

            $ show_sprites(("m 4", "s 1 angry"))
            voice "ch1.3_s_010"
            s "Yeah, it's got absolutely nothing to do with it."

        "Why do you think that?":
            $ show_sprites(("m 1 shy", "s 3 sad"))
            voice "ch1.3_s_016"
            s "Why would you think that? I just happened to save that girl who collapsed on the road, that's all, right?"  

            $ show_sprites(("m 1 sad", "s 3 sad"))  
            voice "ch1.3_m_016"
            m "I wonder if it was really just a coincidence? Or did you actually arrange it all beforehand and stage a little play to get her into the academy... or something?"

            voice "ch1.3_s_017"
            s "Why would I go through all that trouble? Besides, Louise would be totally against it, right?"

            $ show_sprites(("m 4 sad", "s 3 sad"))
            voice "ch1.3_m_017"
            m "Hmmm?"

            $ show_sprites(("m 4 sad", "s 1 angry"))
            voice "ch1.3_s_018"
            s "Just believe me!"

        "Th-there's no way that's true, right?":
            voice "ch1.3_s_007"
            s "T-there's no way that's true, right?"

            $ show_sprites(("m 1 sad", "s 3 shy"))
            voice "ch1.3_m_014"
            m "Oh my? Am I wrong? My instincts are usually pretty good, though... Or maybe you have a crush on Louise?"

            $ update_sympathy(20)
            $ show_sprites(("m 1 sad", "s 3 sad"))
            voice "ch1.3_s_014"
            s "N-no, I'm telling you, that's not it! And it's not like that with Louise either, I swear!"

            $ show_sprites(("m 4", "s 3 sad"))
            voice "ch1.3_m_015"
            m "Oh my? Then... that maid?"

            $ show_sprites(("m 4", "s 1 angry"))
            voice "ch1.3_s_015"
            s "Thaaat's wroong tooo!"

    $ show_sprites(("m 4 happy", "s 1 angry"))
    voice "ch1.3_m_010"
    m "Hmph. Well, I think I'll let it slide for today."

    $ show_sprites(("m 4 happy", "s 3 sad"))
    voice "ch1.3_s_011"
    s "It's the 'for today...' part that's oddly terrifying, though."

    $ show_sprites(("m 1", "s 3 sad"))
    voice "ch1.3_m_011"
    m "Don't sweat the small stuff. I know it's hard to believe, but I can keep a secret, you know?"

    voice "ch1.3_m_012"
    m "I'll keep quiet about that girl, too. You can rest assured of that."

    $ show_sprites(("m 1", "s 1 sad"))
    voice "ch1.3_s_012"
    s "I'm trusting you here! Please, don't let me down!"

    voice "ch1.3_m_013"
    m "Alright, alright. Well then, I'm heading back to my room. Good night, sleep well."

    $ show_sprites(("s 3 sad"))
    voice "ch1.3_s_013"
    s "Phew, what a relief. But... I wonder if it's really going to be okay..."
                
    return
```

## Файл: `chapters\1\script-ch1_4.rpy`

```renpy
# louise's room night
label ch1_4:
    $ fade_clear("louise_room_night", new_music="t19")
    $ show_sprites(("s 5"))
    voice "ch1.4_s_001"
    s "Well then, I guess I'll call it a night."

    ## ! возможно тут диалог начинается в зависимости от симпатии луизы (но он начался когда симпатия была -20)
    $ show_sprites(("l 4", "s 5"))
    voice "ch1.4_l_001"
    l "Hey, Saito. What are you doing over there in the corner of the room?"

    voice "ch1.4_s_002"
    s "Huh? I mean, my sleeping spot is just straw on the floor..."

    $ show_sprites(("l 4 shy", "s 5"))
    voice "ch1.4_l_002"
    l "I-if you don't mind taking the corner, I'll let you sleep in my bed with me!"

    voice "ch1.4_s_003"
    s "Huh...? Are you sure?"

    $ show_sprites(("l 4 angry", "s 5"))
    voice "ch1.4_l_003"
    l "Of course! I said so, didn't I? Hurry up and get in bed already!"

    $ show_sprites(("l 4 angry", "s 6 sad"))
    voice "ch1.4_s_004"
    s "Ah... ahh... yeah."

    # sitos dreams
    th "When I was first summoned, I was told, 'Because you're a familiar,' and had to sleep on a pile of straw... and to think how things have changed..."
    th "To think I'm actually sharing a bed with Louise!"
    th "Does this mean she's secretly into me, even just a little? Or is it the exact opposite... and I'm completely out of the running?"
    th "... But whatever. Being able to sleep in a warm bed is just pure bliss, yeah."

    voice "ch1.4_l_004"
    l "What are you muttering about? Come on, hurry up and go to sleep!"

    voice "ch1.4_s_005"
    s "Y-yeah."

    # ! оба уходят в одну сторону
    $ clear_chars(anim="slide", direction="slide_right")
    pause(2)

    voice "ch1.4_l_005"
    l "Hey... stop squirming around so much."

    voice "ch1.4_s_006"
    s "Ah, sorry."

    voice "ch1.4_l_006"
    l "It's nothing... I don't mind if you move a little, though."

    voice "ch1.4_s_007"
    s "It's just that I can see the moon really well from this angle... I just couldn't help myself."

    voice "ch1.4_l_007"
    l "W-what's with you...? You're suddenly saying all these weird things."

    show bg sky_night at bg_center with dissolve
    voice "ch1.4_s_008"
    s "Louise. There are two moons in this world, aren't there?"

    voice "ch1.4_l_008"
    l "Obviously. You don't need to state the obvious."

    voice "ch1.4_s_009"
    s "Yeah, I guess. To you, it's just completely normal, huh."

    voice "ch1.4_l_009"
    l "Geez... you're such a weirdo."

    th "Yeah. It might be completely normal for Louise, but for me... two moons is anything but ordinary."
    th "It really hits me all over again... this truly is another world."
    th "And now a classmate has actually appeared in this other world... What on earth is going on...?"

    voice "ch1.4_s_010"
    s "..."

    voice "ch1.4_l_010"
    l "...Hey, Saito...? You still up?"

    voice "ch1.4_s_011"
    s "Zzz..."

    voice "ch1.4_l_011"
    l "Are you asleep...?"

    voice "ch1.4_l_012"
    l "...Geez! Fine then! I'm going to sleep too!"

    jump ch1_5
    
    return
```

## Файл: `chapters\1\script-ch1_5.rpy`

```renpy
# morning
label ch1_5:
    $ fade_clear("sky", new_music="t4")
    voice "ch1.5_s_001"
    s "Hmm... {i}yawns{/i}. It's already morning, huh... I wonder what time it is?"

    voice "ch1.5_s_002"
    s "I'd better get everything ready for washing up before Louise wakes up... {i}yawns{/i}."

    voice "ch1.5_s_003"
    s "Ah... But this bed, which I haven't slept in for a long time, is so comfortable... I can't get up..."

    $ fade_clear("louise_room")
    # стук

    voice "ch1.5_s_004"
    s "Huh...?{#ha}" 

    voice "ch1.5_si_001"
    si "Good morning, Saito-san. Good morning, Miss Vallière."

    voice "ch1.5_s_005"
    s "Eh, Siesta?"

    th "Wait, I'm still sleeping in the same bed as Louise!!"

    voice "ch1.5_si_002"
    si "I'm sorry to bother you so early in the morning, but actually, about last night..."

    $ fade_clear("si_wakeup", new_music="t29")
    pause(2)
    voice "ch1.5_si_003"
    si "..."

    voice "ch1.5_s_006"
    s "Ah... G-good morning... Siesta..."

    voice "ch1.5_si_004"
    si "You two... in the same bed..."

    voice "ch1.5_s_007"
    s "Ah, no, wait!"

    voice "ch1.5_s_008"
    s "I don't know what kind of misunderstanding you've got, but there's no romance, no 'moe' moments, or anything like that you're imagining."

    voice "ch1.5_s_009"
    s "It's hard to sleep on the straw that is technically my proper bed, right?"

    voice "ch1.5_s_010"
    s "Then my master told me to get into the corner of the bed, so I just did what I was told..."

    voice "ch1.5_s_011"
    s "See, if I don't obey, I'll get punished, you know."

    voice "ch1.5_s_012"
    s "So I was like, 'this is annoying,' but I still got into the same bed anyway. Just thinking to myself, 'man, this is a pain...' or whatever."

    pause(1)
    show cg si_wakeup at bg_center

    voice "ch1.5_si_005"
    si "...Is that so?"

    th "S-scary... It's terrifying how she's still smiling..."

    voice "ch1.5_si_006"
    si "I get all that. But then, what about that hand tightly gripping your clothes, Saito-san?"

    voice "ch1.5_s_013"
    s "Eh!?{#e}"
    
    th "W-w-why the hell is Louise sleeping while holding onto my clothes!?"

    voice "ch1.5_s_014"
    s "Th-th-this!"

    voice "ch1.5_si_007"
    si "Yes?"

    voice "ch1.5_s_015"
    s "Well, the thing is..."

    $ result = None
    menu:
        "Louise is just half-asleep!":
            voice "ch1.5_s_016"
            s "That Louise is just half-asleep and clinging to me..."

            voice "ch1.5_s_017"
            s "If this keeps up, I might be stuck in bed for the rest of my life, hehe... Or so I could say... How does that sound?"

            voice "ch1.5_si_008"
            si "That must be a dreadful situation."

            voice "ch1.5_si_009"
            si "How on earth did he manage to catch the attention of that Miss Vallière... I'm quite curious."

            voice "ch1.5_s_018"
            s "S-Siesta..."

            voice "ch1.5_l_001"
            l "Mmm..."

            voice "ch1.5_s_019"
            s "Ah, looks like Louise is waking up."

            voice "ch1.5_l_002"
            l "Mmm... {i}yaaaawn{/i}... Huh, Saito...?"
        
        "We need a witness's testimony here!":
            $ result = 'TESTIMONY!!!'

            voice "ch1.5_s_021"
            s "At this juncture, it is my intention to prove my innocence through the testimony of a third party!"

            voice "ch1.5_si_012"
            si "A third party...? But currently, there is no one else in this room besides Saito-san, myself, and Miss Vallière."

            voice "ch1.5_s_022"
            s "I have my partner with me! Hey, Derf!"

            voice "ch1.5_d_001"
            d "What's up, partner? What do you need from me this early in the morning?"

            voice "ch1.5_d_002"
            d "Hold on, what's going on here? Sneaking around with a village girl in a noble's bedroom? You're as reckless as ever, partner."

            voice "ch1.5_si_013"
            si "W-What!? No, I'm not mentally ready for something like that!"

            $ update_sympathy(20, char_key="siesta")
            $ update_sympathy(-20, char_key="louise")

            voice "ch1.5_s_023"
            s "That's not it! Don't say things that will be completely misunderstood!"

            voice "ch1.5_d_003"
            d "Tch, what a drag. Anyway, what do you really need?"

            voice "ch1.5_s_024"
            s "You've been keeping an eye on everything in this room the whole time, haven't you?"

            voice "ch1.5_d_004"
            d "Yeah, I suppose."

            voice "ch1.5_s_025"
            s "Sorry to ask, but could you vouch for my innocence to Siesta?"

            voice "ch1.5_d_005"
            d "Eh?{#e?}"

            voice "ch1.5_s_026"
            s "I'm begging you. My honor is on the line."

            voice "ch1.5_d_006"
            d "My, my. You're as stubbornly by-the-book as always, partner. Oh well, whatever."

            voice "ch1.5_d_007"
            d "The noble girl gave my partner permission to use the bed."

            voice "ch1.5_d_008"
            d "She told him he could share the bed as long as he stuck to the corner. And I ain't making this up."

            voice "ch1.5_si_014"
            si "...Is that really true?"

            voice "ch1.5_s_037"
            s "Yes, yes! It's the truth, so please, try to believe me!"

            voice "ch1.5_d_009"
            d "Well, naturally. Though what dirty thoughts my partner had when he got into that bed is none of my business."

            voice "ch1.5_s_027"
            s "Like I said! Stop adding unnecessary commentary!"

            voice "ch1.5_l_001-2"
            l "Mmm..."

            voice "ch1.5_s_028"
            s "Huh? Louise, did you wake up?"

            voice "ch1.5_l_005"
            l "{i}Yawns{/i}... Ugh, you're so noisy first thing in the morning, Saito. Now I've ended up waking up because of you..."

        "I'll wake up Louise and let her explain it herself.":
            $ result = "WAKE UP!"

            voice "ch1.5_s_029"
            s "Uh, um. In a situation like this, rather than me saying it, it's probably better to let Louise herself explain it, yeah."

            voice "ch1.5_s_030"
            s "Hey, Louise, Louise! I'm begging you, wake up and explain this situation!  Or rather, prove my innocence!"

            voice "ch1.5_l_006"
            l "Mmm... mm..."

            voice "ch1.5_s_031"
            s "Louise! Come on, wake up!"

            voice "ch1.5_l_007"
            l "Mmm..."

            voice "ch1.5_si_016"
            si "!!!!!"

            $ update_sympathy(-20, char_key="siesta")
            $ update_sympathy(20, char_key="louise")

            voice "ch1.5_s_032"
            s "Lu-, Louise!? Wait a minute, there's a limit to sleep-hugging! Don't cling to me, don't squeeze me!"

            voice "ch1.5_si_017"
            si "Sa... Saito-san..."

            voice "ch1.5_s_033"
            s "!!!!! Wait, Siesta, I swear it's a misunderstanding!"

            voice "ch1.5_si_018"
            si "To think that you and Miss Vallière had become that close... I had no idea at all."

            th "What am I supposed to do now!?"

            voice "ch1.5_l_002-2"
            l "Mmm... {i}Yawns{/i}... Huh, Saito...?"

    $ fade_clear("louise_room")
    pause(1)

    if result == "WAKE UP!":
        $ show_sprites(("l 4 angry", "s 5 sad"))
        voice "ch1.5_l_008"
        l "...Wait, huh!? Why are you clinging to me!?"

        voice "ch1.5_s_034"
        s "Wha-!? N-No, that's wro...!"

        #! звук удара, тряска и вспышка долгая
        $ shake_scene(sound="audio/sfx/punch.ogg", effect="flash", clear=True)
        $ show_sprites(("s 5 sad", "s 1 sad"), anim="dissolve")

        voice "ch1.5_s_035"
        s "A-Anyway, at least my name has been cleared, right?"

        voice "ch1.5_si_019"
        si "Y-Yes... I sincerely apologize for having doubted you."

        $ show_sprites(("l 4 angry", "s 1 sad"))
        voice "ch1.5_l_009"
        l "Geez, that's fine now, whatever! More importantly, why is Siesta in my room!?"
    else:
        $ show_sprites(("l 4 angry", "s 5"))
        pause(0.5)

        if result == 'TESTIMONY!!!':
            voice "ch1.5_l_003-2"
        else:
            voice "ch1.5_l_003"
        l "Wait... wha-!? Why is Siesta in my room!?"

    th "Come to think of it, I wonder why Siesta came at this time?"

    $ show_sprites(("l 4 angry", "si 1"))
    voice "ch1.5_si_010"
    si "Yes. I came regarding that girl."

    $ show_sprites(("s 5 angry", "si 1"))
    s "Eh?{#e?}"

    voice "ch1.5_si_011"
    si "That girl woke up just now. So, I thought I should come and inform Saito-san and Miss Vallière..."

    $ show_sprites(("s 5 happy", "si 1"))
    voice "ch1.5_s_036"
    s "Really!? Got it, I'll go right away!"

    $ show_sprites(("l 4 angry", "si 1"))
    voice "ch1.5_l_010"
    l "Eh, ah, wait a sec, Saito!? Wait until I get changed!!"

    $ show_sprites(("l 4 angry", "si 1 angry"))
    voice "ch1.5_si_020"
    si "Ah, Saito-san. Please wait!"

    # ! оба уходят в одну сторону
    $ clear_chars(anim="slide", direction="slide_right")

    jump ch1_6
    return
```

## Файл: `chapters\1\script-ch1_6.rpy`

```renpy
label ch1_6:
    $ fade_clear("si_room", new_music="t18")
    $ show_sprites(("h 1 sad", "s 1"))

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

    #! тут кирхе с сайто вправо перемещаются а потом через правый слайд также появляются новые персы
    $ show_sprites(("t 1", "m 1"))
    t "..."

    voice "ch1.6_m_001"
    m "Umm... Ah, right, right. Looks like she's doing well now."

    # слайд вправо
    $ show_sprites(("l 3 angry", "s 3 sad"))
    voice "ch1.6_l_001"
    l "Why have so many people gathered here since this morning!"

    # слайд вправо
    $ show_sprites(("k 1", "t 1"))
    th "Kirche and Tabitha are Louise's classmates, having arrived as exchange students from Germania and Gallia, respectively."

    $ show_sprites(("k 1"), mode="big")
    th "Kirche excels in the fire element of magic. She is known as 'Kirche the Ardent'."
    th "She and Louise are simply on bad terms because of some ongoing friction over family lineage or place of origin."
    
    $ show_sprites(("t 1"), mode="big")
    th "Tabitha excels in the wind element of magic. She is known as 'Tabitha the Snowstorm'."
    th "Always taciturn and devoid of expression. What goes on in her mind is a mystery. Yet, she and Kirche are surprisingly close..."
    
    $ show_sprites(("k 1, t 1"))
    th "Kirche being curious is one thing, but it's rare for Tabitha, who is always quietly reading a book, to actually show up."
    th "I wonder why they came here..."

    menu:
        "Ask Tabitha":
            $ show_sprites(("s 3 sad, t 1"))
            voice "ch1.6_s_007-2"
            s "Hey, Tabitha. Why are you here?"

        "Ask Siesta":
            $ show_sprites(("si 1 sad, s 3 sad"))
            voice "ch1.6_s_007-3"
            s "Hey, Siesta. Why are there so many people here?"

        "Ask Louise":
            $ show_sprites(("l 3 angry, s 3 sad"))
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

            $ show_sprites(("l 3, s 3 sad"))
            voice "ch1.6_l_004"
            l  "Tell me, Siesta. It wasn't this bustling before you came to fetch us, was it?"

        "Ask Kirche":
            $ show_sprites(("k1, s 3 sad"))
            voice "ch1.6_s_007"
            s "Hey, Kirche. Why are you here?"



```

## Файл: `characters.rpy`

```renpy
define s = Character(_("Saito"), color="#3874a3")
define l = Character(_("Louise"), color="#fd7589")
define k = Character(_("Kirche"), color="#e36566")
define t = Character(_("Tabitha"), color="#b4dfec")
define c = Character(_("Kolbert"), color="#5e5b51")
define h = Character(_("Henrietta"), color="#782163")
define si = Character(_("Siesta"), color="#535a6a")
define ha = Character(_("Haruna"), color="#4b4d51")
define g = Character(_("Guiche"), color="#f3e69d")
define d = Character(_("Derflinger"), color="#9d996b")
define o = Character(_("Osmond"), color="#ddd7d4")
define m = Character(_("Montmorency"), color="#e2d79d")
define npc1 = Character(_("Сommander"), color="#797979")
define npc2 = Character(_("Soldier"), color="#797979")
define mage = Character(_("Mage"), color="#d82b2b")

define unknown = Character(_("???"), color="#000000") #protagonist
define unk_h = Character(_("???"), color="#4b4d51") # haruna
define unk_k = Character(_("???"), color="#e36566") #kirche

define th = Character(None, 
    what_italic=True,
    what_color="#3874a3",
    window_style='thought_window'
)






# define tiffania = Character(_("Тиффания"), color="#fec979")
# define agnes = Character(_("Агнес"), color="#ede2ba")

```

## Файл: `definitions.rpy`

```renpy
init python:
    import os
    
    def get_localized_path(path):
        base, ext = os.path.splitext(path)

        if _preferences.language == "japanese": 
            localized = f"{base}_jp{ext}"
        elif _preferences.language == "russian":
            localized = f"{base}_ru{ext}"
            
        if renpy.loadable(localized):
            return localized
        return path


default chapter = 0


# ==== POSITIONS ====

# bg position
transform bg_center: 
    zoom 0.85
    xalign 0.5
    yalign 0.5

# chara position
transform normal_center:
    zoom 0.55  
    xalign 0.5
    yalign 1.0

transform normal_right:
    zoom 0.55     
    xalign 1.2  
    yalign 1.0    

transform normal_left:
    zoom 0.55 
    xalign -0.2
    yalign 1.0        

transform close_center:
    zoom 0.70  
    xalign 0.5
    yalign 0.15

transform close_left_npc:
    zoom 0.60 
    xalign -0.3
    yalign 1.0        

transform close_right_npc:
    zoom 0.60 
    xalign 1.9
    yalign 0.95    

# ==== TRANSITIONS ====
define flash = Fade(0.1, 0.5, 0.5, color="#fff")
define fade = Fade(0.5, 0.0, 0.5)

# slide
transform slide_left_out_generic:
    yalign 1.0 zoom 0.55 alpha 1.0
    ease 0.4 xalign -0.3 alpha 0

transform slide_right_out_generic:
    yalign 1.0 zoom 0.55 alpha 1.0
    ease 0.4 xalign 1.3 alpha 0

# === LEFT SLIDES ===
transform slide_left_in:
    xalign -0.3 yalign 1.0 zoom 0.55 alpha 0.1
    ease 0.4 xalign 0.05 alpha 1.0

transform slide_left_out:
    xalign 0.05 yalign 1.0 zoom 0.55 alpha 1.0
    ease 0.4 xalign -0.3 alpha 0

transform slide_left_to_center_in:
    xalign -0.3 yalign 1.0 zoom 0.55 alpha 0.1
    ease 0.4 xalign 0.5 alpha 1.0    

# === RIGHT SLIDES ===
transform slide_right_in:
    xalign 1.3 yalign 1.0 zoom 0.55 alpha 0.1
    ease 0.4 xalign 0.95 alpha 1.0

transform slide_right_out:
    xalign 0.95 yalign 1.0 zoom 0.55 alpha 1.0
    ease 0.4 xalign 1.3 alpha 0

transform slide_center_to_right_out:
    xalign 0.5 yalign 1.0 zoom 0.55 alpha 1.0
    ease 0.4 xalign 1.3 alpha 0  

# === CENTER TO SIDE SLIDES ===
transform slide_center_to_left:
    xalign 0.5 yalign 1.0 zoom 0.55 alpha 1.0
    ease 0.4 xalign -0.2 alpha 1.0

transform slide_center_to_right:
    xalign 0.5 yalign 1.0 zoom 0.55 alpha 1.0
    ease 0.4 xalign 1.2 alpha 1.0


# blow
transform explosion_shake(duration=0.4, *, old_widget=None, new_widget=None):
    delay duration
    xcenter 0.5
    ycenter 0.5

    old_widget
    events False
    linear 0.04 xoffset 32 yoffset 20
    linear 0.04 xoffset -26 yoffset -13
    linear 0.04 xoffset 16 yoffset 10
    linear 0.04 xoffset -8 yoffset -7
    linear 0.04 xoffset 0 yoffset 0

    new_widget
    events True

transform hit_shake(duration=0.2, strength=60, *, old_widget=None, new_widget=None):
    delay duration
    xcenter 0.5
    ycenter 0.5

    old_widget
    events False
    linear 0.03 xoffset strength yoffset (strength * 0.6)
    linear 0.17 xoffset 0 yoffset 0

    new_widget
    events True

# ==== IMAGES ====

image black = "#000"
image bg overlay = "bg/overlay.png"

# forest
image bg forest = "bg/forest.png"
image bg forest_evening = "bg/forest_evening.png"
image bg forest_night = "bg/forest_night.png"
image bg forest_blurred = "bg/forest_blurred.png"

# sky
image bg sky = "bg/sky.png"
image bg sky_night = "bg/sky_night.png"
image bg sky_evening = "bg/sky_evening.png"

# TOWN

# town_square
image bg town_square = "bg/town_square.png"
image bg town_square_evening = "bg/town_square_evening.png"
image bg town_square_night = "bg/town_square_night.png"
image bg town_square_ruined = "bg/town_square_ruined.png"
image bg town_square_night_blurred = "bg/town_square_night_blurred.png"

# town
image bg town = "bg/town.png"
image bg town_evening = "bg/town_evening.png"
image bg town_night = "bg/town_night.png"

# cafe
image bg cafe = "bg/cafe.png"
image bg cafe_evening = "bg/cafe_evening.png"
image bg cafe_night = "bg/cafe_night.png"

# cafe_entrance
image bg cafe_entrance = "bg/cafe_entrance.png"
image bg cafe_entrance_evening = "bg/cafe_entrance_evening.png"
image bg cafe_entrance_night = "bg/cafe_entrance_night.png"

# ACADEMY

# yard
image bg yard = "bg/yard.png"
image bg yard_evening = "bg/yard_evening.png"
image bg yard_night = "bg/yard_night.png"
image bg yard_night_blurred = "bg/yard_night_blurred.png"
image bg yard_ruined = "bg/yard_ruined.png"
image bg yard_ruined_evening = "bg/yard_ruined_evening.png"
image bg yard_ruined_night = "bg/yard_ruined_night.png"

# classroom
image bg classroom = "bg/classroom.png"
image bg classroom_evening = "bg/classroom_evening.png"
image bg classroom_night = "bg/classroom_night.png"

# kitchen
image bg kitchen = "bg/kitchen.png"
image bg kitchen_evening = "bg/kitchen_evening.png"
image bg kitchen_night = "bg/kitchen_night.png"

# osman cabinet
image bg osman_cabinet = "bg/osman_cabinet.png"
image bg osman_cabinet_evening = "bg/osman_cabinet_evening.png"
image bg osman_cabinet_night = "bg/osman_cabinet_night.png"

# library
image bg library = "bg/library.png"
image bg library_evening = "bg/library_evening.png"
image bg library_night = "bg/library_night.png"

# library_table
image bg library_table = "bg/library_table.png"
image bg library_table_evening = "bg/library_table_evening.png"
image bg library_table_night = "bg/library_table_night.png"

# siesta room
image bg si_room = "bg/si_room.png"
image bg si_room_evening = "bg/si_room_evening.png"
image bg si_room_night = "bg/si_room_night.png"

#hallway
image bg hallway = "bg/hallway.png"
image bg hallway_evening = "bg/hallway_evening.png"
image bg hallway_night = "bg/hallway_night.png"
#hallway_down
image bg hallway_down = "bg/hallway_down.png"
image bg hallway_down_evening = "bg/hallway_down_evening.png"
image bg hallway_down_night = "bg/hallway_down_night.png"

#louise_room
image bg louise_room = "bg/louise_room.png"
image bg louise_room_evening = "bg/louise_room_evening.png"
image bg louise_room_night = "bg/louise_room_night.png"


# ==== CG ==== 

image cg terrorist = "cg/terrorist.png"
image cg terrorist2 = "cg/terrorist2.png"
image cg terrorist3 = "cg/terrorist3.png"

image cg l_s_forest_l_speak = "cg/l_s_forest_l_speak.png"
image cg l_s_forest_l_s_speak = "cg/l_s_forest_l_s_speak.png"
image cg l_s_forest = "cg/l_s_forest.png"
image cg l_forest = "cg/l_forest.png"
image cg l_s_forest_s_speak = "cg/l_s_forest_s_speak.png"

image cg ha_forest = "cg/ha_forest.png"
image cg ha_forest_open = "cg/ha_forest_open.png"

image cg ha_sick = "cg/ha_sick.png"
image cg ha_sick_2 = "cg/ha_sick_2.png"
image cg ha_sick_3 = "cg/ha_sick_3.png"
image cg ha_sick_4 = "cg/ha_sick_4.png"
image cg ha_sick_5 = "cg/ha_sick_5.png"

image cg si_wakeup = "cg/si_wakeup.png"
image cg si_wakeup_2 = "cg/si_wakeup_2.png"

# ==== MUSIC ====
define audio.t1 = "audio/bgm/t1.ogg"
define audio.t2 = "audio/bgm/t2.ogg"
define audio.t3 = "audio/bgm/t3.ogg"
define audio.t4 = "audio/bgm/t4.ogg"
define audio.t5 = "audio/bgm/t5.ogg"
define audio.t6 = "audio/bgm/t6.ogg"
define audio.t7 = "audio/bgm/t7.ogg"
define audio.t8 = "audio/bgm/t8.ogg"
define audio.t9 = "audio/bgm/t9.ogg"
define audio.t10 = "audio/bgm/t10.ogg"
define audio.t11 = "audio/bgm/t11.ogg"
define audio.t12 = "audio/bgm/t12.ogg"
define audio.t13 = "audio/bgm/t13.ogg"
define audio.t14 = "audio/bgm/t14.ogg"
define audio.t15 = "audio/bgm/t15.ogg"
define audio.t16 = "audio/bgm/t16.ogg"
define audio.t17 = "audio/bgm/t17.ogg"
define audio.t18 = "audio/bgm/t18.ogg"
define audio.t19 = "audio/bgm/t19.ogg"
define audio.t20 = "audio/bgm/t20.ogg"
define audio.t21 = "audio/bgm/t21.ogg"
define audio.t22 = "audio/bgm/t22.ogg"
define audio.t23 = "audio/bgm/t23.ogg"
define audio.t24 = "audio/bgm/t24.ogg"
define audio.t25 = "audio/bgm/t25.ogg"
define audio.t26 = "audio/bgm/t26.ogg"
define audio.t27 = "audio/bgm/t27.ogg"
define audio.t28 = "audio/bgm/t28.ogg"
define audio.t29 = "audio/bgm/t29.ogg"
define audio.t30 = "audio/bgm/t30.ogg"
define audio.t31 = "audio/bgm/t31.ogg"
define audio.t32 = "audio/bgm/t32.ogg"

# ==== SOUNDS ====
define audio.blow = "audio/sfx/blow.wav"
define audio.punch = "audio/sfx/punch.wav"

```

## Файл: `gui.rpy`

```renpy
﻿################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(1920, 1080)

## Enable checks for invalid or unstable properties in screens or transforms
define config.check_conflicting_properties = True


################################################################################
## GUI Configuration Variables
################################################################################


## Colors ######################################################################
##
## The colors of text in the interface.

## An accent color used throughout the interface to label and highlight text.
define gui.accent_color = '#3874a3'

## The color used for a text button when it is neither selected nor hovered.
define gui.idle_color = '#2e3b6b'

## The small color is used for small text, which needs to be brighter/darker to
## achieve the same effect.
define gui.idle_small_color = '#132447'

## The color that is used for buttons and bars that are hovered.
define gui.hover_color = '#3874a3'

## The color used for a text button when it is selected but not focused. A
## button is selected if it is the current screen or preference value.
define gui.selected_color = '#3874a3'

## The color used for a text button when it cannot be selected.
define gui.insensitive_color = '#443e4a'

## Colors used for the portions of bars that are not filled in. These are not
## used directly, but are used when re-generating bar image files.
define gui.muted_color = '#e0a366'
define gui.hover_muted_color = '#eac199'

## The colors used for dialogue and menu choice text.
define gui.text_color = '#404040'
define gui.interface_text_color = '#404040'


## Fonts and Font Sizes ########################################################

## The font used for in-game text.
define gui.text_font = "DejaVuSans.ttf"

## The font used for character names.
define gui.name_text_font = "DejaVuSans.ttf"

## The font used for out-of-game text.
define gui.interface_text_font = "DejaVuSans.ttf"

## The size of normal dialogue text.
define gui.text_size = 32

## The size of character names.
define gui.name_text_size = 40

## The size of text in the game's user interface.
define gui.interface_text_size = 32

## The size of labels in the game's user interface.
define gui.label_text_size = 36

## The size of text on the notify screen.
define gui.notify_text_size = 24

## The size of the game's title.
define gui.title_text_size = 75


## Main and Game Menus #########################################################

## The images used for the main and game menus.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Dialogue ####################################################################
##
## These variables control how dialogue is displayed on the screen one line at a
## time.

## The height of the textbox containing dialogue.
define gui.textbox_height = 278

## The placement of the textbox vertically on the screen. 0.0 is the top, 0.5 is
## center, and 1.0 is the bottom.
define gui.textbox_yalign = 1.0


## The placement of the speaking character's name, relative to the textbox.
## These can be a whole number of pixels from the left or top, or 0.5 to center.
define gui.name_xpos = 0.5
#define gui.name_xpos = 0.25
define gui.name_ypos = 10

## The horizontal alignment of the character's name. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.name_xalign = 0.5


## The width, height, and borders of the box containing the character's name, or
## None to automatically size it.
define gui.namebox_width = None
define gui.namebox_height = None

## The borders of the box containing the character's name, in left, top, right,
## bottom order.
define gui.namebox_borders = Borders(100, 5, 100, 10)

## If True, the background of the namebox will be tiled, if False, the
## background of the namebox will be scaled.
define gui.namebox_tile = False


## The placement of dialogue relative to the textbox. These can be a whole
## number of pixels relative to the left or top side of the textbox, or 0.5 to
## center.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 70

## The maximum width of dialogue text, in pixels.
define gui.dialogue_width = 1116

## The horizontal alignment of the dialogue text. This can be 0.0 for left-
## aligned, 0.5 for centered, and 1.0 for right-aligned.
define gui.dialogue_text_xalign = 0.0


## Buttons #####################################################################
##
## These variables, along with the image files in gui/button, control aspects of
## how buttons are displayed.

## The width and height of a button, in pixels. If None, Ren'Py computes a size.
define gui.button_width = None
define gui.button_height = None

## The borders on each side of the button, in left, top, right, bottom order.
define gui.button_borders = Borders(6, 6, 6, 6)

## If True, the background image will be tiled. If False, the background image
## will be linearly scaled.
define gui.button_tile = False

## The font used by the button.
define gui.button_text_font = gui.interface_text_font

## The size of the text used by the button.
define gui.button_text_size = gui.interface_text_size

## The color of button text in various states.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## The horizontal alignment of the button text. (0.0 is left, 0.5 is center, 1.0
## is right).
define gui.button_text_xalign = 0.0


## These variables override settings for different kinds of buttons. Please see
## the gui documentation for the kinds of buttons available, and what each is
## used for.
##
## These customizations are used by the default interface:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 30
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## You can also add your own customizations, by adding properly-named variables.
## For example, you can uncomment the following line to set the width of a
## navigation button.

# define gui.navigation_button_width = 250


## Choice Buttons ##############################################################
##
## Choice buttons are used in the in-game menus.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#3874a3'
define gui.choice_button_text_hover_color = "#2e3b6b"
define gui.choice_button_text_insensitive_color = '#132447'


## File Slot Buttons ###########################################################
##
## A file slot button is a special kind of button. It contains a thumbnail
## image, and text describing the contents of the save slot. A save slot uses
## image files in gui/button, like the other kinds of buttons.

## The save slot button.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## The number of columns and rows in the grid of save slots.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Positioning and Spacing #####################################################
##
## These variables control the positioning and spacing of various user interface
## elements.

## The position of the left side of the navigation buttons, relative to the left
## side of the screen.
define gui.navigation_xpos = 60

## The vertical position of the skip indicator.
define gui.skip_ypos = 15

## The vertical position of the notify screen.
define gui.notify_ypos = 68

## The spacing between menu choices.
define gui.choice_spacing = 33

## Buttons in the navigation section of the main and game menus.
define gui.navigation_spacing = 6

## Controls the amount of spacing between preferences.
define gui.pref_spacing = 15

## Controls the amount of spacing between preference buttons.
define gui.pref_button_spacing = 0

## The spacing between file page buttons.
define gui.page_spacing = 0

## The spacing between file slots.
define gui.slot_spacing = 15

## The position of the main menu text.
define gui.main_menu_text_xalign = 1.0


## Frames ######################################################################
##
## These variables control the look of frames that can contain user interface
## components when an overlay or window is not present.

## Generic frames.
define gui.frame_borders = Borders(6, 6, 6, 6)

## The frame that is used as part of the confirm screen.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## The frame that is used as part of the skip screen.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## The frame that is used as part of the notify screen.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Should frame backgrounds be tiled?
define gui.frame_tile = False


## Bars, Scrollbars, and Sliders ###############################################
##
## These control the look and size of bars, scrollbars, and sliders.
##
## The default GUI only uses sliders and vertical scrollbars. All of the other
## bars are only used in creator-written screens.

## The height of horizontal bars, scrollbars, and sliders. The width of vertical
## bars, scrollbars, and sliders.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## True if bar images should be tiled. False if they should be linearly scaled.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Horizontal borders.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Vertical borders.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## What to do with unscrollable scrollbars in the game menu. "hide" hides them,
## while None shows them.
define gui.unscrollable = "hide"


## History #####################################################################
##
## The history screen displays dialogue that the player has already dismissed.

## The number of blocks of dialogue history Ren'Py will keep.
define config.history_length = 250

## The height of a history screen entry, or None to make the height variable at
## the cost of performance.
define gui.history_height = 210

## Additional space to add between history screen entries.
define gui.history_spacing = 0

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## NVL-Mode ####################################################################
##
## The NVL-mode screen displays the dialogue spoken by NVL-mode characters.

## The borders of the background of the NVL-mode background window.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## The maximum number of NVL-mode entries Ren'Py will display. When more entries
## than this are to be show, the oldest entry will be removed.
define gui.nvl_list_length = 6

## The height of an NVL-mode entry. Set this to None to have the entries
## dynamically adjust height.
define gui.nvl_height = 173

## The spacing between NVL-mode entries when gui.nvl_height is None, and between
## NVL-mode entries and an NVL-mode menu.
define gui.nvl_spacing = 15

## The position, width, and alignment of the label giving the name of the
## speaking character.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## The position, width, and alignment of the dialogue text.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## The position, width, and alignment of nvl_thought text (the text said by the
## nvl_narrator character.)
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## The position of nvl menu_buttons.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at https://
## www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Mobile devices
################################################################################

init python:

    ## This increases the size of the quick buttons to make them easier to touch
    ## on tablets and phones.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## This changes the size and spacing of various GUI elements to ensure they
    ## are easily visible on phones.
    @gui.variant
    def small():

        ## Font sizes.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Adjust the location of the textbox.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Change the size and spacing of various things.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## File button layout.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## NVL-mode.
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30

```

## Файл: `options.rpy`

```renpy
﻿define config.default_language = "english"

# ============================================
# УНИВЕРСАЛЬНЫЙ ШРИФТ С ПОДДЕРЖКОЙ CJK (японский, китайский, корейский)
# ============================================
# NotoSansCJK поддерживает все символы: латиницу, кириллицу, японский, китайский, корейский
define gui.cjk_font = "fonts/NotoSansCJK-Regular.ttc"

# ============================================
# ПРИМЕНЕНИЕ ШРИФТА КО ВСЕМ ЭЛЕМЕНТАМ GUI
# ============================================

# Основные текстовые элементы
define gui.text_font = "fonts/NotoSansCJK-Regular.ttc"
define gui.name_text_font = "fonts/NotoSansCJK-Regular.ttc"
define gui.interface_text_font = "fonts/NotoSansCJK-Regular.ttc"

# Кнопки и интерактивные элементы
define gui.button_text_font = "fonts/NotoSansCJK-Regular.ttc"
define gui.choice_button_text_font = "fonts/NotoSansCJK-Regular.ttc"

# Лейблы и поля ввода
define gui.label_text_font = "fonts/NotoSansCJK-Regular.ttc"
define gui.input_text_font = "fonts/NotoSansCJK-Regular.ttc"

# Слоты сохранения
define gui.slot_button_text_font = "fonts/NotoSansCJK-Regular.ttc"

# Навигация (меню)
define gui.navigation_button_text_font = "fonts/NotoSansCJK-Regular.ttc"

# ============================================
# СТИЛИ ПО УМОЛЧАНИЮ
# ============================================

style default:
    font "fonts/NotoSansCJK-Regular.ttc"

style button_text:
    font "fonts/NotoSansCJK-Regular.ttc"

style label_text:
    font "fonts/NotoSansCJK-Regular.ttc"

style input:
    font "fonts/NotoSansCJK-Regular.ttc"

style hyperlink_text:
    font "fonts/NotoSansCJK-Regular.ttc"

style prompt_text:
    font "fonts/NotoSansCJK-Regular.ttc"

style bar:
    font "fonts/NotoSansCJK-Regular.ttc"

style vbar:
    font "fonts/NotoSansCJK-Regular.ttc"

style scrollbar:
    font "fonts/NotoSansCJK-Regular.ttc"

style slider:
    font "fonts/NotoSansCJK-Regular.ttc"

# Навигационные кнопки (меню слева)
style navigation_button_text:
    font "fonts/NotoSansCJK-Regular.ttc"

# Радио-кнопки и чекбоксы
style radio_button_text:
    font "fonts/NotoSansCJK-Regular.ttc"

style check_button_text:
    font "fonts/NotoSansCJK-Regular.ttc"

# Превью сохранений
style slot_button_text:
    font "fonts/NotoSansCJK-Regular.ttc"

style slot_name_text:
    font "fonts/NotoSansCJK-Regular.ttc"

style slot_time_text:
    font "fonts/NotoSansCJK-Regular.ttc"

# Заголовки страниц меню
style page_label_text:
    font "fonts/NotoSansCJK-Regular.ttc"

# Текст в preferences/настройках
style pref_label_text:
    font "fonts/NotoSansCJK-Regular.ttc"

style pref_button_text:
    font "fonts/NotoSansCJK-Regular.ttc"

# Текст в истории
style history_name_text:
    font "fonts/NotoSansCJK-Regular.ttc"

style history_text:
    font "fonts/NotoSansCJK-Regular.ttc"

# Текст в about/информации
style about_text:
    font "fonts/NotoSansCJK-Regular.ttc"

# Текст подтверждения
style confirm_prompt_text:
    font "fonts/NotoSansCJK-Regular.ttc"

# Quick menu
style quick_button_text:
    font "fonts/NotoSansCJK-Regular.ttc"

# ============================================
# ФУНКЦИЯ ОБНОВЛЕНИЯ ШРИФТОВ (для динамической смены)
# ============================================

init -10 python:
    def update_ui_font():
        """Обновить все шрифты UI на текущий язык"""
        target_font = 'fonts/NotoSansCJK-Regular.ttc'
        
        # Устанавливаем шрифты для всех элементов GUI
        gui.text_font = target_font
        gui.name_text_font = target_font
        gui.interface_text_font = target_font
        gui.button_text_font = target_font
        gui.choice_button_text_font = target_font
        gui.label_text_font = target_font
        gui.input_text_font = target_font
        gui.slot_button_text_font = target_font
        gui.navigation_button_text_font = target_font
        
        # Устанавливаем шрифт по умолчанию для стилей
        style.default.font = target_font
        style.button_text.font = target_font
        style.label_text.font = target_font
        style.input.font = target_font
        style.prompt_text.font = target_font
        style.navigation_button_text.font = target_font
        style.radio_button_text.font = target_font
        style.check_button_text.font = target_font
        style.slot_button_text.font = target_font
        style.slot_name_text.font = target_font
        style.slot_time_text.font = target_font
        style.page_label_text.font = target_font
        style.pref_label_text.font = target_font
        style.pref_button_text.font = target_font
        style.history_name_text.font = target_font
        style.history_text.font = target_font
        style.about_text.font = target_font
        style.confirm_prompt_text.font = target_font
        style.quick_button_text.font = target_font
        
        # Перестраиваем стили для применения изменений
        style.rebuild()
        
        return target_font

# Инициализация шрифтов при запуске
init python:
    # Применяем шрифт при старте игры
    update_ui_font()

# ============================================
# ОСНОВНЫЕ НАСТРОЙКИ ИГРЫ
# ============================================

define build.name = "ZnT1"
define config.version = "0.0.2"
define config.name = _("Zero no Tsukaima: Shou-akuma to Harukaze no Concerto (Unnoficial remaster)")

define config.voice_filename_format = "audio/voices/{filename}.wav"

define gui.show_name = False

define config.developer = True

    # disable ctrl skip
    #define config.keymap['skip'] = []
    # disable rollback
    #define config.keymap['rollback'] = [] 
    #define config.rollback_enabled = False

# ============================================
# ЗВУК И МУЗЫКА
# ============================================

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.main_menu_music = audio.t2

# ============================================
# ПЕРЕХОДЫ
# ============================================

define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = None
define config.end_game_transition = None

# ============================================
# УПРАВЛЕНИЕ ОКНАМИ
# ============================================

define config.window = "auto"
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# ============================================
# НАСТРОЙКИ ПО УМОЛЧАНИЮ
# ============================================

default preferences.text_cps = 199
default preferences.afm_time = 15

# ============================================
# СБОРКА
# ============================================

define config.save_directory = "ZnT1-1777760105"
define config.window_icon = "gui/window_icon.png"

```

## Файл: `script.rpy`

```renpy
label intro:
    $ renpy.movie_cutscene("video/intro.webm")
    return

label splashscreen:
    scene black
    pause (0.5)
    scene disclaimer with fade
    pause(2)
    scene black with fade
    pause(1)
    call intro from _call_intro
    return       


label start:
    jump ch0

```

## Файл: `scripts\0_init\0_init_screens.rpy`

```renpy
################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





```

## Файл: `scripts\dialogue\choice_screen.rpy`

```renpy

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"
    

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


```

## Файл: `scripts\dialogue\confirm_screen.rpy`

```renpy

## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")



```

## Файл: `scripts\dialogue\input_screen.rpy`

```renpy
## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


```

## Файл: `scripts\dialogue\nvl_screen.rpy`

```renpy


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")
```

## Файл: `scripts\dialogue\say_screen.rpy`

```renpy
## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    #background Image("gui/textbox.png", xalign=0.5, yalign=1.0)
    background Transform("gui/textbox.png", alpha=0.8)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    #background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    background None
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5
    outlines [(0.1, "#000000", 0, 0)]

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

style choice_button_text:
    properties gui.button_text_properties("choice_button")

    


```

## Файл: `scripts\features\battle.rpy`

```renpy
# ============================================================================
# ZERO NO TSUKAIMA - BATTLE & INVENTORY SYSTEM
# Complete battle and inventory system in PS2 JRPG style
# ============================================================================

# ============================================================================
# GLOBAL VARIABLES
# ============================================================================

# Character states: "normal", "happy", "hurt"
default character_states = {}

# Current battle
default battle_active = False
default current_turn_index = 0
default battle_phase = "player"  # "player", "enemy", "victory", "defeat"
default selected_action = None
default selected_skill = None
default selected_target = None
default current_actor = None
default battle_message = ""
default battle_message_timer = 0

# AOE casting
default aoe_casting = {}  # {character_key: {"skill": skill, "turns_left": N}}

# Defense buffs
default defense_buffs = {}  # {character_key: {"value": 50, "turns": 2}}

# Enemies
default enemies = []

# Selected item
default selected_item = None
default item_target_selection = False

# Battle preparation selected character
default selected_character = None

# Inventory lock (True = items blocked from use)
default inventory_locked = False

# ============================================================================
# ITEM DATA (EXTENDED)
# ============================================================================

default curr_items = {
    "Bread": 3,
    "Herb": 3,
    "Elixir": 3,
    "Antidote": 2,
    "Phoenix Feather": 1,
}

init python:
    import random
    
    # Full item dictionary with actions
    items = {
        "Bread": {
            "name": "Bread",
            "description": "Restores 50 HP",
            "effect_type": "hp",
            "effect_value": 50,
            "animation": "heal",
            "sound": "audio/sfx/item_use.ogg"
        },
        "Herb": {
            "name": "Herb",
            "description": "Restores 30 MP",
            "effect_type": "mp",
            "effect_value": 30,
            "animation": "mp_restore",
            "sound": "audio/sfx/item_use.ogg"
        },
        "Elixir": {
            "name": "Elixir",
            "description": "Restores 100 HP and 50 MP",
            "effect_type": "both",
            "effect_hp": 100,
            "effect_mp": 50,
            "animation": "full_restore",
            "sound": "audio/sfx/elixir.ogg"
        },
        "Antidote": {
            "name": "Antidote",
            "description": "Cures poison status",
            "effect_type": "cure_poison",
            "animation": "cure",
            "sound": "audio/sfx/cure.ogg"
        },
        "Phoenix Feather": {
            "name": "Phoenix Feather",
            "description": "Revives fallen ally with 50% HP",
            "effect_type": "revive",
            "effect_value": 0.5,
            "animation": "revive",
            "sound": "audio/sfx/revive.ogg"
        }
    }
    
    def lock_inventory():
        """Locks inventory - items cannot be used"""
        store.inventory_locked = True
    
    def unlock_inventory():
        """Unlocks inventory - items can be used"""
        store.inventory_locked = False
    
    def can_use_item_on_target(item_name, target_key):
        """Checks if item can be used on target (checks HP/MP full status)"""
        if store.inventory_locked:
            return False
        
        if item_name not in items:
            return False
        
        target = store.party_characters.get(target_key)
        if not target:
            return False
        
        item = items[item_name]
        effect_type = item.get("effect_type", "")
        
        # Check if HP item can be used (not at full HP)
        if effect_type == "hp":
            if target.get('hp', 0) >= target.get('max_hp', 0):
                return False
        
        # Check if MP item can be used (not at full MP)
        elif effect_type == "mp":
            if target.get('mp', 0) >= target.get('max_mp', 0):
                return False
        
        # Check if both HP/MP item can be used
        elif effect_type == "both":
            hp_full = target.get('hp', 0) >= target.get('max_hp', 0)
            mp_full = target.get('mp', 0) >= target.get('max_mp', 0)
            if hp_full and mp_full:
                return False
        
        # Revive only works on dead characters
        elif effect_type == "revive":
            if target.get('hp', 0) > 0:
                return False
        
        # Cure poison only works on poisoned characters
        elif effect_type == "cure_poison":
            if 'status' not in target or 'poison' not in target.get('status', set()):
                return False
        
        return True

    def use_item(item_name, target_key):
        """Applies item to character"""
        if store.inventory_locked:
            return False
        
        if item_name not in store.curr_items or store.curr_items[item_name] <= 0:
            return False
        
        if item_name not in items:
            return False
        
        if not can_use_item_on_target(item_name, target_key):
            return False
            
        item = items[item_name]
        target = store.party_characters.get(target_key)
        
        if not target:
            return False
        
        # Apply effect
        effect_type = item.get("effect_type", "")
        
        if effect_type == "hp":
            value = item.get("effect_value", 0)
            target['hp'] = min(target['hp'] + value, target['max_hp'])
        elif effect_type == "mp":
            value = item.get("effect_value", 0)
            target['mp'] = min(target['mp'] + value, target['max_mp'])
        elif effect_type == "both":
            hp_val = item.get("effect_hp", 0)
            mp_val = item.get("effect_mp", 0)
            target['hp'] = min(target['hp'] + hp_val, target['max_hp'])
            target['mp'] = min(target['mp'] + mp_val, target['max_mp'])
        elif effect_type == "revive":
            if target['hp'] <= 0:
                ratio = item.get("effect_value", 0.5)
                target['hp'] = int(target['max_hp'] * ratio)
        elif effect_type == "cure_poison":
            if 'status' in target:
                target['status'].discard('poison')
        
        # Decrease quantity
        store.curr_items[item_name] -= 1
        if store.curr_items[item_name] <= 0:
            del store.curr_items[item_name]
        
        return True

    def get_party_members():
        """Returns list of party members"""
        return [(key, char) for key, char in store.party_characters.items()]

    def get_alive_party_members():
        """Returns alive party members"""
        return [(key, char) for key, char in store.party_characters.items() 
                if char.get('hp', 0) > 0]

    def get_alive_enemies():
        """Returns alive enemies"""
        return [e for e in store.enemies if e.get('hp', 0) > 0]
    
    def get_attack_type(char_data):
        """Returns attack type based on is_mage flag"""
        if char_data.get('is_mage', False):
            return "Magic"
        else:
            return "Attack"

# ============================================================================
# SKILL DATA (EXTENDED)
# ============================================================================

default skills = {
    # Louise skills
    "arrow": {
        "name": "Magic Arrow",
        "consume": 30,
        "description": "Attacks a single enemy with magic arrow",
        "damage": 40,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "void",
        "accuracy": 90,
        "animation": "magic_arrow"
    },
    "heroism": {
        "name": "Heroism",
        "consume": 50,
        "description": "Powerful attack on single enemy",
        "damage": 80,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "void",
        "accuracy": 85,
        "animation": "heroism"
    },
    "meteor": {
        "name": "Meteor",
        "consume": 70,
        "description": "Attacks ALL enemies with meteors",
        "damage": 60,
        "is_aoe": True,
        "cast_turns": 2,
        "element": "void",
        "accuracy": 80,
        "animation": "meteor"
    },
    "dispel": {
        "name": "Dispel Magic",
        "consume": 30,
        "description": "Increases ally accuracy",
        "is_buff": True,
        "buff_type": "accuracy",
        "buff_value": 20,
        "is_aoe": False,
        "cast_turns": 0,
        "animation": "buff"
    },
    "heal": {
        "name": "Heal",
        "consume": 30,
        "description": "Restores ally HP",
        "is_heal": True,
        "heal_value": 60,
        "is_aoe": False,
        "cast_turns": 0,
        "animation": "heal"
    },

    # Saito skills
    "slash": {
        "name": "Slash",
        "consume": 20,
        "description": "Basic sword attack",
        "damage": 35,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "physical",
        "accuracy": 95,
        "animation": "slash"
    },
    "d_slash": {
        "name": "Double Slash",
        "consume": 40,
        "description": "Double sword strike",
        "damage": 65,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "physical",
        "accuracy": 90,
        "animation": "double_slash"
    },
    "wind_moon_slash": {
        "name": "Wind Moon Slash",
        "consume": 70,
        "description": "Powerful attack on ALL enemies",
        "damage": 50,
        "is_aoe": True,
        "cast_turns": 2,
        "element": "wind",
        "accuracy": 85,
        "animation": "wind_slash"
    },

    # Tabitha skills (wind)
    "wing": {
        "name": "Wing",
        "consume": 30,
        "description": "Wind attack",
        "damage": 35,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "wind",
        "accuracy": 90,
        "animation": "wind"
    },
    "air_needle": {
        "name": "Air Needle",
        "consume": 50,
        "description": "Air needles attack",
        "damage": 55,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "wind",
        "accuracy": 88,
        "animation": "air_needle"
    },
    "wind_break": {
        "name": "Wind Break",
        "consume": 70,
        "description": "Hurricane on ALL enemies",
        "damage": 45,
        "is_aoe": True,
        "cast_turns": 2,
        "element": "wind",
        "accuracy": 82,
        "animation": "wind_storm"
    },
    "air_force": {
        "name": "Air Force",
        "consume": 30,
        "description": "Increases ally speed",
        "is_buff": True,
        "buff_type": "agility",
        "buff_value": 15,
        "is_aoe": False,
        "cast_turns": 0,
        "animation": "buff"
    },

    # Kirche skills (fire)
    "fire": {
        "name": "Fire",
        "consume": 30,
        "description": "Fire attack",
        "damage": 40,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "fire",
        "accuracy": 88,
        "animation": "fire"
    },
    "fire_needle": {
        "name": "Fire Needle",
        "consume": 50,
        "description": "Fire needles attack",
        "damage": 60,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "fire",
        "accuracy": 85,
        "animation": "fire_needle"
    },
    "fire_arrow": {
        "name": "Fire Arrow",
        "consume": 70,
        "description": "Fire storm on ALL enemies",
        "damage": 50,
        "is_aoe": True,
        "cast_turns": 2,
        "element": "fire",
        "accuracy": 80,
        "animation": "fire_storm"
    },
    "fire_shield": {
        "name": "Fire Shield",
        "consume": 30,
        "description": "Increases ally defense",
        "is_buff": True,
        "buff_type": "defense",
        "buff_value": 25,
        "is_aoe": False,
        "cast_turns": 0,
        "animation": "buff"
    },

    # Henrietta skills (water)
    "water": {
        "name": "Water",
        "consume": 30,
        "description": "Water attack",
        "damage": 38,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "water",
        "accuracy": 90,
        "animation": "water"
    },
    "water_needle": {
        "name": "Water Needle",
        "consume": 50,
        "description": "Water needles attack",
        "damage": 55,
        "is_aoe": False,
        "cast_turns": 0,
        "element": "water",
        "accuracy": 87,
        "animation": "water_needle"
    },
    "water_hazard": {
        "name": "Water Hazard",
        "consume": 70,
        "description": "Water storm on ALL enemies",
        "damage": 48,
        "is_aoe": True,
        "cast_turns": 2,
        "element": "water",
        "accuracy": 83,
        "animation": "water_storm"
    },
    "water_blade": {
        "name": "Water Blade",
        "consume": 30,
        "description": "Increases ally attack",
        "is_buff": True,
        "buff_type": "attack",
        "buff_value": 20,
        "is_aoe": False,
        "cast_turns": 0,
        "animation": "buff"
    }
}

# ============================================================================
# PARTY CHARACTERS - Only characters currently in party
# ============================================================================

default party_characters = {
    'saito': {
        'name': 'Saito',
        'description': "A Japanese boy who was summoned to this world by Louise.\nHe is treated as a familiar by Louise.", 
        "is_mage": False,
        "skills": ["slash", "d_slash", "wind_moon_slash"],
        'hp': 255,
        'max_hp': 255,
        'mp': 100,
        'max_mp': 100,
        'attack': 45,
        'defense': 30,
        'agility': 35,
        'accuracy': 95,
        'portrait': 'gui/portraits/s.png',
        'portrait_normal': 'gui/portraits/s.png',
        'portrait_happy': 'gui/portraits/s_happy.png',
        'portrait_hurt': 'gui/portraits/s_hurt.png',
        'cast_video': 'video/cast/saito_cast.webm',
        'state': 'normal',
        'cooldown': 0
    },
    'louise': {
        'name': 'Louise',
        "description": "The magician who summoned Saito.\nAlthough she can use Void magic,\nits true nature remains unknown.",
        "is_mage": True,
        "skills": ["arrow", "heroism", "dispel"],
        'hp': 200,
        'max_hp': 200,
        'mp': 150,
        'max_mp': 150,
        'attack': 25,
        'defense': 20,
        'agility': 30,
        'accuracy': 85,
        'portrait': 'gui/portraits/l.png',
        'portrait_normal': 'gui/portraits/l.png',
        'portrait_happy': 'gui/portraits/l_happy.png',
        'portrait_hurt': 'gui/portraits/l_hurt.png',
        'cast_video': 'video/cast/louise_cast.webm',
        'state': 'normal',
        'cooldown': 0
    }
}

# All characters data (for reference/adding to party)
default all_characters = {
    'saito': {
        'name': 'Saito',
        'description': "A Japanese boy who was summoned to this world by Louise.\nHe is treated as a familiar by Louise.", 
        "is_mage": False,
        "skills": ["slash", "d_slash", "wind_moon_slash"],
        'hp': 255,
        'max_hp': 255,
        'mp': 100,
        'max_mp': 100,
        'attack': 45,
        'defense': 30,
        'agility': 35,
        'accuracy': 95,
        'portrait': 'gui/portraits/s.png',
        'portrait_normal': 'gui/portraits/s.png',
        'portrait_happy': 'gui/portraits/s_happy.png',
        'portrait_hurt': 'gui/portraits/s_hurt.png',
        'cast_video': 'video/cast/saito_cast.webm',
        'state': 'normal',
        'cooldown': 0
    },
    'louise': {
        'name': 'Louise',
        "description": "The magician who summoned Saito.\nAlthough she can use Void magic,\nits true nature remains unknown.",
        "is_mage": True,
        "skills": ["arrow", "heroism", "dispel"],
        'hp': 200,
        'max_hp': 200,
        'mp': 150,
        'max_mp': 150,
        'attack': 25,
        'defense': 20,
        'agility': 30,
        'accuracy': 85,
        'portrait': 'gui/portraits/l.png',
        'portrait_normal': 'gui/portraits/l.png',
        'portrait_happy': 'gui/portraits/l_happy.png',
        'portrait_hurt': 'gui/portraits/l_hurt.png',
        'cast_video': 'video/cast/louise_cast.webm',
        'state': 'normal',
        'cooldown': 0
    },
    'siesta': {
        'name': 'Siesta',
        'portrait': 'gui/portraits/si.png',
        "skills": [],
        'description': "A maid working at Tristain Academy of Magic.\nSince she is a commoner, she cannot use magic.\nShe has feelings for Saito."
    },
    'tabitha': {
        'name': "Tabitha",
        "is_mage": True,
        'portrait': 'gui/portraits/t.png',
        'portrait_normal': 'gui/portraits/t.png',
        'portrait_happy': 'gui/portraits/t_happy.png',
        'portrait_hurt': 'gui/portraits/t_hurt.png',
        'description': "Louise's classmate.\nSpecializes in wind magic.\nHer nickname is \"Tabitha of the Snow Wind\".", 
        "skills": ["wing", "air_needle", "wind_break", "air_force", "heal"],
        'hp': 180,
        'max_hp': 180,
        'mp': 180,
        'max_mp': 180,
        'attack': 20,
        'defense': 18,
        'agility': 40,
        'accuracy': 90,
        'cast_video': 'video/cast/tabitha_cast.webm',
        'state': 'normal',
        'cooldown': 0
    },
    'kirche': {
        'name': "Kirche",
        "is_mage": True,
        'portrait': 'gui/portraits/k.png',
        'portrait_normal': 'gui/portraits/k.png',
        'portrait_happy': 'gui/portraits/k_happy.png',
        'portrait_hurt': 'gui/portraits/k_hurt.png',
        'description': "Louise's classmate.\nSpecializes in fire magic.\nHer nickname is \"Kirche of the Mild Fever\".",
        "skills": ["fire", "fire_needle", "fire_arrow", "fire_shield", "heal"],
        'hp': 190,
        'max_hp': 190,
        'mp': 170,
        'max_mp': 170,
        'attack': 22,
        'defense': 22,
        'agility': 28,
        'accuracy': 88,
        'cast_video': 'video/cast/kirche_cast.webm',
        'state': 'normal',
        'cooldown': 0
    },
    'henrietta': {
        'name': "Henrietta",
        "is_mage": True,
        'portrait': 'gui/portraits/h.png',
        'portrait_normal': 'gui/portraits/h.png',
        'portrait_happy': 'gui/portraits/h_happy.png',
        'portrait_hurt': 'gui/portraits/h_hurt.png',
        'description': "Princess of the Tristain Kingdom.\nChildhood friend of Louise.\nSpecializes in water magic.",
        "skills": ["water", "water_needle", "water_hazard", "water_blade", "heal"],
        'hp': 185,
        'max_hp': 185,
        'mp': 175,
        'max_mp': 175,
        'attack': 23,
        'defense': 25,
        'agility': 32,
        'accuracy': 87,
        'cast_video': 'video/cast/henrietta_cast.webm',
        'state': 'normal',
        'cooldown': 0
    }
}

# ============================================================================
# ENEMY DATA (without exp_reward and gold_reward)
# ============================================================================

default enemy_templates = {
    "bandit": {
        "name": "Bandit",
        "hp": 80,
        "max_hp": 80,
        "mp": 20,
        "max_mp": 20,
        "attack": 25,
        "defense": 15,
        "agility": 20,
        "accuracy": 80,
        "sprite": "images/enemies/bandit.png",
        "skills": ["slash"]
    },
    "mage": {
        "name": "Dark Mage",
        "hp": 60,
        "max_hp": 60,
        "mp": 100,
        "max_mp": 100,
        "attack": 35,
        "defense": 10,
        "agility": 25,
        "accuracy": 85,
        "sprite": "images/enemies/mage.png",
        "skills": ["fire", "fire_needle"]
    },
    "golem": {
        "name": "Stone Golem",
        "hp": 150,
        "max_hp": 150,
        "mp": 0,
        "max_mp": 0,
        "attack": 40,
        "defense": 40,
        "agility": 10,
        "accuracy": 70,
        "sprite": "images/enemies/golem.png",
        "skills": ["slash"]
    }
}

# ============================================================================
# BATTLE FUNCTIONS
# ============================================================================

init python:

    def init_battle(enemy_list):
        """Initializes battle state with specified enemies"""
        store.enemies = []
        for i, enemy_type in enumerate(enemy_list):
            if enemy_type in store.enemy_templates:
                enemy = dict(store.enemy_templates[enemy_type])
                enemy['id'] = i
                enemy['key'] = "{}_{}".format(enemy_type, i)
                enemy['state'] = 'normal'
                store.enemies.append(enemy)
        
        store.battle_active = True
        store.battle_phase = "player"
        store.current_turn_index = 0
        store.aoe_casting = {}
        store.defense_buffs = {}
        
        # Reset character states
        for key in store.party_characters:
            store.party_characters[key]['state'] = 'normal'
            store.party_characters[key]['cooldown'] = 0

    def get_current_actor():
        """Gets current acting character"""
        party = get_alive_party_members()
        if store.current_turn_index < len(party):
            return party[store.current_turn_index]
        return None

    def calculate_damage(attacker, defender, skill):
        """Calculates damage"""
        base_damage = skill.get('damage', 30)
        atk = attacker.get('attack', 20)
        defense = defender.get('defense', 10)
        
        # Account for defense buffs
        def_key = None
        for k, v in store.party_characters.items():
            if v == defender:
                def_key = k
                break
        
        if def_key and def_key in store.defense_buffs:
            defense += store.defense_buffs[def_key].get('value', 0)
        
        damage = int((base_damage + atk * 0.5) * (100 / (100 + defense)))
        # Small variation
        damage = int(damage * random.uniform(0.9, 1.1))
        return max(1, damage)

    def check_hit(attacker, skill):
        """Checks if attack hits"""
        accuracy = skill.get('accuracy', 85)
        attacker_acc = attacker.get('accuracy', 80)
        final_acc = (accuracy + attacker_acc) / 2
        return random.randint(1, 100) <= final_acc

    def perform_attack(attacker_key, attacker, skill, target):
        """Performs attack"""
        skill_data = store.skills.get(skill) if isinstance(skill, str) else skill
        if not skill_data:
            return None
        
        # Check MP
        mp_cost = skill_data.get('consume', 0)
        if attacker.get('mp', 0) < mp_cost:
            return {"success": False, "reason": "not_enough_mp"}
        
        # Spend MP
        attacker['mp'] = attacker['mp'] - mp_cost
        
        results = []
        
        # AOE or single target
        if skill_data.get('is_aoe'):
            targets = get_alive_enemies() if attacker_key in store.party_characters else get_alive_party_members()
            for t in targets:
                if isinstance(t, tuple):
                    t = t[1]
                hit = check_hit(attacker, skill_data)
                if hit:
                    damage = calculate_damage(attacker, t, skill_data)
                    t['hp'] = max(0, t['hp'] - damage)
                    results.append({"target": t, "hit": True, "damage": damage})
                else:
                    results.append({"target": t, "hit": False, "damage": 0, "dodged": True})
        else:
            # Single target
            hit = check_hit(attacker, skill_data)
            if hit:
                if skill_data.get('is_heal'):
                    heal = skill_data.get('heal_value', 50)
                    target['hp'] = min(target['hp'] + heal, target['max_hp'])
                    results.append({"target": target, "hit": True, "heal": heal})
                elif skill_data.get('is_buff'):
                    # Apply buff
                    results.append({"target": target, "hit": True, "buff": skill_data.get('buff_type')})
                else:
                    damage = calculate_damage(attacker, target, skill_data)
                    target['hp'] = max(0, target['hp'] - damage)
                    results.append({"target": target, "hit": True, "damage": damage})
            else:
                results.append({"target": target, "hit": False, "damage": 0, "dodged": True})
        
        return {"success": True, "results": results, "skill": skill_data}

    def enemy_turn():
        """Enemy turn"""
        alive_enemies = get_alive_enemies()
        alive_party = get_alive_party_members()
        
        results = []
        
        for enemy in alive_enemies:
            if not alive_party:
                break
            
            # Choose random skill
            enemy_skills = enemy.get('skills', ['slash'])
            skill_key = random.choice(enemy_skills)
            skill_data = store.skills.get(skill_key, store.skills['slash'])
            
            # Choose random target
            target_key, target = random.choice(alive_party)
            
            # Attack
            result = perform_attack(enemy['key'], enemy, skill_key, target)
            if result and result.get('success'):
                results.append({
                    "attacker": enemy,
                    "skill": skill_data,
                    "target_key": target_key,
                    "target": target,
                    "results": result.get('results', [])
                })
        
        return results

    def next_turn():
        """Advance to next turn"""
        party = get_alive_party_members()
        store.current_turn_index += 1
        
        if store.current_turn_index >= len(party):
            # All characters acted - enemy turn
            store.battle_phase = "enemy"
            store.current_turn_index = 0
        
        # Check victory/defeat
        if not get_alive_enemies():
            store.battle_phase = "victory"
        elif not get_alive_party_members():
            store.battle_phase = "defeat"

    def apply_defense(char_key):
        """Applies defense to character"""
        store.defense_buffs[char_key] = {
            "value": 50,
            "turns": 2
        }
        # Restore some MP
        char = store.party_characters.get(char_key)
        if char:
            char['mp'] = min(char['mp'] + 10, char['max_mp'])

    def update_defense_buffs():
        """Updates defense buffs"""
        to_remove = []
        for key in store.defense_buffs:
            store.defense_buffs[key]['turns'] -= 1
            if store.defense_buffs[key]['turns'] <= 0:
                to_remove.append(key)
        for key in to_remove:
            del store.defense_buffs[key]

    def update_aoe_casting():
        """Updates AOE casting"""
        to_cast = []
        for key in store.aoe_casting:
            store.aoe_casting[key]['turns_left'] -= 1
            if store.aoe_casting[key]['turns_left'] <= 0:
                to_cast.append((key, store.aoe_casting[key]['skill']))
        
        for key, skill in to_cast:
            del store.aoe_casting[key]
            # Execute AOE
            char = store.party_characters.get(key)
            if char and char.get('hp', 0) > 0:
                perform_attack(key, char, skill, None)


# ============================================================================
# STYLES
# ============================================================================

style battle_card:
    background "#5c4033"
    padding (5, 5)

style battle_card_active:
    background "#8b6914"
    padding (5, 5)

style battle_card_inactive:
    background "#3a3a3a"
    padding (5, 5)

style battle_action_button:
    background "#8b5a2b"
    hover_background "#a06030"
    padding (15, 10)
    xsize 150
    ysize 50

style battle_action_button_text:
    color "#fff8e7"
    size 20
    bold True
    text_align 0.5

style battle_menu_button:
    background "#8b5a2b"
    hover_background "#a06030"
    padding (20, 12)
    xsize 280
    ysize 55

style battle_menu_button_text:
    color "#fff8e7"
    hover_color "#ffffff"
    size 22
    bold True
    text_align 0.5
    outlines [(1, "#3d2817", 1, 1)]

style battle_start_button:
    background "#c9763c"
    hover_background "#e08850"
    padding (20, 15)
    xsize 280
    ysize 60

style battle_start_button_text:
    color "#ffffff"
    hover_color "#ffffd0"
    size 26
    bold True
    text_align 0.5
    outlines [(2, "#5c3d2e", 0, 0)]

style battle_title_text:
    color "#fff8e7"
    size 32
    bold True
    outlines [(2, "#3d2817", 0, 0)]
    text_align 0.5

style battle_hp_bar:
    left_bar Solid("#4caf50")
    right_bar Solid("#2d2d2d")
    thumb None
    ysize 14
    xsize 140

style battle_mp_bar:
    left_bar Solid("#29b6f6")
    right_bar Solid("#2d2d2d")
    thumb None
    ysize 14
    xsize 140

style battle_bar_label:
    color "#fff8e7"
    size 14
    bold True
    outlines [(1, "#000000", 0, 0)]

style item_button_normal:
    background "#5c3d2e"
    hover_background "#a06030"
    padding (10, 8)

style item_button_selected:
    background "#8b5a2b"
    hover_background "#a06030"
    padding (10, 8)

style skill_button_enabled:
    background "#5c3d2e"
    hover_background "#7a5040"
    padding (8, 6)

style skill_button_disabled:
    background "#3a3a3a"
    padding (8, 6)

style item_button_disabled:
    background "#3a3a3a"
    padding (10, 8)


# ============================================================================
# INVENTORY SCREEN (FULL)
# ============================================================================

screen inventory():
    tag menu
    modal True
    
    add "#00000088"
    
    default local_selected_item = None
    default show_target_selection = False
    default confirm_target = None
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 600
        background "#e8d5b8"
        padding (20, 20)
        
        vbox:
            spacing 15
            xfill True
            
            # Header
            frame:
                background "#8b5a2b"
                xalign 0.5
                padding (30, 10)
                text "Inventory" color "#fff8e7" size 28 bold True
            
            # Show lock status
            if inventory_locked:
                frame:
                    background "#ff4444"
                    xalign 0.5
                    padding (15, 5)
                    text "Items are currently locked" color "#ffffff" size 16
            
            hbox:
                spacing 20
                xfill True
                
                # Item list
                frame:
                    background "#dcbfa6"
                    xsize 400
                    ysize 400
                    padding (10, 10)
                    
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        
                        vbox:
                            spacing 8
                            
                            if curr_items:
                                for item_name, quantity in curr_items.items():
                                    $ is_selected = (local_selected_item == item_name)
                                    button:
                                        xfill True
                                        if is_selected:
                                            style "item_button_selected"
                                        else:
                                            style "item_button_normal"
                                        action SetScreenVariable("local_selected_item", item_name)
                                        
                                        hbox:
                                            spacing 10
                                            text item_name color "#fff8e7" size 18
                                            text "x[quantity]" color "#ffd700" size 18 xalign 1.0
                            else:
                                text "No items" color "#5c3d2e" size 18 xalign 0.5
                
                # Item info
                frame:
                    background "#dcbfa6"
                    xsize 420
                    ysize 400
                    padding (15, 15)
                    
                    vbox:
                        spacing 15
                        
                        if local_selected_item and local_selected_item in items:
                            $ item_info = items[local_selected_item]
                            
                            text local_selected_item color "#5c3d2e" size 24 bold True
                            
                            frame:
                                background "#e8d5b8"
                                xfill True
                                padding (10, 10)
                                text item_info.get('description', 'No description') color "#3d2817" size 16
                            
                            null height 20
                            
                            if not inventory_locked:
                                textbutton "Use Item":
                                    xalign 0.5
                                    style "battle_menu_button"
                                    text_style "battle_menu_button_text"
                                    action SetScreenVariable("show_target_selection", True)
                            else:
                                frame:
                                    background "#666666"
                                    xalign 0.5
                                    padding (20, 12)
                                    text "Items Locked" color "#aaaaaa" size 22
                        else:
                            text "Select an item to view details" color "#8b5a2b" size 18 xalign 0.5 yalign 0.5
            
            # Close button
            textbutton "Close":
                xalign 0.5
                style "battle_menu_button"
                text_style "battle_menu_button_text"
                action Return()
    
    # Target selection window
    if show_target_selection and local_selected_item and not inventory_locked:
        frame:
            xalign 0.5
            yalign 0.5
            xsize 500
            ysize 450
            background "#e8d5b8"
            padding (20, 20)
            
            vbox:
                spacing 15
                
                frame:
                    background "#8b5a2b"
                    xalign 0.5
                    padding (20, 8)
                    text "Select Target" color "#fff8e7" size 22 bold True
                
                text "Apply [local_selected_item] to:" color "#5c3d2e" size 18 xalign 0.5
                
                # Party member list
                vbox:
                    spacing 10
                    xalign 0.5
                    
                    for char_key, char_data in party_characters.items():
                        $ can_use = can_use_item_on_target(local_selected_item, char_key)
                        button:
                            xsize 350
                            if can_use:
                                background "#5c3d2e"
                                hover_background "#7a5040"
                            else:
                                background "#3a3a3a"
                            padding (15, 10)
                            if can_use:
                                action SetScreenVariable("confirm_target", char_key)
                            
                            hbox:
                                spacing 15
                                
                                # Mini portrait
                                frame:
                                    background "#1a1a1a"
                                    xsize 50
                                    ysize 50
                                    if char_data.get('portrait'):
                                        add char_data['portrait'] xalign 0.5 yalign 0.5 fit "contain"
                                
                                vbox:
                                    if can_use:
                                        text char_data['name'] color "#fff8e7" size 18
                                    else:
                                        text char_data['name'] color "#888888" size 18
                                    hbox:
                                        spacing 10
                                        text "HP: [char_data['hp']]/[char_data['max_hp']]" color "#4caf50" size 14
                                        text "MP: [char_data['mp']]/[char_data['max_mp']]" color "#29b6f6" size 14
                                    if not can_use:
                                        text "(Cannot use on this target)" color "#ff6666" size 12
                
                hbox:
                    spacing 20
                    xalign 0.5
                    
                    textbutton "Cancel":
                        style "battle_menu_button"
                        text_style "battle_menu_button_text"
                        action SetScreenVariable("show_target_selection", False)
    
    # Confirmation window
    if confirm_target and local_selected_item:
        $ target_name = party_characters.get(confirm_target, {}).get('name', 'Unknown')
        
        frame:
            xalign 0.5
            yalign 0.5
            xsize 400
            ysize 200
            background "#e8d5b8"
            padding (20, 20)
            
            vbox:
                spacing 20
                xalign 0.5
                
                text "Confirm" color "#5c3d2e" size 24 bold True xalign 0.5
                text "Apply [local_selected_item] to [target_name]?" color "#3d2817" size 18 xalign 0.5
                
                hbox:
                    spacing 30
                    xalign 0.5
                    
                    textbutton "Yes":
                        style "battle_menu_button"
                        text_style "battle_menu_button_text"
                        action [
                            Function(use_item, local_selected_item, confirm_target),
                            SetScreenVariable("confirm_target", None),
                            SetScreenVariable("show_target_selection", False),
                            SetScreenVariable("local_selected_item", None)
                        ]
                    
                    textbutton "No":
                        style "battle_menu_button"
                        text_style "battle_menu_button_text"
                        action SetScreenVariable("confirm_target", None)


# ============================================================================
# BATTLE PREPARATION MENU
# ============================================================================

screen battle_menu():
    tag menu
    modal True
    
    # Darkening background
    add "#00000088"
    
    # Main container
    frame:
        xfill True
        yfill True
        background None
        padding (40, 30, 40, 30)
        
        vbox:
            xfill True
            yfill True
            spacing 15
            
            # === HEADER ===
            frame:
                background "#8b5a2b"
                xalign 0.5
                padding (40, 10)
                
                text "Battle Preparation" style "battle_title_text"
            
            # === MAIN AREA ===
            hbox:
                spacing 30
                xalign 0.5
                yalign 0.5
                
                # --- LEFT MENU ---
                vbox:
                    spacing 12
                    xsize 300
                    
                    # Items/Inventory
                    textbutton "Items":
                        style "battle_menu_button"
                        text_style "battle_menu_button_text"
                        action ShowMenu("inventory")
                    
                    # View characters
                    textbutton "Characters":
                        style "battle_menu_button"
                        text_style "battle_menu_button_text"
                        action ShowMenu("characters")
                    
                    # Separator
                    null height 20
                    
                    # Back (close menu without battle)
                    textbutton "Back":
                        style "battle_menu_button"
                        text_style "battle_menu_button_text"
                        action Return("cancel")
                    
                    # Large separator before battle button
                    null height 40
                    
                    # START BATTLE - main button
                    textbutton "Start Battle":
                        style "battle_start_button"
                        text_style "battle_start_button_text"
                        action Return("start_battle")
                
                # --- RIGHT PANEL: BATTLE PARTICIPANTS ---
                frame:
                    background "#dcbfa6"
                    xsize 650
                    ysize 450
                    padding (15, 15)
                    
                    vbox:
                        spacing 15
                        xfill True
                        
                        # Panel header
                        frame:
                            background "#8b5a2b"
                            xalign 0.5
                            xsize 300
                            padding (15, 8)
                            
                            text "Battle Participants" color "#fff8e7" size 24 bold True xalign 0.5
                        
                        # Character slots
                        hbox:
                            spacing 20
                            xalign 0.5
                            yalign 0.3
                            
                            for char_key, char_data in party_characters.items():
                                use battle_character_slot(char_key, char_data)
                        
                        # Bottom info panel
                        frame:
                            background "#e8d5b8"
                            xalign 0.5
                            xsize 580
                            ysize 120
                            padding (15, 15)
                            
                            if selected_character:
                                use battle_character_info(selected_character)
                            else:
                                text "Select a character to view information" xalign 0.5 yalign 0.5 color "#8b5a2b" size 18


# === COMPONENT: CHARACTER SLOT ===
screen battle_character_slot(char_key, char_data):
    button:
        background "#5c3d2e"
        hover_background "#7a5040"
        xsize 200
        ysize 220
        padding (5, 5)
        action SetVariable("selected_character", char_data)
        
        vbox:
            spacing 8
            xalign 0.5
            
            # Character portrait
            frame:
                background "#1a1a1a"
                xsize 140
                ysize 140
                xalign 0.5
                
                if char_data.get('portrait'):
                    add char_data['portrait'] xalign 0.5 yalign 0.5 fit "contain"
                else:
                    # Color placeholder for testing
                    if char_key == "saito":
                        add Solid("#1a237e") xsize 130 ysize 130 xalign 0.5 yalign 0.5
                    else:
                        add Solid("#7b1fa2") xsize 130 ysize 130 xalign 0.5 yalign 0.5
            
            # HP bar
            hbox:
                spacing 5
                xalign 0.5
                text "HP" style "battle_bar_label"
                bar:
                    style "battle_hp_bar"
                    value char_data['hp']
                    range char_data['max_hp']
            
            # MP bar
            hbox:
                spacing 5
                xalign 0.5
                text "MP" style "battle_bar_label"
                bar:
                    style "battle_mp_bar"
                    value char_data['mp']
                    range char_data['max_mp']


# === COMPONENT: CHARACTER INFO ===
screen battle_character_info(char_data):
    hbox:
        spacing 20
        xfill True
        
        # Mini portrait
        frame:
            background "#5c3d2e"
            xsize 80
            ysize 80
            padding (5, 5)
            
            if char_data.get('portrait'):
                add char_data['portrait'] xalign 0.5 yalign 0.5 fit "contain"
            else:
                add Solid("#333333") xsize 70 ysize 70 xalign 0.5 yalign 0.5
        
        # Info
        vbox:
            spacing 5
            
            text char_data.get('name', 'Unknown') color "#5c3d2e" size 20 bold True
            
            # Attack type based on is_mage
            $ attack_type = get_attack_type(char_data)
            text "Type: [attack_type]" color "#8b5a2b" size 16
            
            hbox:
                spacing 20
                text "HP: [char_data['hp']]/[char_data['max_hp']]" color "#4caf50" size 16
                text "MP: [char_data['mp']]/[char_data['max_mp']]" color "#29b6f6" size 16


# === CHARACTERS SCREEN ===
screen characters():
    tag menu
    modal True
    
    add "#00000088"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 550
        background "#e8d5b8"
        padding (20, 20)
        
        vbox:
            spacing 15
            
            frame:
                background "#8b5a2b"
                xalign 0.5
                padding (30, 10)
                text "Party Members" color "#fff8e7" size 28 bold True
            
            hbox:
                spacing 20
                xalign 0.5
                
                for char_key, char_data in party_characters.items():
                    use character_detail_card(char_key, char_data)
            
            textbutton "Close":
                xalign 0.5
                style "battle_menu_button"
                text_style "battle_menu_button_text"
                action Return()


# Character card for characters screen
screen character_detail_card(char_key, char_data):
    frame:
        background "#dcbfa6"
        xsize 200
        ysize 320
        padding (10, 10)
        
        vbox:
            spacing 8
            xalign 0.5
            
            # Portrait
            frame:
                background "#5c3d2e"
                xsize 100
                ysize 100
                xalign 0.5
                padding (5, 5)
                
                if char_data.get('portrait'):
                    add char_data['portrait'] xalign 0.5 yalign 0.5 fit "contain"
                else:
                    add Solid("#333333") xsize 90 ysize 90 xalign 0.5 yalign 0.5
            
            text char_data.get('name', 'Unknown') color "#5c3d2e" size 16 bold True xalign 0.5
            
            # Attack type based on is_mage
            $ attack_type = get_attack_type(char_data)
            text "[attack_type]" color "#8b5a2b" size 12 xalign 0.5
            
            if char_data.get('hp') is not None and char_data.get('max_hp') is not None:
                text "HP: [char_data['hp']]/[char_data['max_hp']]" color "#4caf50" size 12 xalign 0.5
            
            if char_data.get('mp') is not None and char_data.get('max_mp') is not None:
                text "MP: [char_data['mp']]/[char_data['max_mp']]" color "#29b6f6" size 12 xalign 0.5
            
            if char_data.get('attack') is not None:
                text "ATK: [char_data['attack']]" color "#ff6b6b" size 12 xalign 0.5
            
            if char_data.get('defense') is not None:
                text "DEF: [char_data['defense']]" color "#4dabf7" size 12 xalign 0.5


# ============================================================================
# BATTLE SCREEN
# ============================================================================

screen battle_screen():
    tag battle
    modal True
    
    # Battle background - fallback solid color first, then image on top
    add Solid("#2d4a2d")
    add "images/battle/forest_bg.png" xalign 0.5 yalign 0.5
    
    default action_menu = "main"  # main, attack, skills, items, target_enemy, target_ally, defense_target
    default local_selected_skill = None
    default local_selected_item = None
    default show_char_info = None
    default battle_log = []
    
    # Enemies (top of screen)
    hbox:
        xalign 0.5
        yalign 0.2
        spacing 100
        
        for enemy in enemies:
            if enemy.get('hp', 0) > 0:
                button:
                    background None
                    if action_menu == "target_enemy":
                        action [
                            Function(execute_player_attack, local_selected_skill, enemy),
                            SetScreenVariable("action_menu", "main"),
                            SetScreenVariable("local_selected_skill", None)
                        ]
                    
                    vbox:
                        spacing 5
                        
                        # Enemy sprite
                        frame:
                            background None
                            xsize 200
                            ysize 250
                            
                            # Placeholder if no sprite
                            add Solid("#4a3a5a") xsize 150 ysize 200 xalign 0.5 yalign 0.5
                            
                            if enemy.get('sprite'):
                                add enemy['sprite'] xalign 0.5 yalign 0.5 fit "contain"
                        
                        # Enemy name and HP (visible when targeting)
                        if action_menu == "target_enemy":
                            frame:
                                background "#000000aa"
                                padding (10, 5)
                                xalign 0.5
                                
                                vbox:
                                    spacing 3
                                    text enemy['name'] color "#ffffff" size 16 xalign 0.5
                                    bar:
                                        value enemy['hp']
                                        range enemy['max_hp']
                                        xsize 120
                                        ysize 10
                                        left_bar Solid("#ff4444")
                                        right_bar Solid("#333333")
    
    # Character cards (bottom)
    hbox:
        xalign 0.5
        yalign 0.85
        spacing 20
        
        $ party = get_alive_party_members()
        $ current_actor_data = get_current_actor()
        
        for idx, (char_key, char_data) in enumerate(party):
            $ is_active = (battle_phase == "player" and idx == current_turn_index)
            
            button:
                if is_active:
                    style "battle_card_active"
                elif battle_phase != "player":
                    style "battle_card_inactive"
                else:
                    style "battle_card"
                xsize 180
                ysize 220
                action SetScreenVariable("show_char_info", char_key if show_char_info != char_key else None)
                
                vbox:
                    spacing 5
                    xalign 0.5
                    
                    # Portrait
                    frame:
                        background "#1a1a1a"
                        xsize 120
                        ysize 120
                        xalign 0.5
                        
                        # Select portrait based on state
                        $ portrait_key = 'portrait_' + char_data.get('state', 'normal')
                        $ portrait = char_data.get(portrait_key, char_data.get('portrait'))
                        
                        if portrait:
                            add portrait xalign 0.5 yalign 0.5 fit "contain"
                        else:
                            add Solid("#333355") xsize 110 ysize 110 xalign 0.5 yalign 0.5
                    
                    # HP bar
                    hbox:
                        spacing 5
                        xalign 0.5
                        text "HP" color "#ffffff" size 12 bold True
                        bar:
                            value char_data['hp']
                            range char_data['max_hp']
                            xsize 100
                            ysize 12
                            left_bar Solid("#4caf50")
                            right_bar Solid("#2d2d2d")
                    
                    # MP bar
                    hbox:
                        spacing 5
                        xalign 0.5
                        text "MP" color "#ffffff" size 12 bold True
                        bar:
                            value char_data['mp']
                            range char_data['max_mp']
                            xsize 100
                            ysize 12
                            left_bar Solid("#29b6f6")
                            right_bar Solid("#2d2d2d")
                    
                    # Defense status
                    if char_key in defense_buffs:
                        frame:
                            background "#ffd700aa"
                            padding (5, 2)
                            xalign 0.5
                            vbox:
                                text "Defense" color "#000000" size 10 xalign 0.5
                                text "+50" color "#000000" size 10 xalign 0.5
                                text "Boost" color "#006400" size 8 xalign 0.5
    
    # Action menu (right side)
    if battle_phase == "player" and current_actor_data:
        $ actor_key, actor = current_actor_data
        
        frame:
            xalign 0.95
            yalign 0.4
            background "#8b5a2bcc"
            padding (15, 15)
            
            vbox:
                spacing 10
                
                # Main menu
                if action_menu == "main":
                    text "[actor['name']]'s Turn" color "#fff8e7" size 18 bold True xalign 0.5
                    
                    null height 10
                    
                    textbutton "Attack":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "skills")
                    
                    textbutton "Defense":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "defense_target")
                    
                    textbutton "Items":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "items")
                
                # Skills menu
                elif action_menu == "skills":
                    text "Select Skill" color "#fff8e7" size 18 bold True xalign 0.5
                    
                    null height 5
                    
                    for skill_key in actor.get('skills', []):
                        if skill_key in skills:
                            $ skill_data = skills[skill_key]
                            $ can_use = actor['mp'] >= skill_data.get('consume', 0)
                            
                            button:
                                xsize 180
                                if can_use:
                                    style "skill_button_enabled"
                                else:
                                    style "skill_button_disabled"
                                
                                if can_use:
                                    if skill_data.get('is_aoe'):
                                        action [
                                            SetScreenVariable("local_selected_skill", skill_key),
                                            Function(execute_aoe_attack, actor_key, skill_key),
                                            SetScreenVariable("action_menu", "main")
                                        ]
                                    elif skill_data.get('is_heal') or skill_data.get('is_buff'):
                                        action [
                                            SetScreenVariable("local_selected_skill", skill_key),
                                            SetScreenVariable("action_menu", "target_ally")
                                        ]
                                    else:
                                        action [
                                            SetScreenVariable("local_selected_skill", skill_key),
                                            SetScreenVariable("action_menu", "target_enemy")
                                        ]
                                
                                vbox:
                                    spacing 2
                                    $ text_color = "#fff8e7" if can_use else "#888888"
                                    $ mp_color = "#29b6f6" if can_use else "#555555"
                                    text skill_data['name'] color text_color size 14
                                    hbox:
                                        spacing 10
                                        text "MP: [skill_data['consume']]" color mp_color size 12
                                        if skill_data.get('cast_turns', 0) > 0:
                                            text "Cast: [skill_data['cast_turns']]" color "#ffd700" size 12
                    
                    null height 10
                    
                    textbutton "Back":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "main")
                
                # Target selection for attack
                elif action_menu == "target_enemy":
                    text "Select Enemy" color "#fff8e7" size 18 bold True xalign 0.5
                    text "(Click on enemy sprite)" color "#cccccc" size 14 xalign 0.5
                    
                    null height 10
                    
                    textbutton "Back":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "skills")
                
                # Ally selection (heal/buff)
                elif action_menu == "target_ally":
                    text "Select Ally" color "#fff8e7" size 18 bold True xalign 0.5
                    
                    for ally_key, ally_data in party:
                        button:
                            xsize 180
                            background "#5c3d2e"
                            hover_background "#7a5040"
                            padding (8, 6)
                            action [
                                Function(execute_support_skill, actor_key, local_selected_skill, ally_key),
                                SetScreenVariable("action_menu", "main"),
                                SetScreenVariable("local_selected_skill", None)
                            ]
                            
                            hbox:
                                spacing 10
                                text ally_data['name'] color "#fff8e7" size 14
                                text "HP:[ally_data['hp']]" color "#4caf50" size 12
                    
                    null height 10
                    
                    textbutton "Back":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "skills")
                
                # Defense target selection
                elif action_menu == "defense_target":
                    text "Defend Who?" color "#fff8e7" size 18 bold True xalign 0.5
                    
                    for ally_key, ally_data in party:
                        button:
                            xsize 180
                            background "#5c3d2e"
                            hover_background "#7a5040"
                            padding (8, 6)
                            action [
                                Function(apply_defense, ally_key),
                                Function(next_turn),
                                SetScreenVariable("action_menu", "main")
                            ]
                            
                            text ally_data['name'] color "#fff8e7" size 14
                    
                    null height 10
                    
                    textbutton "Back":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "main")
                
                # Items menu
                elif action_menu == "items":
                    text "Select Item" color "#fff8e7" size 18 bold True xalign 0.5
                    
                    if curr_items:
                        for item_name, quantity in curr_items.items():
                            button:
                                xsize 180
                                background "#5c3d2e"
                                hover_background "#7a5040"
                                padding (8, 6)
                                action [
                                    SetScreenVariable("local_selected_item", item_name),
                                    SetScreenVariable("action_menu", "item_target")
                                ]
                                
                                hbox:
                                    spacing 10
                                    text item_name color "#fff8e7" size 14
                                    text "x[quantity]" color "#ffd700" size 14
                    else:
                        text "No items" color "#888888" size 14 xalign 0.5
                    
                    null height 10
                    
                    textbutton "Back":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "main")
                
                # Item target selection
                elif action_menu == "item_target":
                    text "Use [local_selected_item] on:" color "#fff8e7" size 16 bold True xalign 0.5
                    
                    for ally_key, ally_data in party:
                        $ can_use = can_use_item_on_target(local_selected_item, ally_key)
                        button:
                            xsize 180
                            if can_use:
                                background "#5c3d2e"
                                hover_background "#7a5040"
                            else:
                                background "#3a3a3a"
                            padding (8, 6)
                            if can_use:
                                action [
                                    Function(use_item_in_battle, local_selected_item, ally_key),
                                    SetScreenVariable("action_menu", "main"),
                                    SetScreenVariable("local_selected_item", None)
                                ]
                            
                            hbox:
                                spacing 10
                                if can_use:
                                    text ally_data['name'] color "#fff8e7" size 14
                                else:
                                    text ally_data['name'] color "#888888" size 14
                                text "HP:[ally_data['hp']]" color "#4caf50" size 12
                    
                    null height 10
                    
                    textbutton "Back":
                        style "battle_action_button"
                        text_style "battle_action_button_text"
                        action SetScreenVariable("action_menu", "items")
    
    # Process enemy turn automatically when it's their phase
    if battle_phase == "enemy":
        timer 0.5 action Function(process_enemy_turns)
    
    # Action message (center of screen)
    if battle_message:
        frame:
            xalign 0.5
            yalign 0.5
            background "#000000cc"
            padding (30, 15)
            
            text battle_message color "#ffffff" size 24 bold True
    
    # Victory screen
    if battle_phase == "victory":
        frame:
            xalign 0.5
            yalign 0.4
            background "#ffd700ee"
            padding (60, 40)
            
            vbox:
                spacing 20
                
                text "VICTORY!" color "#3d2817" size 48 bold True xalign 0.5
                
                textbutton "Continue":
                    xalign 0.5
                    style "battle_start_button"
                    text_style "battle_start_button_text"
                    action Return("victory")
    
    # Defeat screen
    if battle_phase == "defeat":
        frame:
            xalign 0.5
            yalign 0.4
            background "#8b0000ee"
            padding (60, 40)
            
            vbox:
                spacing 20
                
                text "DEFEAT" color "#ffffff" size 48 bold True xalign 0.5
                
                textbutton "Retry":
                    xalign 0.5
                    style "battle_start_button"
                    text_style "battle_start_button_text"
                    action Return("defeat")
    
    # Character info window
    if show_char_info:
        $ info_char = party_characters.get(show_char_info, {})
        
        frame:
            xalign 0.05
            yalign 0.3
            xsize 280
            background "#e8d5b8ee"
            padding (15, 15)
            
            vbox:
                spacing 8
                
                text info_char.get('name', 'Unknown') color "#5c3d2e" size 22 bold True
                
                # Attack type based on is_mage
                $ attack_type = get_attack_type(info_char)
                text "Type: [attack_type]" color "#8b5a2b" size 14
                
                null height 5
                
                # Status Panel
                text "--- Status Panel ---" color "#5c3d2e" size 14 bold True
                text "HP: [info_char['hp']]/[info_char['max_hp']]" color "#4caf50" size 16
                text "MP: [info_char['mp']]/[info_char['max_mp']]" color "#29b6f6" size 16
                $ cooldown = info_char.get('cooldown', 0)
                if cooldown > 0:
                    text "[cooldown] Turns Wait" color "#ffd700" size 14
                else:
                    text "0 Turns Wait (Ready)" color "#4caf50" size 14
                
                null height 5
                
                text "Attack Power: [info_char.get('attack', 0)]" color "#ff6b6b" size 14
                text "Defense: [info_char.get('defense', 0)]" color "#4dabf7" size 14
                text "Agility: [info_char.get('agility', 0)]" color "#69db7c" size 14
                text "Accuracy: [info_char.get('accuracy', 0)]%" color "#fcc419" size 14
                
                null height 10
                
                text "Skills:" color "#5c3d2e" size 16 bold True
                
                for skill_key in info_char.get('skills', []):
                    if skill_key in skills:
                        $ s = skills[skill_key]
                        vbox:
                            spacing 2
                            text "* [s['name']]" color "#3d2817" size 12
                            text "  MP: [s['consume']] - [s.get('description', '')]" color "#666666" size 10
                
                null height 10
                
                textbutton "Close":
                    xalign 0.5
                    background "#5c3d2e"
                    hover_background "#7a5040"
                    padding (10, 5)
                    action SetScreenVariable("show_char_info", None)
                    text_color "#fff8e7"
                    text_size 14


# ============================================================================
# BATTLE SCREEN FUNCTIONS
# ============================================================================

init python:
    def execute_player_attack(skill_key, target_enemy):
        """Executes player attack on enemy"""
        actor_data = get_current_actor()
        if not actor_data:
            return
        
        actor_key, actor = actor_data
        skill_data = store.skills.get(skill_key)
        
        if not skill_data:
            return
        
        # Show message
        store.battle_message = "{} uses {}!".format(actor['name'], skill_data['name'])
        
        # Execute attack
        result = perform_attack(actor_key, actor, skill_key, target_enemy)
        
        if result and result.get('success'):
            for res in result.get('results', []):
                if res.get('dodged'):
                    target_enemy['state'] = 'happy'
                    store.battle_message = "The character ({}) successfully dodged the attack!".format(target_enemy['name'])
                elif res.get('hit'):
                    target_enemy['state'] = 'hurt'
                    dmg = res.get('damage', 0)
                    store.battle_message = "{} deals {} damage to {}!".format(actor['name'], dmg, target_enemy['name'])
        
        # Next turn
        next_turn()
        
        # Clear message after a delay (use timer in real game)
        store.battle_message = ""

    def execute_aoe_attack(actor_key, skill_key):
        """Executes AOE attack"""
        actor = store.party_characters.get(actor_key)
        skill_data = store.skills.get(skill_key)
        
        if not actor or not skill_data:
            return
        
        cast_turns = skill_data.get('cast_turns', 0)
        
        if cast_turns > 0:
            # Start casting
            store.aoe_casting[actor_key] = {
                'skill': skill_key,
                'turns_left': cast_turns
            }
            actor['cooldown'] = cast_turns
            store.battle_message = "{} is casting {}... ({} turns)".format(actor['name'], skill_data['name'], cast_turns)
        else:
            # Instant AOE
            store.battle_message = "{} uses {}!".format(actor['name'], skill_data['name'])
            result = perform_attack(actor_key, actor, skill_key, None)
        
        next_turn()
        store.battle_message = ""

    def execute_support_skill(actor_key, skill_key, target_key):
        """Executes support skill"""
        actor = store.party_characters.get(actor_key)
        target = store.party_characters.get(target_key)
        skill_data = store.skills.get(skill_key)
        
        if not actor or not target or not skill_data:
            return
        
        store.battle_message = "{} uses {} on {}!".format(actor['name'], skill_data['name'], target['name'])
        
        result = perform_attack(actor_key, actor, skill_key, target)
        
        if result and result.get('success'):
            for res in result.get('results', []):
                if res.get('heal'):
                    store.battle_message = "{} recovered {} HP!".format(target['name'], res['heal'])
                elif res.get('buff'):
                    store.battle_message = "{}'s {} increased!".format(target['name'], res['buff'])
        
        next_turn()
        store.battle_message = ""

    def use_item_in_battle(item_name, target_key):
        """Uses item in battle (character loses turn)"""
        actor_data = get_current_actor()
        if not actor_data:
            return
        
        actor_key, actor = actor_data
        target = store.party_characters.get(target_key)
        
        if not target:
            return
        
        store.battle_message = "{} uses {} on {}!".format(actor['name'], item_name, target['name'])
        
        success = use_item(item_name, target_key)
        
        if success:
            target['state'] = 'happy'
        
        next_turn()
        store.battle_message = ""

    def process_enemy_turns():
        """Processes enemy turns"""
        results = enemy_turn()
        
        for r in results:
            enemy = r['attacker']
            skill = r['skill']
            target = r['target']
            
            store.battle_message = "{} uses {}! Target: {}".format(enemy['name'], skill['name'], target['name'])
            
            for res in r.get('results', []):
                if res.get('dodged'):
                    target['state'] = 'happy'
                elif res.get('hit') and res.get('damage'):
                    target['state'] = 'hurt'
        
        # Check victory/defeat after enemy turn
        if not get_alive_enemies():
            store.battle_phase = "victory"
        elif not get_alive_party_members():
            store.battle_phase = "defeat"
        else:
            # Return turn to player
            store.battle_phase = "player"
            store.current_turn_index = 0
        
        # Update buffs
        update_defense_buffs()
        update_aoe_casting()
        
        store.battle_message = ""


# ============================================================================
# USAGE EXAMPLE - CORRECT WAY TO USE
# ============================================================================

# In your script.rpy, use like this:
#
# label forest_battle:
#     # Show battle preparation menu
#     call screen battle_menu
#     
#     if _return == "start_battle":
#         # Initialize battle state
#         $ init_battle(["mage", "mage"])
#         
#         # Show battle screen and get result
#         call screen battle_screen
#         
#         if _return == "victory":
#             "You won the battle!"
#         else:
#             "Game Over..."
#     elif _return == "cancel":
#         "You decided not to fight."
#     
#     return
#
# 
# To lock/unlock inventory from anywhere:
#     $ lock_inventory()
#     $ unlock_inventory()
#
# To add a character to party:
#     $ party_characters['tabitha'] = dict(all_characters['tabitha'])
#
# To remove a character from party:
#     $ del party_characters['tabitha']

```

## Файл: `scripts\features\battle_menu.rpy`

```renpy
# # ============================================================================
# # ZERO NO TSUKAIMA - REMASTER BATTLE MENU
# # Полноэкранное меню подготовки к бою в стиле PS2 игры
# # ============================================================================

# # Данные персонажей
# default battle_characters = {
#     'saito': {
#         'name': 'Saito',
#         'description': "A Japanese boy who was summoned to this world by Louise.\nHe is treated as a familiar by Louise.", 
#         "is_mage": false, # Category: Attack 
#         "category": "Attack",
#         "skills": [skills["slash"], skills["d_slash"], skills["wind_moon_slash"]],
#         'hp': 100,
#         'max_hp': 100,
#         'mp': 50,
#         'max_mp': 50,
#         'portrait': 'gui/portraits/s.png',
#         'in_party': True,
#     },
#     'louise': {
#         'name': 'Louise',
#         "description": "The magician who summoned Saito.\nAlthough she can use Void magic,\nits true nature remains unknown.",
#         "is_mage": true, # Category: Magic
#         "skills": [skills["arrow"], skills["heroism"], skills["dispel"]]
#         'hp': 80,
#         'max_hp': 80,
#         'mp': 80,
#         'max_mp': 80,
#         'portrait': 'gui/portraits/l.png',
#         'in_party': True,
#     },
#     'siesta': {
#         'name': 'Siesta',
#         'portrait': 'gui/portraits/si.png',
#         "skills": None, # None skills non category
#         'description': "A maid working at Tristain Academy of Magic.\nSince she is a commoner, she cannot use magic.\nShe has feelings for Saito."
#     },
#     'tabitha': {
#         'name': "Tabitha",
#         "is_mage": true, # Category: Magic
#         'portrait': 'gui/portraits/t.png',
#         'description': "Louise's classmate.\nSpecializes in wind magic.\mHer nickname is \"Tabitha of the Snow Wind\".", 
#         "skills": [skills["wing"], skills["air_needle"], skills["wind_break"], skills["air_force"], skills["heal"]],
#     },
#     'kirche': {
#         'name': "Kirche",
#         "is_mage": true, # Category: Magic
#         'portrait': 'gui/portraits/k.png'
#         'description': "Louise's classmate.\nSpecializes in fire magic.\nHer nickname is \"Kirche of the Mild Fever\".",
#         "skills": [skills["fire"], skills["fire_needle"], skills["fire_arrow"], skills["fire_shield"], skills["heal"]],
#     },
#     'henrietta': {
#         'name': "Henrietta",
#         "is_mage": true, # Category: Magic
#         'portrait': 'gui/portraits/h.png',
#         'description': "Princess of the Tristain Kingdom.\nChildhood friend of Louise.\nSpecializes in water magic.",
#         "skills": [skills["water"], skills["water_needle"], skills["water_hazard"], skills["water_blade"], skills["heal"]],
#     }
# }

# default skills = {
#     "arrow": {
#         "name": "Magic Arrow",
#         "consume": 30,
#         "description": "Attacks a single enemy",
#     },
#     "heroism": {
#         "name": "Heroism",
#         "consume": 50,
#         "description": "Attacks a single enemy"
#     },
#     "meteor": {
#         "name": "Meteor",
#         "consume": 70,
#         "description": "Attacks all enemies",
#     },
#     "dispel": {
#         "name": "Dispel Magic",
#         "consume": 30,
#         "description": "Increases accuracy of 1 ally",
#     },
#     "heal": {
#         "name": "Heal",
#         "consume": 30,
#         "description": "Recovers HP of 1 ally"
#     },

#     "slash": {
#         "name": "Slash",
#         "consume": 30,
#         "description": "Attacks a single enemy",
#     },

#     "d_slash": {
#         "name": "Double Slash",
#         "consume": 50,
#         "description": "Attacks a single enemy",
#     },

#     "wind_moon_slash": {
#         "name": "Wind Moon Slash",
#         "consume": 70,
#         "description": "Attacks all enemies",
#     },

#     "wing": {
#         "name": "Wing",
#         "consume": 30,
#         "description": "Attacks a single enemy",
#     },

#     "air_needle": {
#         "name": "Ait Needle",
#         "consume": 50,
#         "description": "Attacks a single enemy"
#     },

#     "wind_break":{
#         "name": "Wind Break",
#         "consume": 70,
#         "description": "Attacks all enemies",
#     },

#     "air_force": {
#         "name": "Air Force",
#         "consume": 30,
#         "description": "Increases speed of 1 ally",
#     },

#     "fire": {
#         "name": "Fire",
#         "consume": 30,
#         "description": "Attacks a single enemy"
#     },

#     "fire_needle": {
#         "name": "Fire Needle",
#         "consume": 50,
#         "description": "Attacks a single enemy"
#     },

#     "fire_arrow": {
#         "name": "Fire Arrow",
#         "consume": 70,
#         "description": "Attacks all enemies"
#     },

#     "fire_shield": {
#         "name": "Fire Shield",
#         "consume": 30,
#         "description": "Increases defense of 1 ally",
#     },

#     "water"" {
#         "name": "Water",
#         "consume": 30,
#         "description": "Attacks a single enemy",
#     },
#     "water_needle" {
#         "name": "Water Needle",
#         "consume": 30,
#         "description": "Attacks a single enemy",
#     },

#     "water_hazard": {
#         "name": "Water Hazard",
#         "consume": 70,
#         "description": "Attacks all enemies"
#     },

#     "water_blade": {
#         "name": "Water Blade",
#         "consume": 30,
#         "description": "Increases attack power of 1 ally",
#     },


# }

# # Выбранный персонаж для просмотра
# default selected_character = None

# init python:
#     def show_battle_menu():
#         """Вызывает экран меню подготовки к бою"""
#         renpy.call_screen("battle_menu")
    
#     def get_party_members():
#         """Возвращает список персонажей в отряде"""
#         return [char for key, char in store.battle_characters.items() if char.get('in_party', False)]

# # ============================================================================
# # СТИЛИ В ДУХЕ PS2 ВЕРСИИ (деревянная текстура, тёплые тона)
# # ============================================================================

# init:
#     # === ОСНОВНЫЕ ЦВЕТА ===
#     # Деревянная тема как в оригинале
#     define gui.battle_wood_dark = "#5c3d2e"      # Тёмное дерево (рамки)
#     define gui.battle_wood_medium = "#8b5a2b"    # Среднее дерево (кнопки)
#     define gui.battle_wood_light = "#a06030"     # Светлое дерево (hover)
#     define gui.battle_panel_bg = "#e8d5b8"       # Бежевый фон панелей
#     define gui.battle_panel_inner = "#dcbfa6"    # Внутренний фон
#     define gui.battle_text_light = "#fff8e7"     # Светлый текст
#     define gui.battle_text_shadow = "#3d2817"    # Тень текста

#     # === ГЛАВНЫЙ КОНТЕЙНЕР (полноэкранный) ===
#     style battle_fullscreen:
#         background "#00000099"  # Полупрозрачный затемняющий слой

#     # === ЗАГОЛОВОК МЕНЮ ===
#     style battle_title_frame:
#         #background Frame("gui/battle/header_bg.png", 20, 10, 20, 10) 
#         # Fallback если нет изображения:
#         background "#8b5a2b"
#         padding (30, 8, 30, 8)
#         xminimum 400

#     style battle_title_text:
#         color "#fff8e7"
#         size 32
#         bold True
#         outlines [(2, "#3d2817", 0, 0)]
#         text_align 0.5

#     # === ОСНОВНАЯ ПАНЕЛЬ ===
#     style battle_main_panel:
#         #background Frame("gui/battle/panel_bg.png", 15, 15, 15, 15)
#         # Fallback:
#         background "#e8d5b8"
#         padding (20, 20, 20, 20)

#     # === КНОПКИ МЕНЮ (деревянный стиль) ===
#     style battle_menu_button:
#         #background Frame("gui/battle/button_idle.png", 15, 8, 15, 8)
#         #hover_background Frame("gui/battle/button_hover.png", 15, 8, 15, 8)
#         #selected_background Frame("gui/battle/button_selected.png", 15, 8, 15, 8)
#         # Fallback:
#         background "#8b5a2b"
#         hover_background "#a06030"
#         padding (20, 12, 20, 12)
#         xsize 280
#         ysize 55

#     style battle_menu_button_text:
#         color "#fff8e7"
#         hover_color "#ffffff"
#         size 22
#         bold True
#         text_align 0.5
#         outlines [(1, "#3d2817", 1, 1)]

#     # === КНОПКА "НАЧАТЬ БОЙ" (выделенная) ===
#     style battle_start_button:
#         #background Frame("gui/battle/button_start_idle.png", 15, 8, 15, 8)
#         #hover_background Frame("gui/battle/button_start_hover.png", 15, 8, 15, 8)
#         # Fallback:
#         background "#c9763c"
#         hover_background "#e08850"
#         padding (20, 15, 20, 15)
#         xsize 280
#         ysize 60

#     style battle_start_button_text:
#         color "#ffffff"
#         hover_color "#ffffd0"
#         size 26
#         bold True
#         text_align 0.5
#         outlines [(2, "#5c3d2e", 0, 0)]

#     # === ПАНЕЛЬ УЧАСТНИКОВ БОЯ ===
#     style battle_participants_frame:
#         #background Frame("gui/battle/participants_bg.png", 12, 12, 12, 12)
#         # Fallback:
#         background "#dcbfa6"
#         padding (15, 15, 15, 15)

#     style battle_participants_header:
#         background "#8b5a2b"
#         padding (15, 8, 15, 8)

#     style battle_participants_header_text:
#         color "#fff8e7"
#         size 24
#         bold True
#         text_align 0.5
#         outlines [(1, "#3d2817", 1, 1)]

#     # === СЛОТ ПЕРСОНАЖА ===
#     style battle_char_slot:
#         #background Frame("gui/battle/char_slot_bg.png", 8, 8, 8, 8)
#         # Fallback:
#         background "#5c3d2e"
#         padding (8, 8, 8, 8)

#     style battle_char_slot_hover:
#         #background Frame("gui/battle/char_slot_hover.png", 8, 8, 8, 8)
#         # Fallback:
#         background "#7a5040"
#         padding (8, 8, 8, 8)

#     # === HP/MP БАРЫ ===
#     style battle_hp_bar:
#         left_bar Solid("#4caf50")  # Зелёный HP
#         right_bar Solid("#2d2d2d")
#         thumb None
#         ysize 14
#         xsize 140

#     style battle_mp_bar:
#         left_bar Solid("#29b6f6")  # Голубой MP
#         right_bar Solid("#2d2d2d")
#         thumb None
#         ysize 14
#         xsize 140

#     style battle_bar_label:
#         color "#fff8e7"
#         size 14
#         bold True
#         outlines [(1, "#000000", 0, 0)]

#     # === ПАНЕЛЬ ИНФОРМАЦИИ О ПЕРСОНАЖЕ ===
#     style battle_info_panel:
#         background "#e8d5b8"
#         padding (15, 15, 15, 15)

#     style battle_char_name_text:
#         color "#5c3d2e"
#         size 20
#         bold True

#     # === ПУСТОЙ СЛОТ ===
#     style battle_empty_slot:
#         background "#4a4a4a"
#         xsize 120
#         ysize 120


# # ============================================================================
# # ЭКРАН МЕНЮ ПОДГОТОВКИ К БОЮ
# # ============================================================================

# screen battle_menu():
#     tag menu
#     modal True
    
#     # Полноэкранный затемняющий фон
#     add "#00000088"
    
#     # Фоновое изображение (пентаграмма как в оригинале)
#     # add "gui/battle/battle_bg.png" xalign 0.5 yalign 0.5
    
#     # Главный контейнер
#     frame:
#         style_prefix "battle"
#         xfill True
#         yfill True
#         background None
#         padding (40, 30, 40, 30)
        
#         vbox:
#             xfill True
#             yfill True
#             spacing 15
            
#             # === ЗАГОЛОВОК ===
#             frame:
#                 style "battle_title_frame"
#                 xalign 0.5
#                 background "#8b5a2b"
#                 padding (40, 10)
                
#                 text "Battle Preparation" style "battle_title_text"
            
#             # === ОСНОВНАЯ ОБЛАСТЬ ===
#             hbox:
#                 spacing 30
#                 xalign 0.5
#                 yalign 0.5
                
#                 # --- ЛЕВОЕ МЕНЮ ---
#                 vbox:
#                     spacing 12
#                     xsize 300
                    
#                     # Предметы/Инвентарь
#                     textbutton "Items":
#                         style "battle_menu_button"
#                         text_style "battle_menu_button_text"
#                         action ShowMenu("inventory")  # Или ваш экран инвентаря
                    
#                     # Просмотр персонажей
#                     textbutton "Characters":
#                         style "battle_menu_button"
#                         text_style "battle_menu_button_text"
#                         action ShowMenu("characters")  # Экран информации о персонажах
                    
#                     # Выбор отряда (если есть больше персонажей)
#                     # textbutton "Squad selection":
#                     #     style "battle_menu_button"
#                     #     text_style "battle_menu_button_text"
#                     #     action ShowMenu("party_select")
                    
#                     # Разделитель
#                     null height 20
                    
#                     # Вернуться (закрыть меню без боя)
#                     textbutton "Back":
#                         style "battle_menu_button"
#                         text_style "battle_menu_button_text"
#                         action Return("cancel")
                    
#                     # Большой разделитель перед кнопкой боя
#                     null height 40
                    
#                     # НАЧАТЬ БОЙ - главная кнопка
#                     textbutton "Start Battle":
#                         style "battle_start_button"
#                         text_style "battle_start_button_text"
#                         action Return("start_battle")
#                         # confirm ("Start Battle?", Return("start_battle") Return())
                
#                 # --- ПРАВАЯ ПАНЕЛЬ: УЧАСТНИКИ БОЯ ---
#                 frame:
#                     style "battle_participants_frame"
#                     background "#dcbfa6"
#                     xsize 650
#                     ysize 450
                    
#                     vbox:
#                         spacing 15
#                         xfill True
                        
#                         # Заголовок панели
#                         frame:
#                             style "battle_participants_header"
#                             xalign 0.5
#                             xsize 300
                            
#                             text "Battle Participants" style "battle_participants_header_text" xalign 0.5
                        
#                         # Слоты персонажей
#                         hbox:
#                             spacing 20
#                             xalign 0.5
#                             yalign 0.3
                            
#                             for char_key, char_data in battle_characters.items():
#                                 if char_data.get('in_party', False):
#                                     use battle_character_slot(char_key, char_data)
                        
#                         # Нижняя информационная панель
#                         frame:
#                             style "battle_info_panel"
#                             xalign 0.5
#                             xsize 580
#                             ysize 120
                            
#                             if selected_character:
#                                 use battle_character_info(selected_character)
#                             else:
#                                 text "Select a character to view information" xalign 0.5 yalign 0.5 color "#8b5a2b" size 18


# # === КОМПОНЕНТ: СЛОТ ПЕРСОНАЖА ===
# screen battle_character_slot(char_key, char_data):
#     button:
#         style "battle_char_slot"
#         background "#5c3d2e"
#         hover_background "#7a5040"
#         xsize 200
#         ysize 220
#         action SetVariable("selected_character", char_data)
        
#         vbox:
#             spacing 8
#             xalign 0.5
            
#             # Портрет персонажа
#             frame:
#                 background "#1a1a1a"
#                 xsize 140
#                 ysize 140
#                 xalign 0.5
                
#                 # Если есть портрет - показываем, иначе заглушка
#                 if char_data.get('portrait'):
#                     add char_data['portrait'] xalign 0.5 yalign 0.5 fit "contain"
#                 else:
#                     # Цветная заглушка для тестирования
#                     if char_key == "saito":
#                         add Solid("#1a237e") xsize 130 ysize 130 xalign 0.5 yalign 0.5
#                     else:
#                         add Solid("#7b1fa2") xsize 130 ysize 130 xalign 0.5 yalign 0.5
            
#             # HP бар
#             hbox:
#                 spacing 5
#                 xalign 0.5
#                 text "HP" style "battle_bar_label"
#                 bar:
#                     style "battle_hp_bar"
#                     value char_data['hp']
#                     range char_data['max_hp']
            
#             # MP бар
#             hbox:
#                 spacing 5
#                 xalign 0.5
#                 text "MP" style "battle_bar_label"
#                 bar:
#                     style "battle_mp_bar"
#                     value char_data['mp']
#                     range char_data['max_mp']


# # === КОМПОНЕНТ: ИНФОРМАЦИЯ О ПЕРСОНАЖЕ ===
# screen battle_character_info(char_data):
#     hbox:
#         spacing 20
#         xfill True
        
#         # Мини-портрет
#         frame:
#             background "#5c3d2e"
#             xsize 80
#             ysize 80
            
#             if char_data.get('portrait'):
#                 add char_data['portrait'] xalign 0.5 yalign 0.5 fit "contain"
#             else:
#                 add Solid("#333333") xsize 70 ysize 70 xalign 0.5 yalign 0.5
        
#         # Информация
#         vbox:
#             spacing 8
            
#             text char_data.get('name', 'Unknown') style "battle_char_name_text"
            
#             hbox:
#                 spacing 20
#                 text "HP: [char_data['hp']]/[char_data['max_hp']]" color "#4caf50" size 18
#                 text "MP: [char_data['mp']]/[char_data['max_mp']]" color "#29b6f6" size 18
            
#             # Можно добавить дополнительную информацию
#             # text "Уровень: [char_data.get('level', 1)]" color "#5c3d2e" size 16


# # Экран выбора отряда (заглушка)
# screen party_select():
#     tag menu
#     modal True
    
#     add "#00000088"
    
#     frame:
#         xalign 0.5
#         yalign 0.5
#         xsize 900
#         ysize 550
#         background "#e8d5b8"
#         padding (20, 20)
        
#         vbox:
#             spacing 15
            
#             frame:
#                 background "#8b5a2b"
#                 xalign 0.5
#                 padding (30, 10)
#                 text "Squad selection" color "#fff8e7" size 28 bold True
            
#             text "Здесь можно будет выбрать участников боя..." xalign 0.5 color "#5c3d2e"
            
#             textbutton "Close":
#                 xalign 0.5
#                 style "battle_menu_button"
#                 text_style "battle_menu_button_text"
#                 action Return()


# # Экран информации о персонажах (заглушка)
# screen characters():
#     tag menu
#     modal True
    
#     add "#00000088"
    
#     frame:
#         xalign 0.5
#         yalign 0.5
#         xsize 900
#         ysize 550
#         background "#e8d5b8"
#         padding (20, 20)
        
#         vbox:
#             spacing 15
            
#             frame:
#                 background "#8b5a2b"
#                 xalign 0.5
#                 padding (30, 10)
#                 text "Characters" color "#fff8e7" size 28 bold True
            
#             hbox:
#                 spacing 20
#                 xalign 0.5
                
#                 for char_key, char_data in battle_characters.items():
#                     use character_detail_card(char_key, char_data)
            
#             textbutton "Close":
#                 xalign 0.5
#                 style "battle_menu_button"
#                 text_style "battle_menu_button_text"
#                 action Return()


# # Карточка персонажа для экрана персонажей
# screen character_detail_card(char_key, char_data):
#     frame:
#         background "#dcbfa6"
#         xsize 280
#         ysize 350
#         padding (15, 15)
        
#         vbox:
#             spacing 10
#             xalign 0.5
            
#             # Портрет
#             frame:
#                 background "#5c3d2e"
#                 xsize 150
#                 ysize 150
#                 xalign 0.5
                
#                 if char_key == "saito":
#                     add Solid("#1a237e") xsize 140 ysize 140 xalign 0.5 yalign 0.5
#                 else:
#                     add Solid("#7b1fa2") xsize 140 ysize 140 xalign 0.5 yalign 0.5
            
#             text char_data.get('name', 'Unknown') xalign 0.5 color "#5c3d2e" size 22 bold True
            
#             vbox:
#                 spacing 5
#                 text "HP: [char_data['hp']]/[char_data['max_hp']]" color "#4caf50" size 16
#                 text "MP: [char_data['mp']]/[char_data['max_mp']]" color "#29b6f6" size 16

```

## Файл: `scripts\features\inventory.rpy`

```renpy
# ## inventory.rpy - Система инвентаря

# default curr_items = {
#     "Bread": 3,
#     "Herb": 3,
#     "Elixir": 3,
# }


# init python:
#     # items dict
#     items = {
#         "Bread": {
#             "description": "Restore HP",
#         },
#         "Herb": {
#             "description": "Restore MP"
#         },
#         "Elixir": {
#             "description": "Restore HP and MP"
#         }
#     }

# # Экран инвентаря (заглушка)
# screen inventory():
#     tag menu
#     modal True
    
#     add "#00000088"
    
#     frame:
#         xalign 0.5
#         yalign 0.5
#         xsize 800
#         ysize 500
#         background "#e8d5b8"
#         padding (20, 20)
        
#         vbox:
#             spacing 15
            
#             frame:
#                 background "#8b5a2b"
#                 xalign 0.5
#                 padding (30, 10)
#                 text "Items" color "#fff8e7" size 28 bold True
            
#             text "Здесь будет список предметов..." xalign 0.5 color "#5c3d2e"
            
#             textbutton "Close":
#                 xalign 0.5
#                 style "battle_menu_button"
#                 text_style "battle_menu_button_text"
#                 action Return()


```

## Файл: `scripts\features\scene_helpers.rpy`

```renpy
# =============================================================================
#  scene_helpers.rpy
#  Готовые методы: затухание сцены, скрытие/возврат интерфейса,
#  умный показ 1-3 персонажей, flash со сбросом спрайтов.
#  Просто положи файл в game/ — переписывать существующий код не нужно.
#
#  ВАЖНО: персонаж определяется по ТЕГУ (первое слово имени образа).
#    "d 1 happy" -> тег "d"   |   "s 1 sad" -> тег "s"
#  Поэтому смена эмоции того же персонажа ("s 1 sad" -> "s 1") НЕ вызывает
#  слайд: меняется только картинка на месте (как обычный show с dissolve).
# =============================================================================


# =============================================================================
#  ГЕОМЕТРИЯ ПОЗИЦИЙ  (zoom, xalign, yalign) — значения совпадают с твоими
#  transform normal_left / normal_center / normal_right и close_center.
#  Меняешь координаты здесь — меняются и точки покоя, и слайды.
# =============================================================================
init -1 python:

    CHARA_GEOM = {
        #  mode      side       zoom  xalign  yalign
        ("normal", "left"):   (0.55, -0.20, 1.00),
        ("normal", "center"): (0.55,  0.50, 1.00),
        ("normal", "right"):  (0.55,  1.20, 1.00),

        ("big",    "left"):   (0.70, -0.30, 1.00),
        ("big",    "center"): (0.70,  0.50, 0.15),
        ("big",    "right"):  (0.70,  1.40, 0.95),
    }

    def _geom(mode, side):
        return CHARA_GEOM.get((mode, side), CHARA_GEOM[("normal", "center")])

    # точка ЗА экраном для слайда
    def _off(side, direction):
        if side == "left":
            return -0.60
        if side == "right":
            return 1.70
        # центр: заезжает слева, уезжает вправо (как slide_*_to_center)
        return 1.70 if direction == "out" else -0.60

    # порядок наложения. центральный (например derflinger) может быть
    # на переднем плане (center_front=True) или под боковыми (False).
    def _zorder(side, center_front):
        if side == "center":
            if center_front is True:
                return 50
            if center_front is False:
                return 5
            return 15
        return 20

    def _tag_of(image_name):
        # тег = первое слово имени образа ("d 1 happy" -> "d")
        return image_name.split()[0]


# =============================================================================
#  ПАРАМЕТРИЧЕСКИЕ ТРАНСФОРМЫ
# =============================================================================

# точка покоя (для появления/обновления без движения)
transform chara_at(z, xa, ya):
    zoom z
    xalign xa
    yalign ya
    alpha 1.0

# плавный въезд из-за экрана в точку покоя
transform chara_slide_in(z, xa, ya, sx):
    zoom z
    yalign ya
    xalign sx
    alpha 0.0
    easein 0.4 xalign xa alpha 1.0

# плавный выезд из точки покоя за экран
transform chara_slide_out(z, xa, ya, ex):
    zoom z
    yalign ya
    xalign xa
    alpha 1.0
    easeout 0.4 xalign ex alpha 0.0

# плавное ПЕРЕМЕЩЕНИЕ из старой точки покоя в новую (например center -> left),
# когда тот же персонаж остаётся на экране, но меняет позицию/размер.
transform chara_move(z0, xa0, ya0, z1, xa1, ya1):
    zoom z0
    xalign xa0
    yalign ya0
    alpha 1.0
    ease 0.4 zoom z1 xalign xa1 yalign ya1


# =============================================================================
#  СОСТОЯНИЕ: slot ("left"/"center"/"right") -> (tag, image, mode, z)
#  z — текущий zorder спрайта. Растёт от _sprite_z: кто показан/изменён
#  последним, тот выше всех (новый элемент перекрывает остальных).
# =============================================================================
default _sprite_slots = {}
default _sprite_z = 0

# Все теги персонажей — чтобы снести всех одной командой.
define CHARA_TAGS = [
    "l", "s", "k", "t", "c", "h", "si", "ha", "g", "d", "o", "m",
    "npc_left", "npc_right", "mage",
]

define _SLIDE_DUR = 0.4   # длительность слайда (синхронно с ease в трансформах)


# =============================================================================
#  СКРЫТЬ ВСЕХ ПЕРСОНАЖЕЙ ОДНОЙ КОМАНДОЙ
#     $ clear_chars()           — с dissolve
#     $ clear_chars(anim=None)  — мгновенно
# =============================================================================
init -1 python:

    _CLEAR_SLIDE_DUR = 0.4

    def clear_chars(anim="dissolve", direction="left"):
        """
        Убирает всех персонажей.
        
        anim:
            "dissolve"    — плавное исчезновение (по умолчанию)
            "slide"       — слайд, направления берутся из direction
            "slide_left"  — все уезжают влево
            "slide_right" — все уезжают вправо
            None          — мгновенно
        
        direction (для anim="slide"):
            "left"   — все влево
            "right"  — все вправо
            dict {slot: "left"|"right"|"dissolve"} — индивидуально по слотам
        """
        slots = store._sprite_slots

        if not slots:
            store._sprite_slots = {}
            store._sprite_z = 0
            if anim == "dissolve":
                renpy.with_statement(dissolve)
            return

        if renpy.is_skipping() or renpy.in_rollback():
            for tag in CHARA_TAGS:
                renpy.hide(tag)
            store._sprite_slots = {}
            store._sprite_z = 0
            renpy.with_statement(None)
            return

        # Нормализация
        if anim == "slide_left":
            anim, direction = "slide", "left"
        elif anim == "slide_right":
            anim, direction = "slide", "right"

        if anim != "slide":
            for tag in CHARA_TAGS:
                renpy.hide(tag)
            store._sprite_slots = {}
            store._sprite_z = 0
            if anim == "dissolve":
                renpy.with_statement(dissolve)
            else:
                renpy.with_statement(None)
            return

        # --- SLIDE ---
        if isinstance(direction, str):
            dir_map = {s: direction for s in slots.keys()}
        else:
            dir_map = dict(direction)
            for s in slots.keys():
                dir_map.setdefault(s, "left")

        dissolve_tags = []
        slide_tags = []

        for s, (tag, img, mode, z) in slots.items():
            act = dir_map.get(s, "left")
            z0, xa0, ya0 = _geom(mode, s)

            if act == "dissolve":
                dissolve_tags.append((tag, img, z0, xa0, ya0))
            else:
                slide_tags.append((tag, img, z0, xa0, ya0, act))

        # Запускаем slide
        for tag, img, z0, xa0, ya0, act in slide_tags:
            trans = _make_clear_slide(act)
            renpy.show(img, at_list=[trans], tag=tag, zorder=z0)

        # dissolve-персонажи оставляем на месте (исчезнут в общем dissolve)
        for tag, img, z0, xa0, ya0 in dissolve_tags:
            renpy.show(img, at_list=[chara_at(z0, xa0, ya0)], tag=tag, zorder=z0)

        renpy.with_statement(None)

        if slide_tags:
            renpy.pause(_CLEAR_SLIDE_DUR)

        for tag in CHARA_TAGS:
            renpy.hide(tag)
        store._sprite_slots = {}
        store._sprite_z = 0

        if dissolve_tags and slide_tags:
            renpy.with_statement(dissolve)
        else:
            renpy.with_statement(None)


    def _make_clear_slide(direction):
        """Возвращает ATL-трансформ слайда из текущей позиции за экран."""
        if direction == "left":
            return slide_left_out_generic
        else:
            return slide_right_out_generic

# =============================================================================
#  1. ЗАТУХАНИЕ СЦЕНЫ  (всё внутри fade): спрайты сняты, интерфейс скрыт,
#     музыка затихает по флагу, фон меняется на new_bg или на чёрный.
#
#     $ fade_clear()                                  -> в чёрный, музыка играет
#     $ fade_clear(stop_music=True)                   -> в чёрный + музыка затихает
#     $ fade_clear("bg forest")                       -> сразу новый фон под затуханием
#     $ fade_clear("bg forest", True)                 -> новый фон + стоп музыки
#     $ fade_clear("bg forest", new_music="t17")      -> фон + завести трек audio.t17
#     
#     УПРАВЛЕНИЕ HUD:
#     $ fade_clear(show_hud=True, hud_delay=1.0)      -> показать HUD через 1 сек (по умолч.)
#     $ fade_clear(show_hud=True, hud_delay=2.5)      -> показать HUD через 2.5 сек
#     $ fade_clear(show_hud=False)                    -> не показывать HUD после fade
# =============================================================================
init -1 python:

    def fade_clear(new_bg=None, stop_music=False, music_fadeout=1.0, new_music=None, music_fadein=1.0):
        
        # 1) убрать всех персонажей
        for tag in CHARA_TAGS:
            renpy.hide(tag)
        store._sprite_slots = {}
        store._sprite_z = 0

        # 2) спрятать интерфейс на время затухания
        store.quick_menu = False
        if hasattr(store, "sympathy_hud_visible"):
            store._fade_hud_was = store.sympathy_hud_visible
            store.sympathy_hud_visible = False

        # 3) очистить мастер-слой и поставить фон/чёрный
        renpy.scene()
        if new_bg is not None:
            renpy.show(new_bg, at_list=[bg_center])
        else:
            renpy.show("black")

        # 4) музыка: при стопе или при смене трека гасим старую
        if stop_music or new_music is not None:
            renpy.music.stop(fadeout=music_fadeout)

        # 5) всё проигрывается ВНУТРИ затухания
        renpy.with_statement(fade)

        # 6) завести новый трек по короткому имени ("t17" -> audio.t17,
        #    либо передай полный путь "audio/bgm/t17.ogg")
        if new_music is not None:
            track = getattr(store.audio, new_music, new_music)
            renpy.music.play(track, fadein=music_fadein)

        # вернуть быстрые кнопки для последующих реплик
        #store.quick_menu = True



# =============================================================================
#  4. УМНЫЙ ПОКАЗ 1-3 ПЕРСОНАЖЕЙ
# -----------------------------------------------------------------------------
#  show_sprites(chars, mode="normal", anim="dissolve", side=None, center_front=None)
#
#    chars  — строка (1 персонаж) или список/кортеж из 1..3 имён образов:
#               1 -> позиция из side (по умолчанию "center")
#               2 -> [левый, правый]
#               3 -> [левый, центр, правый]
#    mode   — "normal" / "big"
#    anim   — "dissolve" / "slide" / None (None = мгновенно, без анимации,
#                                          в т.ч. при смене эмоции)
#    side   — только для одного персонажа: "left"/"center"/"right"
#    center_front — порядок наложения для ЦЕНТРАЛЬНОГО при ПЕРВОМ показе:
#                   True  — центр сразу поверх боковых,
#                   False — центр сразу под боковыми,
#                   None  — обычный порядок.
#
#  ZORDER (наложение спрайтов):
#   • любой ПОКАЗАННЫЙ/ИЗМЕНЁННЫЙ в этом вызове спрайт получает новый, самый
#     высокий zorder -> «новый элемент перекрывает всех остальных»;
#   • неизменившиеся спрайты сохраняют свой прежний zorder и относительный
#     порядок (если d перекрывал s и оба не менялись — d так и перекрывает s).
#
#  ЛОГИКА (сравнение со старым раскладом по ТЕГУ персонажа):
#   • тот же персонаж в том же слоте, сменился РАЗМЕР (normal<->big)
#                                     -> плавный scale (chara_move), в ОБЕ стороны;
#   • тот же персонаж в том же слоте, сменилась ТОЛЬКО эмоция -> dissolve на месте;
#   • тот же персонаж в другом слоте  -> плавно переезжает (chara_move);
#   • персонаж пропал/сменился        -> старый уезжает (slide) или гаснет,
#                                         pause(0.2), затем заезжает новый;
#   • неизменившийся слот             -> остаётся как есть.
# =============================================================================
init -1 python:

    def show_sprites(chars, mode="normal", anim="slide", side=None,
                     center_front=None, hide_window=False):
        if isinstance(chars, str):
            chars = [chars]
        chars = list(chars)
        n = len(chars)

        if n == 1:
            layout = {(side or "center"): chars[0]}
        elif n == 2:
            layout = {"left": chars[0], "right": chars[1]}
        elif n == 3:
            layout = {"left": chars[0], "center": chars[1], "right": chars[2]}
        else:
            raise Exception("show_sprites: поддерживается от 1 до 3 персонажей")

        _apply_layout(layout, mode, anim, center_front, hide_window)


    def _apply_layout(layout, mode, anim, center_front, hide_window=False):
        slots  = store._sprite_slots         # slot -> (tag, img, mode, z)

        # Мгновенный режим: скип/перемотка (Ctrl), А ТАКЖЕ откат/прокрутка
        # колесом мыши (rollback / roll-forward). В этих состояниях реальное
        # время НЕ идёт: renpy.pause() возвращается сразу, а alpha-слайды
        # «застревают» прозрачными. is_skipping() ловит только скип, поэтому
        # колесо мыши (rollback) раньше оставляло спрайты невидимыми.
        _instant = renpy.is_skipping() or renpy.in_rollback()

        slide  = (anim == "slide")
        noanim = (anim is None)

        # Текстбокс
        if hide_window:
            _window_hide(None)
        else:
            _window_show(None)

        # новый расклад: slot -> (tag, image)
        new = {}
        for s, img in layout.items():
            new[s] = (_tag_of(img), img)

        # индексируем по ТЕГУ персонажа
        old_by_tag = {tag: (s, oimg, om, oz)
                      for s, (tag, oimg, om, oz) in slots.items()}
        new_by_tag = {tag: (s, nimg) for s, (tag, nimg) in new.items()}

        # ---- БЫСТРЫЙ ПУТЬ: МГНОВЕННЫЙ ПОКАЗ (скип / откат / прокрутка) ----
        # Никаких pause и alpha-анимаций — сразу ставим всех актуальных
        # персонажей в точку покоя с полной непрозрачностью, гасим лишних.
        # Это убирает «прозрачные/невидимые» спрайты при быстром ЛКМ и колесе.
        if _instant:
            new_tags = set(new_by_tag.keys())
            for tag, (os_, oimg, om, oz) in old_by_tag.items():
                if tag not in new_tags:
                    renpy.hide(tag)

            def _order_key_fast(item):
                s = item[0]
                if s != "center":
                    return 1
                if center_front is True:
                    return 2
                if center_front is False:
                    return 0
                return 1

            slot_z = {}
            for s, (tag, nimg) in sorted(new.items(), key=_order_key_fast):
                store._sprite_z += 1
                slot_z[s] = store._sprite_z
                z, xa, ya = _geom(mode, s)
                renpy.show(nimg, at_list=[chara_at(z, xa, ya)],
                           tag=tag, zorder=slot_z[s])
            renpy.with_statement(None)

            new_state = {}
            for s, (tag, nimg) in new.items():
                new_state[s] = (tag, nimg, mode, slot_z[s])
            store._sprite_slots = new_state
            return

        leavers  = []   # (slot, tag, img, mode)
        movers   = []   # (old_slot, new_slot, tag, img, old_mode)  -> другой слот
        resizes  = []   # (slot, tag, img, old_mode)  -> тот же слот, сменился РАЗМЕР
        emotions = []   # (slot, tag, img)            -> тот же слот, сменилась ТОЛЬКО картинка
        entrants = []   # (slot, tag, img)

        for tag, (os_, oimg, om, oz) in old_by_tag.items():
            if tag not in new_by_tag:
                leavers.append((os_, tag, oimg, om))

        for tag, (ns_, nimg) in new_by_tag.items():
            old = old_by_tag.get(tag)
            if old is None:
                entrants.append((ns_, tag, nimg))
            else:
                os_, oimg, om, oz = old
                if os_ != ns_:
                    movers.append((os_, ns_, tag, nimg, om))
                elif om != mode:
                    # ФИКС 2: размер проверяем РАНЬШЕ эмоции, поэтому смена
                    # размера ВСЕГДА даёт плавный scale (chara_move) — и при
                    # normal->big, и при big->normal — даже если заодно
                    # сменилась картинка. Никакого dissolve при зуме.
                    resizes.append((ns_, tag, nimg, om))
                elif oimg != nimg:
                    emotions.append((ns_, tag, nimg))        # только эмоция -> dissolve

        # ---- НАЗНАЧИТЬ ZORDER показанным/изменённым слотам ----
        shown_slots = [m[1] for m in movers] + [r[0] for r in resizes] \
                      + [e[0] for e in emotions] + [e[0] for e in entrants]

        def _order_key(s):
            if s != "center":
                return 1
            if center_front is True:
                return 2
            if center_front is False:
                return 0
            return 1

        slot_z = {}
        for s in sorted(shown_slots, key=_order_key):
            store._sprite_z += 1
            slot_z[s] = store._sprite_z

        old_z_by_slot = {s: oz for s, (tag, oimg, om, oz) in slots.items()}

        # ---- 1) УХОДЯЩИЕ ----
        if leavers:
            if slide:
                for s, tag, oimg, om in leavers:
                    z, xa, ya = _geom(om, s)
                    renpy.show(oimg, at_list=[chara_slide_out(z, xa, ya, _off(s, "out"))],
                               tag=tag, zorder=old_z_by_slot.get(s, 20))
                renpy.with_statement(None)
                renpy.pause(_SLIDE_DUR)
                for s, tag, oimg, om in leavers:
                    renpy.hide(tag)
                renpy.with_statement(None)
            else:
                for s, tag, oimg, om in leavers:
                    renpy.hide(tag)
                renpy.with_statement(None if noanim else dissolve)

        # ---- 2) ПЕРЕЕЗЖАЮЩИЕ (другой слот) ----
        if movers:
            for os_, ns_, tag, nimg, om in movers:
                z1, xa1, ya1 = _geom(mode, ns_)
                if noanim:
                    renpy.show(nimg, at_list=[chara_at(z1, xa1, ya1)],
                               tag=tag, zorder=slot_z[ns_])
                else:
                    z0, xa0, ya0 = _geom(om, os_)
                    renpy.show(nimg, at_list=[chara_move(z0, xa0, ya0, z1, xa1, ya1)],
                               tag=tag, zorder=slot_z[ns_])
            renpy.with_statement(None)

        # ---- 3a) СМЕНА РАЗМЕРА (normal<->big) -> ПЛАВНЫЙ SCALE, без dissolve ----
        if resizes:
            for s, tag, nimg, om in resizes:
                z1, xa1, ya1 = _geom(mode, s)
                if noanim:
                    renpy.show(nimg, at_list=[chara_at(z1, xa1, ya1)],
                               tag=tag, zorder=slot_z[s])
                else:
                    z0, xa0, ya0 = _geom(om, s)            # старая геометрия того же слота
                    renpy.show(nimg, at_list=[chara_move(z0, xa0, ya0, z1, xa1, ya1)],
                               tag=tag, zorder=slot_z[s])
            renpy.with_statement(None)                      # без dissolve и без alpha

        # ---- 3b) СМЕНА ЭМОЦИИ (картинка изменилась, размер тот же) -> dissolve ----
        if emotions:
            for s, tag, nimg in emotions:
                z, xa, ya = _geom(mode, s)
                renpy.show(nimg, at_list=[chara_at(z, xa, ya)],
                           tag=tag, zorder=slot_z[s])
            renpy.with_statement(None if noanim else dissolve)

        # задержка перед появлением новых
        if (leavers or movers) and entrants and not noanim:
            renpy.pause(0.2)

        # ---- 4) НОВЫЕ ПЕРСОНАЖИ ----
        if entrants:
            if slide:
                for s, tag, nimg in entrants:
                    z, xa, ya = _geom(mode, s)
                    renpy.show(nimg, at_list=[chara_slide_in(z, xa, ya, _off(s, "in"))],
                               tag=tag, zorder=slot_z[s])
                renpy.with_statement(None)
                renpy.pause(_SLIDE_DUR)
                # фиксируем точку покоя — если слайд прервали кликом,
                # спрайт не останется полупрозрачным/за экраном.
                for s, tag, nimg in entrants:
                    z, xa, ya = _geom(mode, s)
                    renpy.show(nimg, at_list=[chara_at(z, xa, ya)],
                               tag=tag, zorder=slot_z[s])
                renpy.with_statement(None)
            else:
                for s, tag, nimg in entrants:
                    z, xa, ya = _geom(mode, s)
                    renpy.show(nimg, at_list=[chara_at(z, xa, ya)],
                               tag=tag, zorder=slot_z[s])
                renpy.with_statement(None if noanim else dissolve)

        # ---- ПЕРЕСТРОИТЬ СОСТОЯНИЕ СЛОТОВ ----
        new_state = {}
        for s, (tag, nimg) in new.items():
            z = slot_z.get(s, old_z_by_slot.get(s, 0))
            new_state[s] = (tag, nimg, mode, z)
        store._sprite_slots = new_state


# =============================================================================
#  5.1 FLASH, ГАСЯЩИЙ СПРАЙТЫ ОДНОВРЕМЕННО СО ВСПЫШКОЙ
# -----------------------------------------------------------------------------
#  $ flash_clear()             -> вспышка + все персонажи исчезают внутри неё
#  $ flash_clear("bg forest")  -> ещё и фон сменится под вспышкой
#  после — добавляем нужных вручную:
#     $ show_sprites("s 1", side="center", mode="big")
# =============================================================================
init -1 python:

    def flash_clear(new_bg=None):
        for tag in CHARA_TAGS:
            renpy.hide(tag)
        store._sprite_slots = {}
        store._sprite_z = 0
        if new_bg is not None:
            renpy.show(new_bg, at_list=[bg_center])
        renpy.with_statement(flash)


# =============================================================================
#  5.2 ТРЯСКА ЭКРАНА  (shake / flash / fade) С КОНТРОЛЕМ СПРАЙТОВ
# -----------------------------------------------------------------------------
#  Проблема "scene bg forest with hit_shake": команда scene стирает ВСЕ слои,
#  включая спрайты, а состояние слотов об этом не знает -> show_sprites потом
#  «не видит» снесённые спрайты и часть из них не возвращается.
#
#  shake_scene НЕ вызывает scene: по умолчанию спрайты ОСТАЮТСЯ на месте и
#  просто трясутся вместе с фоном. Дальше можно менять эмоции через show_sprites
#  — анимируется только изменившийся, остальные на месте.
#
#  shake_scene(sound=None, effect="shake", new_bg=None, clear=False)
#    sound  — путь к звуку, напр. "audio/sfx/punch.ogg" (None — без звука)
#    effect — "shake" (hit_shake) / "flash" / "fade" / None (без перехода)
#    new_bg — сменить фон под эффектом (None — фон не трогаем)
#    clear  — True: убрать ВСЕХ персонажей и сбросить слоты (после нужно
#             заново показать всех через show_sprites);
#             False (по умолчанию): спрайты остаются.
#
#  Примеры:
#    # тряхнуть всё как есть + звук удара, спрайты на месте:
#    $ shake_scene(sound="audio/sfx/punch.ogg")
#    $ show_sprites(("l 1 angry", "s 3 angry"))   # меняем только эмоции
#
#    # вспышка, всех снести, потом показать заново:
#    $ shake_scene(sound="audio/sfx/punch.ogg", effect="flash", clear=True)
#    $ show_sprites(("l 1 angry", "s 3 angry"))
#
#    # тряска со сменой фона:
#    $ shake_scene(effect="shake", new_bg="bg forest")
# =============================================================================
init -1 python:

    def shake_scene(sound=None, effect="shake", new_bg=None, clear=False):
        if sound is not None:
            renpy.sound.play(sound)

        if clear:
            for tag in CHARA_TAGS:
                renpy.hide(tag)
            store._sprite_slots = {}
            store._sprite_z = 0

        if new_bg is not None:
            renpy.show(new_bg, at_list=[bg_center])

        trans = {
            "shake": hit_shake,
            "flash": flash,
            "fade":  fade,
            None:    None,
        }.get(effect, hit_shake)

        renpy.with_statement(trans)

```

## Файл: `scripts\features\sympathy.rpy`

```renpy
## sympathy.rpy - Система симпатии (Tsun/Dere)

# ============================================
# ШРИФТ ДЛЯ СИСТЕМЫ СИМПАТИИ
# ============================================
define sympathy_font = "fonts/KuroHanaMincho.ttf"

# Изображения для UI симпатии
image gui_sympathy_bar = "gui/sympathy/bar.webp"
image gui_sympathy_arrow = "gui/sympathy/arrow.webp"
image gui_sympathy_up = "gui/sympathy/up.webp"
image gui_sympathy_down = "gui/sympathy/down.webp"
image gui_sympathy_hud_icon = "gui/sympathy/hud_icon.webp"

# Иконки персонажей для отображения при изменении симпатии
image louise_icon = "gui/sympathy/louise_icon.png"
image haruna_icon = "gui/sympathy/haruna_icon.png"
image henrietta_icon = "gui/sympathy/henrietta_icon.png"
image siesta_icon = "gui/sympathy/siesta_icon.png"
image tabitha_icon = "gui/sympathy/tabitha_icon.png"
image kirche_icon = "gui/sympathy/kirche_icon.png"

# ============================================
# ПЕРЕМЕННЫЕ СИМПАТИИ (НЕ persistent - для корректного rollback)
# Диапазон: -100 (tsun) до +100 (dere), начало = 0 (нейтральный)
# ============================================
default louise_sympathy = 0
default haruna_sympathy = 0
default henrietta_sympathy = 0
default siesta_sympathy = 0
default tabitha_sympathy = 0
default kirche_sympathy = 0

# Отслеживание "известных" персонажей (показываются в меню только после первого взаимодействия)
default known_characters = set()

# Видимость HUD иконки симпатии
default sympathy_hud_visible = False

# Словарь данных персонажей для системы симпатии
init python:
    sympathy_characters = {
        "louise": {
            "name": "Louise",
            "icon": "gui/sympathy/louise_icon.png",
            "var": "louise_sympathy",
            "color": "#e9acb3",
            "has_tsun_dere": True  # Только у Louise есть tsun/dere
        },
        "haruna": {
            "name": "Haruna",
            "icon": "gui/sympathy/haruna_icon.png",
            "var": "haruna_sympathy",
            "color": "#4b4d51",
            "has_tsun_dere": False
        },
        "henrietta": {
            "name": "Henrietta",
            "icon": "gui/sympathy/henrietta_icon.png",
            "var": "henrietta_sympathy",
            "color": "#782163",
            "has_tsun_dere": False
        },
        "siesta": {
            "name": "Siesta",
            "icon": "gui/sympathy/siesta_icon.png",
            "var": "siesta_sympathy",
            "color": "#535a6a",
            "has_tsun_dere": False
        },
        "tabitha": {
            "name": "Tabitha",
            "icon": "gui/sympathy/tabitha_icon.png",
            "var": "tabitha_sympathy",
            "color": "#b4dfec",
            "has_tsun_dere": False
        },
        "kirche": {
            "name": "Kirche",
            "icon": "gui/sympathy/kirche_icon.png",
            "var": "kirche_sympathy",
            "color": "#e36566",
            "has_tsun_dere": False
        }
    }

# ============================================
# ТРАНСФОРМАЦИИ ДЛЯ АНИМАЦИЙ
# ============================================

# Анимация блока уведомления (правый верхний угол)
transform sympathy_notification_anim:
    xpos 1.0
    ypos 0.0
    anchor (1.0, 0.0)
    xoffset -30
    yoffset 30
    alpha 0.0
    easein 0.3 alpha 1.0
    pause 2.0
    easeout 0.4 alpha 0.0

# Анимация полоски симпатии (только для Louise, по центру сверху)
transform sympathy_bar_anim:
    xpos 0.5
    ypos 0.0
    anchor (0.5, 0.0)
    yoffset 15
    alpha 0.0
    zoom 0.8
    linear 0.3 alpha 1.0
    pause 2.0
    linear 0.4 alpha 0.0

# Анимация стрелки/указателя на полоске
# Прогресс-бар идёт от -100 до +100, где 0 = середина
transform sympathy_arrow_anim(start_val, end_val, bar_width_px):
    xpos 0.5
    ypos 0.0
    zoom 0.8
    anchor (0.5, 0.0)
    yoffset 85
    # Позиция: при 0 стрелка по центру, при -100 слева, при +100 справа
    xoffset int(float(start_val) / 100.0 * (bar_width_px / 2.0))
    alpha 0.0
    linear 0.3 alpha 1.0
    # Плавное движение к новой позиции
    linear 1.0 xoffset int(float(end_val) / 100.0 * (bar_width_px / 2.0))
    pause 1.0
    linear 0.4 alpha 0.0

# Анимация второго блока для Louise (tsun/dere + up)
transform sympathy_louise_second_anim:
    xpos 1.0
    ypos 0.0
    anchor (1.0, 0.0)
    xoffset -30
    yoffset 30
    alpha 0.0
    easein 0.3 alpha 1.0
    pause 2.0
    easeout 0.4 alpha 0.0

# ============================================
# HUD ИКОНКА ДЛЯ ОТКРЫТИЯ МЕНЮ СИМПАТИИ (отдельный экран)
# ============================================

transform icon_hover:
    zoom 1.0
    on hover:
        ease 0.1 zoom 1.1
    on idle:
        ease 0.1 zoom 1.0

screen sympathy_hud_icon():
    zorder 100
    
    if sympathy_hud_visible:
        imagebutton:
            xpos 0.1
            ypos 0.1
            anchor (1.0, 0.5)
            xoffset -20
            idle "gui_sympathy_hud_icon"
            hover "gui_sympathy_hud_icon"
            at icon_hover
            action ShowMenu("sympathy_status")

# ============================================
# ЭКРАН УВЕДОМЛЕНИЯ О ИЗМЕНЕНИИ СИМПАТИИ (КЕЙС 1 - ДЛЯ ВСЕХ ПЕРСОНАЖЕЙ)
# ============================================

screen sympathy_notification(char_key, change_value):
    zorder 150
    modal False
    
    $ char_data = sympathy_characters.get(char_key, {"name": "???", "icon": None, "color": "#ffffff"})
    $ char_icon = char_data.get("icon", None)
    
    # Блок в правом верхнем углу: [Уровень симпатии] [Иконка персонажа] [UP/DOWN]
    frame at sympathy_notification_anim:
        xpos 1.0
        ypos 0.0
        anchor (1.0, 0.0)
        xoffset -30
        yoffset 30
        background None
        padding (0, 0)
        
        hbox:
            spacing 15
            yalign 0.5
            
            # 1. Текст "Уровень симпатии" (кастомный шрифт)
            text "Sympathy level":
                font sympathy_font
                size 32
                color "#ffffff"
                yalign 0.5
                outlines [(2, "#000000", 0, 0)]
            
            # 2. Иконка персонажа (умеренный размер)
            if char_icon and renpy.loadable(char_icon):
                add char_icon:
                    zoom 0.5
                    yalign 0.5
            
            # 3. Иконка UP или DOWN (маленький размер)
            if change_value > 0:
                add "gui_sympathy_up":
                    zoom 0.35
                    yalign 0.5
            elif change_value < 0:
                add "gui_sympathy_down":
                    zoom 0.35
                    yalign 0.5

# ============================================
# ЭКРАН УВЕДОМЛЕНИЯ ДЛЯ LOUISE - ВТОРОЙ БЛОК (TSUN/DERE + ПРОГРЕСС-БАР)
# ============================================

screen sympathy_louise_second(change_value, old_value, new_value):
    zorder 150
    modal False
    
    # Определяем текст: dere если повышаем симпатию, tsun если понижаем
    $ display_text = "Dere" if change_value > 0 else "Tsun"
    $ text_color = "#ff69b4" if change_value > 0 else "#ff6b6b"
    
    # Прогресс бар по центру сверху (300 пикселей ширина)
    add "gui_sympathy_bar" at sympathy_bar_anim
    add "gui_sympathy_arrow" at sympathy_arrow_anim(old_value, new_value, 300)
    
    # Блок в правом верхнем углу: [tsun/dere] [UP]
    frame at sympathy_louise_second_anim:
        xpos 1.0
        ypos 0.0
        anchor (1.0, 0.0)
        xoffset -30
        yoffset 30
        background None
        padding (0, 0)
        
        hbox:
            spacing 15
            yalign 0.5
            
            # 1. Текст tsun/dere (кастомный шрифт)
            text display_text:
                font sympathy_font
                size 32
                color text_color
                yalign 0.5
                outlines [(2, "#000000", 0, 0)]
            
            # 2. Иконка UP (всегда, маленький размер)
            add "gui_sympathy_up":
                zoom 0.35
                yalign 0.5

# ============================================
# ЭКРАН ПРОСМОТРА СИМПАТИИ (меню)
# ============================================

screen sympathy_status():
    tag menu
    modal True
    zorder 200
    
    # Затемнённый фон
    add Solid("#00000099")
    
    $ _frame_bg = Frame("gui/frame_wood.png", 20, 20, 20, 20) if renpy.loadable("gui/frame_wood.png") else Solid("#e8d5b8")
    
    # Основной контейнер
    frame:
        xpos 0.5
        ypos 0.5
        anchor (0.5, 0.5)
        xsize 800
        ysize 600
        background _frame_bg
        padding (30, 30)
        
        vbox:
            xfill True
            spacing 20
            
            # Заголовок
            text "Sympathy level":
                xalign 0.5
                font sympathy_font
                size 40
                color "#5c3d2e"
                outlines [(2, "#d4a574", 0, 0)]
            
            null height 20
            
            # Список ТОЛЬКО известных персонажей
            for char_key in sympathy_characters:
                if char_key in known_characters:
                    $ char_data = sympathy_characters[char_key]
                    $ var_name = char_data["var"]
                    $ current_val = getattr(renpy.store, var_name, 0)
                    $ char_name = char_data["name"]
                    $ char_color = char_data["color"]
                    $ char_icon = char_data["icon"]
                    $ has_tsun_dere = char_data.get("has_tsun_dere", False)
                    # Для бара: преобразуем -100..+100 в 0..200 для отображения
                    $ bar_value = current_val + 100
                    
                    frame:
                        xfill True
                        ysize 80
                        background Solid("#f5ead8")
                        padding (15, 10)
                        
                        hbox:
                            spacing 20
                            yalign 0.5
                            
                            # Иконка персонажа
                            if char_icon and renpy.loadable(char_icon):
                                add char_icon:
                                    zoom 0.4
                                    yalign 0.5
                            else:
                                null width 60
                            
                            # Имя персонажа
                            text char_name:
                                font sympathy_font
                                size 28
                                color "#5c3d2e"
                                yalign 0.5
                                min_width 120
                            
                            # Полоска симпатии (от -100 до +100, центр = 0)
                            vbox:
                                yalign 0.5
                                spacing 5
                                xsize 350
                                
                                # Бар (0..200 диапазон, где 100 = нейтраль)
                                bar:
                                    value bar_value
                                    range 200
                                    xsize 350
                                    ysize 20
                                    left_bar Solid(char_color)
                                    right_bar Solid("#3a3a3a")
                                
                                # Подписи Tsun / Dere - ТОЛЬКО для Louise
                                if has_tsun_dere:
                                    hbox:
                                        xfill True
                                        text "Tsun":
                                            font sympathy_font
                                            size 16
                                            color "#8b4513"
                                        text "Dere":
                                            font sympathy_font
                                            size 16
                                            color "#ff69b4"
                                            xalign 1.0
                            
                            # Числовое значение
                            text "[current_val]":
                                font sympathy_font
                                size 28
                                color char_color
                                yalign 0.5
            
            # Если нет известных персонажей
            if not known_characters:
                text "No characters unlocked yet":
                    xalign 0.5
                    font sympathy_font
                    size 24
                    color "#888888"
            
            null height 20
            
            # Кнопка закрыть
            textbutton "Close":
                xalign 0.5
                action Return()
                text_font sympathy_font
                text_size 28
                text_color "#5c3d2e"
                text_hover_color "#8b5a2b"

# ============================================
# ФУНКЦИИ PYTHON
# ============================================

init python:
    def show_sympathy_hud():
        """Show HUD icon of Sympathy menu"""
        renpy.store.sympathy_hud_visible = True
        renpy.show_screen("sympathy_hud_icon")
    
    def hide_sympathy_hud():
        """Hide HUD icon of Sympathy menu"""
        renpy.store.sympathy_hud_visible = False
        renpy.hide_screen("sympathy_hud_icon")
    
    def toggle_sympathy_hud():
        """Toggle HUD icon visibility"""
        if renpy.store.sympathy_hud_visible:
            hide_sympathy_hud()
        else:
            show_sympathy_hud()

    def update_sympathy(value, char_key="louise", min_val=-100, max_val=100,
                        up_sound="audio/sfx/sympathy_up.wav", 
                        down_sound="audio/sfx/sympathy_down.wav"):
        """
        Update character sympathy with animation
        
        Диапазон: -100 (tsun) до +100 (dere), начало = 0 (нейтральный)
        
        Логика:
        - Для всех персонажей: показываем блок [Уровень симпатии] [Иконка] [UP/DOWN]
        - Для Louise: дополнительно показываем прогресс-бар + блок [tsun/dere] [UP]
        """
        
        # Получаем данные персонажа
        char_data = sympathy_characters.get(char_key, None)
        if char_data is None:
            var_name = char_key + "_sympathy"
        else:
            var_name = char_data["var"]
        
        # Получаем текущее значение (из store, не persistent - для rollback)
        old_value = getattr(renpy.store, var_name, 0)
        
        # Вычисляем новое значение с ограничением
        new_value = old_value + value
        new_value = max(min_val, min(max_val, new_value))
        
        # Сохраняем новое значение в store (поддерживает rollback)
        setattr(renpy.store, var_name, new_value)
        
        # Добавляем персонажа в "известные"
        renpy.store.known_characters.add(char_key)
        
        # Проигрываем звук
        #if value > 0 and renpy.loadable(up_sound):
            #renpy.sound.play(up_sound, channel="sound")
        #elif value < 0 and renpy.loadable(down_sound):
            #renpy.sound.play(down_sound, channel="sound")
        
        # ============================================
        # КЕЙС 1: Все персонажи (включая Louise)
        # Показываем блок: [Уровень симпатии] [Иконка персонажа] [UP/DOWN]
        # ============================================
        #renpy.show_screen("sympathy_notification", 
                         # char_key=char_key,
                          #change_value=value)
        
        # Ждём завершения анимации первого блока
        #renpy.pause(2.8, hard=False)
        
        # Скрываем первый экран
        #renpy.hide_screen("sympathy_notification")
        
        # ============================================
        # КЕЙС 2: Только для Louise - дополнительный блок с прогресс-баром
        # После задержки показываем прогресс-бар + [tsun/dere] [UP]
        # ============================================
       # if char_key == "louise":
            # Небольшая задержка перед вторым блоком
            #renpy.pause(0.3, hard=False)
            
            # Показываем второй экран для Louise (прогресс-бар + tsun/dere)
           # renpy.show_screen("sympathy_louise_second", 
                            #  change_value=value,
                            ##  new_value=new_value)
            
            # Ждём завершения анимации
           # renpy.pause(2.8, hard=False)
            
            # Скрываем экран
           # renpy.hide_screen("sympathy_louise_second")
        
        return new_value
    
    def get_sympathy(char_key="louise"):
        """Получить текущее значение симпатии персонажа"""
        char_data = sympathy_characters.get(char_key, None)
        if char_data:
            var_name = char_data["var"]
        else:
            var_name = char_key + "_sympathy"
        
        return getattr(renpy.store, var_name, 0)
    
    def set_sympathy(char_key, value, min_val=-100, max_val=100):
        """Установить значение симпатии напрямую (без анимации)"""
        char_data = sympathy_characters.get(char_key, None)
        if char_data:
            var_name = char_data["var"]
        else:
            var_name = char_key + "_sympathy"
        
        value = max(min_val, min(max_val, value))
        setattr(renpy.store, var_name, value)
        
        # Добавляем в известные
        renpy.store.known_characters.add(char_key)
        
        return value
    
    def is_character_known(char_key):
        """Проверить, известен ли персонаж"""
        return char_key in renpy.store.known_characters

# ============================================
# ПРИМЕР ИСПОЛЬЗОВАНИЯ
# ============================================
# 
# В скрипте игры:
#
# # Показать HUD иконку меню симпатии
# $ show_sympathy_hud()
#
# # Скрыть HUD иконку
# $ hide_sympathy_hud()
#
# # Переключить видимость
# $ toggle_sympathy_hud()
#
# # Повысить симпатию Луизы на 10 (покажет оба блока + прогресс-бар)
# $ update_sympathy(10, "louise")
#
# # Понизить симпатию Луизы на 5 (покажет оба блока + прогресс-бар)
# $ update_sympathy(-5, "louise")
#
# # Повысить симпатию Haruna на 15 (покажет только первый блок, без прогресс-бара)
# $ update_sympathy(15, "haruna")
#
# # Получить текущую симпатию (диапазон -100 до +100)
# $ current = get_sympathy("louise")
#
# # Проверить, известен ли персонаж
# if is_character_known("haruna"):
#     "Haruna уже известна!"
#
# # Показать экран просмотра симпатии (видны только известные персонажи)
# call screen sympathy_status
# ============================================

```

## Файл: `scripts\menus\game_menu_screen.rpy`

```renpy

## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size 75
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45




label gallery:
    # Логика просмотра галереи/CG
    return

label music:
    # Логика теста звука / музыкальный плеер
    return

```

## Файл: `scripts\menus\main_menu_screen.rpy`

```renpy

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    tag menu

    add gui.main_menu_background

    frame:
        style "main_menu_frame"

    use navigation

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


```

## Файл: `scripts\menus\mobile_screen.rpy`

```renpy

################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900


```

## Файл: `scripts\menus\navigation_screen.rpy`

```renpy

################################################################################
## Main and Game Menu Screens
################################################################################

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("New Game") action Start()
            textbutton _("Load Game") action ShowMenu("load")
            
            #textbutton _("Gallery") action Jump("gallery")
            #textbutton _("Music") action Jump("music")
            #textbutton _("Scene Select") action ShowMenu("gallery")
            null height 20
                
        else:
            ## Стандартные кнопки для игрового меню
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")
            textbutton _("Load") action ShowMenu("load")
            
            if _in_replay:
                textbutton _("End Replay") action EndReplay(confirm=True)
            elif not main_menu:
                textbutton _("Main Menu") action MainMenu()

        textbutton _("Options") action ShowMenu("preferences")        
        textbutton _("About") action ShowMenu("about")
                
        ##if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            ##textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):
            null height 10
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


```

## Файл: `scripts\menus\quick_menu.rpy`

```renpy

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

# ============================================================================
# ОБНОВЛЁННОЕ БЫСТРОЕ МЕНЮ (QUICK MENU)
# В стиле Zero no Tsukaima с добавлением кнопки инвентаря
# ============================================================================

style quick_menu_hbox:
    xalign 0.5
    yalign 1.0
    yoffset -10
    spacing 0

style quick_button:
    #background Frame("gui/button/quick_idle.png", 5, 5, 5, 5)
    #hover_background Frame("gui/button/quick_hover.png", 5, 5, 5, 5)
    # Fallback стили
    background "#8b5a2b99"
    hover_background "#a0603099"
    padding (12, 6, 12, 6)
    
style quick_button_text:
    color "#e8d5b8"
    hover_color "#ffffff"
    size 16
    outlines [(1, "#3d2817", 0, 0)]


screen quick_menu():
    zorder 100

    if False:
        hbox:
            style "quick_menu_hbox"
            
            # Основные игровые функции
            # textbutton _("Back"):
            #     style "quick_button"
            #     text_style "quick_button_text"
            #     action Rollback()
            
            textbutton _("History"):
                style "quick_button"
                text_style "quick_button_text"
                action ShowMenu('history')
            
            textbutton _("Skip"):
                style "quick_button"
                text_style "quick_button_text"
                action Skip()
                alternate Skip(fast=True, confirm=True)
            
            textbutton _("Auto"):
                style "quick_button"
                text_style "quick_button_text"
                action Preference("auto-forward", "toggle")
            
            # Разделитель визуальный
            null width 15
            
            # НОВОЕ: Инвентарь
            textbutton "Items":
                style "quick_button"
                text_style "quick_button_text"
                action ShowMenu('inventory')
            
            # Разделитель
            null width 15
            
            # Системные функции
            textbutton _("Save"):
                style "quick_button"
                text_style "quick_button_text"
                action ShowMenu('save')
            
            textbutton _("Q.Save"):
                style "quick_button"
                text_style "quick_button_text"
                action QuickSave()
            
            textbutton _("Q.Load"):
                style "quick_button"
                text_style "quick_button_text"
                action QuickLoad()
            
            textbutton _("Prefs"):
                style "quick_button"
                text_style "quick_button_text"
                action ShowMenu('preferences')


```

## Файл: `scripts\overlay\notify_screen.rpy`

```renpy
## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")
```

## Файл: `scripts\overlay\overlay_screen.rpy`

```renpy
#show overlay img with text

# styles presets
default overlay_styles = {
    'black': {
        'title': { 'size': 78, 'color': "#000000", 'outlines': [(2, "#000000", 0, 0), (1, "#000000", 2, 2)] },
        'subtitle': { 'size': 50, 'color': "#000000", 'outlines': [(1, "#000000", 0, 0)] },
        'line': { 'color': "#000000", 'outline_color': "#000000", 'thickness': 6, 'width': 1000 }
    },
    'white': {
        'title': { 'size': 90, 'color': "#ffffff", 'outlines': [(2, "#ffffff", 0, 0), (1, "#ffffff", 2, 2)] },
        'subtitle': { 'size': 48, 'color': "#ffffff", 'outlines': [(1, "#ffffff", 0, 0)] },
        'line': { 'color': "#ffffff", 'outline_color': "#ffffff", 'thickness': 6, 'width': 1000 }
    },
    'beige': {
        'title': { 'size': 78, 'color': "#000000", 'outlines': [(2, "#d9dac6", 0, 0), (1, "#d9dac6", 2, 2)] },
        'subtitle': { 'size': 50, 'color': "#000000", 'outlines': [(1, "#d9dac6", 0, 0)] },
        'line': { 'color': "#000000", 'outline_color': "#d9dac6", 'thickness': 6, 'width': 1000 }
    },
    'orange': {
        'title': { 'size': 78, 'color': "#fe9e5e", 'outlines': [(2, "#875109", 0, 0), (1, "#875109", 2, 2)] },
        'subtitle': { 'size': 50, 'color': "#fe9e5e", 'outlines': [(1, "#875109", 0, 0)] },
        'line': { 'color': "#fd9754", 'outline_color': "#875109", 'thickness': 6, 'width': 1000 }
    },
}


# overlay screen
screen chapter_title_overlay(title_text, show_subtitle=False, style_dict={}):
    zorder 100
    vbox:
        align (0.5, 0.45)  # Центрируем по X и сдвигаем на 40% по Y
        xfill False        # Запрещаем растягивать vbox на всю ширину экрана
        spacing 20         # Отступы между заголовком, линией и подзаголовком

        # Заголовок
        text title_text:
            xalign 0.5
            text_align 0.5
            antialias True
            size style_dict['title']['size']
            color style_dict['title']['color']
            outlines style_dict['title']['outlines']

        # Линия и подзаголовок
        if show_subtitle:
            $ line_width = style_dict['line']['width']
            $ line_thickness = style_dict['line']['thickness']
            $ glow_color = style_dict['line']['outline_color']

            # Контейнер для линии. Убран yalign 0.5, добавлены фиксированные размеры
            fixed:
                xalign 0.5
                xsize line_width + 14
                ysize line_thickness + 14
                
                # Основная линия
                add Solid(style_dict['line']['color']) xysize (line_width, line_thickness) xalign 0.5 yalign 0.5

            # Подзаголовок
            text "The Familiar of Zero":
                xalign 0.5
                text_align 0.5
                antialias True
                size style_dict['subtitle']['size']
                color style_dict['subtitle']['color']
                outlines style_dict['subtitle']['outlines']


# overlay func
label overlay_screen(scene_name=None, title_text="", show_subtitle=False, text_mode='beige', delay=2.0, isUseBlur=True, sound_path=None):
    # get Style from presets
    $ current_style = overlay_styles.get(text_mode, overlay_styles['beige'])

    # clear old
    hide screen chapter_title_overlay
    pause 0.05

    # show bg
    if scene_name is None:
        scene black with dissolve
        $ show_subtitle = False ## no need
    elif isUseBlur is True:
        scene expression "bg " + scene_name + "_blurred" at bg_center with dissolve
    else:
        scene expression "bg " + scene_name at bg_center with dissolve
    pause 0.2

    # show title
    show screen chapter_title_overlay(
        title_text=title_text,
        show_subtitle=show_subtitle,
        style_dict=current_style
    )
    with dissolve

    if sound_path is not None:
        voice sound_path
    
    # pause
    $ renpy.pause(delay, hard=True)

    # hide title
    hide screen chapter_title_overlay
    with dissolve
    pause 0.2

    # return original scene
    if scene_name is not None and isUseBlur is True:
        scene expression "bg " + scene_name at bg_center with dissolve
        pause 0.2
    return
```

## Файл: `scripts\system\about_screen.rpy`

```renpy

## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

# ==== ABOUT ====
define gui.about = _p("""
This project is a non-commercial, amateur development created by fans for fans.
All rights to the characters, setting, names, and other elements of Zero no tsukaima belong to their respective owners.
""")

define gui.credits_text = _p("""
Created by {a=https://t.me/timeasoff}timeasoff{/a}.
Guide to the entire ecosystem of Zero no Tsukaima on the {a=https://t.me/ZeroNoTsukaima_EN}Halkeginia Map{/a}.
""")

define gui.support = _p("""
You can support me here: {a=https://t.me/timeasoff_support}Support{/a}
""")

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]"

            if gui.credits_text:
                text "[gui.credits_text!t]"

            if gui.support:
                text "[gui.support!t]"    

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


```

## Файл: `scripts\system\help_screen.rpy`

```renpy
## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



```

## Файл: `scripts\system\history_screen.rpy`

```renpy
## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5



```

## Файл: `scripts\system\load_save_screen.rpy`

```renpy

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


```

## Файл: `scripts\system\preferences_screen.rpy`

```renpy

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("All Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                vbox:
                    label _("Language")
                    textbutton "English" action [
                        Language(None),
                    ]
                    textbutton "Russian" action [
                        Language("russian"),
                    ]
                    textbutton "Japanese" action [
                        Language("japanese"),
                    ]


                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675



```

## Файл: `scripts\system\skip_screen.rpy`

```renpy
## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"




```

