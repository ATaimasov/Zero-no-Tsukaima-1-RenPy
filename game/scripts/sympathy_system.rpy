image gui_sympathy_bar = "gui/sympathy/bar.png"
image gui_sympathy_arrow = "gui/sympathy/arrow.png"
image gui_sympathy_up = "gui/sympathy/up.png"
image gui_sympathy_down = "gui/sympathy/down.png"

default louise_sympathy = 50

transform sympathy_bar_anim:
    xalign 0.05
    yalign 0.04
    zoom 0.6
    alpha 0.0
    linear 0.2 alpha 1.0   # appear
    pause 1.5              
    linear 0.3 alpha 0.0   # dissapear

transform sympathy_arrow_anim(val, max_val=100, base_range_px=240):
    xalign 0.17
    yalign 0.08
    zoom 0.6
    alpha 0.0
    linear 0.2 alpha 1.0   # appear
    linear 0.8 xoffset (float(val) / max_val * base_range_px) # motion
    pause 0.7              
    linear 0.3 alpha 0.0   # dissapear

transform sympathy_icon_anim:
    xalign 0.98
    yalign 0.1
    zoom 0.5
    alpha 0.0
    linear 0.2 alpha 1.0   # appear
    pause 1.5              
    linear 0.3 alpha 0.0   # dissapear

transform sympathy_text_anim:
    xalign 0.99
    yalign 0.03
    alpha 0.0
    linear 0.3 alpha 1.0   # appear
    pause 1.5              
    linear 0.3 alpha 0.0   # dissapear

# 4. Экран интерфейса
screen sympathy_ui(change_value, max_value=100, show_bar=False, display_text="Sympathy level"):
    zorder 100
    
    # progress bar
    if show_bar:
        add "gui_sympathy_bar" at sympathy_bar_anim
        add "gui_sympathy_arrow" at sympathy_arrow_anim(change_value, max_value, 240)
    
    # up/down icon 
    if change_value > 0 or show_bar is True:
        add "gui_sympathy_up" at sympathy_icon_anim
    elif change_value < 0:
        add "gui_sympathy_down" at sympathy_icon_anim
    
    # up/down text 
    text display_text at sympathy_text_anim:
        size 30
        color "#fe9e5e"
        outlines [(2, "#875109", 0, 0), (1, "#875109", 2, 2)]

init python:
    def update_sympathy(value, var_name="louise_sympathy", max_val=100, 
                        showProgressBar=False,
                        up_sound="audio/sfx/sympathy_up.wav", 
                        down_sound="audio/sfx/sympathy_down.wav"):
        store = renpy.store
        current = getattr(store, var_name, 50)
        
        new_val = current + value
        new_val = max(0, min(max_val, new_val))
        
        setattr(store, var_name, new_val)
        
        # sound
        if value > 0:
            renpy.sound.play(up_sound, channel="sound")
        elif value < 0:
            renpy.sound.play(down_sound, channel="sound")
        
        # show sympathy up/down
        renpy.show_screen("sympathy_ui", change_value=value, max_value=max_val)
        renpy.pause(2.2, hard=False)
        renpy.hide_screen("sympathy_ui")
        
        # show progress bar with tsun/dere
        if showProgressBar:
            bar_text = "Dere" if value > 0 else "Tsun"
            renpy.show_screen("sympathy_ui", change_value=value, max_value=max_val, show_bar=True, display_text=bar_text)
            renpy.pause(2.2, hard=False)
            renpy.hide_screen("sympathy_ui")
            
        return new_val