
## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

# ==== ABOUT ====
define gui.about ="""This project is a non-commercial, amateur development created by fans for fans. 
All rights to the characters, setting, names, and other elements of Zero no tsukaima belong to their respective owners."""

define gui.credits_text = """Prepared by {a=https://t.me/timeasoff}timeasoff{/a}. Translation assistance provided by {a=https://t.me/Alex_Hrst}Alex_Hrst{/a}.
Project available on {a=https://github.com/ATaimasov/Zero-no-Tsukaima-1-RenPy}GitHub{/a}. You can contribute to the translation❗

My channel is here: {a=https://t.me/halkeginia}Halkeginia Archives{/a}.
A guide to all Zero no Tsukaima channels and projects can be found on the {a=https://t.me/ZeroNoTsukaima_RU}Halkeginia Map{/a}."""

define gui.support = "You can leave your thanks {a=https://t.me/timeasoff_support}here{/a} ☕"

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
                text "[gui.about!t]\n"

            if gui.credits_text:
                text "[gui.credits_text!t]"
                spacing 10

            if gui.support:
                text "[gui.support!t]"    

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

