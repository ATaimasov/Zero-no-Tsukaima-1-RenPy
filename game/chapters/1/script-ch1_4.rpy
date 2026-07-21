# louise's room night
label ch1_4:
    $ fade_fx("louise_room_night", new_music="t19", sprites=("s 5"))
    voice "ch1.4_s_001"
    s "Well then, I guess I'll call it a night."

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

    window hide
    $ show_sprites(None, anim="slide_right") 
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

    $ dissolve_fx("sky_night")
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