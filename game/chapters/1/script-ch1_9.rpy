# комната луизы. ОБЩИЙ СБОР!
label ch1_9:
    $ fade_fx("louise_room", new_music="t18", sprites=("l 1"), duration=2)
    voice "ch1.9_l_001"
    l "Right then, everyone is assembled."

    $ show_sprites(("k 1", "t 1"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.9_k_001"
    k "Yes, everyone has gathered."

    t "..."

    $ show_sprites(("g 2 shy", "ha 1"), anim_in="slide_right", anim_out="slide_right")
    voice "ch1.9_g_001"
    g "Oh, lovely young lady. Would you be willing to become my personal maid?"

    $ show_sprites(("g 2 shy", "ha 1 sad"))
    voice "ch1.9_ha_001"
    ha "Eh, umm…"

    $ show_sprites(("g 2 shy", "m 4 angry"))
    voice "ch1.9_m_001"
    m "Gish! You're drooling over every girl you see again!"

    $ show_sprites(("g 2 happy", "m 4 angry"))
    voice "ch1.9_g_002"
    g "Oh my, are you jealous? My dear Montmorency."

    voice "ch1.9_g_003"
    g "But don't worry. My heart will never forget you."

    $ show_sprites(("g 2 happy", "m 1 angry"))
    voice "ch1.9_m_002"
    m "All you do is say you won't forget me, but then you're immediately checking out other girls! How am I supposed not to worry after that?"

    $ show_sprites(("g 2 happy", "s 1 angry"))
    voice "ch1.9_s_001"
    s "Listen, did you even need to come? Take one look, and that's it—goodbye."

    $ show_sprites(("g 1 sad", "s 1 angry"))
    voice "ch1.9_g_004"
    g "What an impolite tone. I'm offering to lend you my strength, so you shouldn't speak to me like that."

    $ show_sprites(("g 1 sad", "l 1 sad"))
    voice "ch1.9_l_002"
    l "It can't be helped. Montmorency let it slip. Since it's come to this, I'll accept your help."

    $ show_sprites(("g 1 angry", "l 1 sad"))
    voice "ch1.9_g_005"
    g "Mmmmm… That's a rather humiliating way to put it, but… fine…"

    $ show_sprites(("g 1 angry", "k 1"))
    voice "ch1.9_k_002"
    k "Yes, yes. That's enough commotion."

    voice "ch1.9_k_003"
    k "First, we need to decide where she should stay… That's the biggest problem."

    $ show_sprites(("g 1 angry", "s 3 sad"))
    voice "ch1.9_s_002"
    s "Where she should stay… Can't it be here?"

    $ show_sprites(("g 2", "s 3 sad"))
    voice "ch1.9_g_006"
    g "Hiding a commoner in secret is a serious matter. In any case, it seems to me that this situation is beyond our capabilities."


    $ show_sprites(("l 1", "s 3 sad"))
    voice "ch1.9_l_003"
    l "Oh, it's fine. We'll have this girl leave right away."

    $ show_sprites(("l 1", "s 1 angry"))
    voice "ch1.9_s_003"
    s "What!? Wait, Louise!"

    $ show_sprites(("l 1 angry", "s 1 angry"))
    voice "ch1.9_l_004"
    l "What?"

    voice "ch1.9_s_004"
    s "You…"

    menu: 
        "Come on, can't something be done about that?":
            $ show_sprites(("l 1 angry", "s 3 sad"))
            voice "ch1.9_s_005"
            s "Come on, can't something be done about that?"

            voice "ch1.9_l_005"
            l "What do you mean by 'something'?"

            voice "ch1.9_l_006"
            l "Do you seriously think we're capable of hiding a commoner? That's just unrealistic."

            voice "ch1.9_s_006"
            s "B-but isn't that cruel?"

            $ update_sympathy(20, char_key="louise")

        "Don't say such awful things!":
            $ show_sprites(("l 1 angry", "s 1 angry"))
            voice "ch1.9_s_005-2"
            s "Don't say such awful things!"

            voice "ch1.9_l_005-2"
            l "What's awful about it? I'm just stating the obvious."

            $ update_sympathy(-20, char_key="louise")

            $ show_sprites(("l 1 angry", "s 3 angry"))
            voice "ch1.9_s_006-2"
            s "You want to leave her all alone in this world! That's exactly what I mean when I say 'awful'!"

    $ show_sprites(("l 1", "s 3 angry"))
    voice "ch1.9_l_007"
    l "Actually, we brought this girl to the academy to look after her, since she had passed out on the road."

    $ show_sprites(("l 1", "s 3 sad"))
    voice "ch1.9_s_007"
    s "W-well, yeah. That's true, but…"

    voice "ch1.9_l_008"
    l "She seems to have recovered after resting for the night, so it is improper for an outsider to remain at the academy."

    voice "ch1.9_l_009"
    l "Am I saying something wrong?"

    voice "ch1.9_s_008"
    s "T-That's... Your logic isn't wrong, but... but that's just heartless!"

    $ show_sprites(("l 1 angry", "s 3 sad"))
    voice "ch1.9_l_010"
    l "Then how are we supposed to take care of her from now on?"

    voice "ch1.9_l_011"
    l "We're not talking about a dog or a cat here. It's obviously impossible to just keep her."

    $ show_sprites(("l 1 angry", "s 3 angry"))
    voice "ch1.9_s_009"
    s "What did you say...?!"

    $ show_sprites(("l 1 angry", "si 1 sad"))
    voice "ch1.9_si_001"
    si "U-Um, Saito-san, Miss Valliere, please calm down"

    $ show_sprites(("l 1 angry", "k 4"))
    voice "ch1.9_k_004"
    k "Hmph..."

    $ show_sprites(("l 1 angry", "k 4 happy"))
    voice "ch1.9_k_005"
    k "Hey, Louise? Could it be... you're jealous?"

    voice "ch1.9_l_012"
    l "Huh?{#a}"

    $ show_sprites(("l 1 angry", "k 1 happy"))
    voice "ch1.9_k_006"
    k "Are you trying to kick her out just because Saito is so devoted to her?"

    $ show_sprites(("l 3 angry", "k 1 happy"))
    voice "ch1.9_l_013"
    l "Wha...! I-I-I don't mean it like that!"

    $ show_sprites(("l 3 angry", "k 1"))
    voice "ch1.9_k_007"
    k "After all, sheltering her doesn't mean we can keep it up indefinitely, right?"

    voice "ch1.9_k_008"
    k "Still, that level of desperation is nothing short of jealousy!"

    $ show_sprites(("l 1 angry", "k 1"))
    voice "ch1.9_l_014"
    l "That can't be! Why would I be jealous of this Saito!" (С

    $ show_sprites(("l 1 angry", "k 1 happy"))
    voice "ch1.9_k_009"
    k "Then that's fine. Even if it's just for a while, why not shelter her?" 

    $ show_sprites(("l 1 sad", "k 1 happy"))
    voice "ch1.9_l_015"
    l "Ugh..."

    $ show_sprites(("l 1 sad", "s 1 sad"))
    voice "ch1.9_s_010"
    s "Louise, please. Just let her stay for a while."

    $ show_sprites(("l 3 angry", "s 1 sad"))
    voice "ch1.9_l_016"
    l "Fine! We just need to hide her for a while, right!"

    $ show_sprites(("l 3 angry", "k 4 happy"))
    voice "ch1.9_k_010"
    k "That settles it."

    $ show_sprites(("l 3 angry", "s 1"))
    voice "ch1.9_s_011"
    s "...Thanks, Louise."

    $ show_sprites(("ha 1 happy", "s 1"))
    voice "ch1.9_ha_002"
    ha "Thank you, Hiraga-kun." 

    $ show_sprites(("ha 1 happy", "s 3 shy"))
    voice "ch1.9_s_012"
    s "Huh? N-No, I didn't do anything..."

    $ show_sprites(("ha 1 happy", "s 3 happy"))
    voice "ch1.9_s_013"
    s "I mean, being thrown into this world all alone is tough, isn't it?"

    $ show_sprites(("g 1", "s 3 happy"))
    voice "ch1.9_g_007"
    g "But if she came from the same place as Saito, 'Japan', doesn't she have a master who summoned her?"

    $ show_sprites(("g 1", "s 1 sad"))
    voice "ch1.9_s_014"
    s "Eh?{#e?}"

    voice "ch1.9_g_008"
    g "I'm just saying that, just like Louise, she might have a master who summoned her."

    $ show_sprites(("g 1", "s 1"))
    voice "ch1.9_s_015"
    s "Ah... I see. That possibility does exist, doesn't it." 

    $ show_sprites(("g 1", "l 1 angry"))
    voice "ch1.9_l_017"
    l "So you're saying the people who attacked us are actually the mages who summoned her, or their subordinates?"

    $ show_sprites(("g 2 angry", "l 1 angry"))
    voice "ch1.9_g_009"
    g "The people who attacked?"
    

    #! диалоги диалоги диалоги

    menu:
        "Isn't it possible that we overlooked something?":
            "ss"

        "Was it by chance that she came to this world?":
            "ss"


    #! прыгаем на новый файл когда утро (последний файл для первой главы)
    jump ch1_10
    return
        
    






