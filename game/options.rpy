define config.default_language = "english"

init python:
    _language_fonts = {
        "english": "fonts/NotoSans.ttf",
        "russian": "fonts/NotoSans.ttf",
        "japanese": "fonts/NotoSansJP.ttf"
    }

    def update_ui_font():
        # Читаем язык из постоянного хранилища (где его сохраняет кнопка Language)
        lang = persistent._language or config.default_language or "english"
        target_font = _language_fonts.get(lang, "fonts/NotoSans.ttf")

        gui.text_font = target_font
        gui.name_text_font = target_font
        gui.interface_text_font = target_font
        gui.button_text_font = target_font
        gui.choice_button_text_font = target_font
        gui.label_text_font = target_font
        gui.input_text_font = target_font

        style.default.font = target_font
        style.rebuild() # Пересобирает стили, чтобы шрифт применился мгновенно

    # Применяем шрифт при запуске игры
    update_ui_font()


define build.name = "ZnT1"
define config.version = "0.0.1"
define config.name = _("Zero no Tsukaima: Shou-akuma to Harukaze no Concerto (Unnoficial remaster)")

#define config.auto_voice = "audio/voices/{id}.wav"
define config.voice_filename_format = "audio/voices/{filename}.wav"

define gui.show_name = False

define config.developer = True


## Sounds and music ############################################################

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.main_menu_music = audio.t2


## Transitions #################################################################

define config.enter_transition = dissolve
define config.exit_transition = dissolve

## Between screens of the game menu.

define config.intra_transition = dissolve

## A transition that is used after a game has been loaded.

define config.after_load_transition = None

## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## Window management ###########################################################

define config.window = "auto"

## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. 
default preferences.text_cps = 0

## The default auto-forward delay.
default preferences.afm_time = 15


define config.save_directory = "ZnT1-1777760105"
define config.window_icon = "gui/window_icon.png"

#define build.itch_project = "renpytom/test-project"
