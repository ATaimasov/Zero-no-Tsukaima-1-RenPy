# ready action for quit-entering via door
label open_door(quit_side="left", new_bg=None, stop_music=False):
    window hide
    if quit_side == "left":
        $ show_sprites(None, anim="slide_left")
    else:
        $ show_sprites(None, anim="slide_right")

    # трюк  ̶с̶ ̶ж̶̶̶о̶̶̶п̶̶̶о̶̶̶й̶̶̶   с black сделан, чтобы звук закрытия двери был с анимацией затухания
    pause(0.5)
    play sound open_door
    if stop_music is True:
        stop music fadeout 1.0
    pause(1.0)

    if new_bg is None:
        $ fade_fx("black", bg_position="default")
    else:
        $ fade_fx(new_bg)
    play sound close_door
    pause (1.0)
    return