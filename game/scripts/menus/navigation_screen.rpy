
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

