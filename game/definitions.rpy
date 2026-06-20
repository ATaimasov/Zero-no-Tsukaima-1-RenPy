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


# ==== ABOUT ====
define gui.about = _p("""
This project is a non-commercial, amateur development created by fans for fans.
All rights to the characters, setting, names, and other elements of Zero no tsukaima belong to their respective owners.
""")

define gui.credits_text = _p("""
Created by {a=https://t.me/timeasoff}timeasoff{/a}.
Guide to the entire ecosystem of Zero no Tsukaima on the {a=https://t.me/ZeroNoTsukaima_EN}Halkeginia Map{/a}.
Made with {a=https://www.renpy.org/}Ren'Py{/a}
""")


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
