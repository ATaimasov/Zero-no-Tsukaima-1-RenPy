
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

    if quick_menu:
        hbox:
            style "quick_menu_hbox"
            
            # Основные игровые функции
            textbutton _("Back"):
                style "quick_button"
                text_style "quick_button_text"
                action Rollback()
            
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

