define config.default_language = "english"

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
