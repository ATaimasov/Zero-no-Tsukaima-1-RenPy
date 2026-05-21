# ============================================================================
# ZERO NO TSUKAIMA - REMASTER BATTLE MENU
# Полноэкранное меню подготовки к бою в стиле PS2 игры
# ============================================================================

# Данные персонажей
default battle_characters = {
    'saito': {
        'name': 'Сайто',
        'hp': 100,
        'max_hp': 100,
        'mp': 50,
        'max_mp': 50,
        'portrait': 'images/portraits/saito.png',
        'in_party': True
    },
    'louise': {
        'name': 'Луиза',
        'hp': 80,
        'max_hp': 80,
        'mp': 80,
        'max_mp': 80,
        'portrait': 'images/portraits/louise.png',
        'in_party': True
    }
}

# Выбранный персонаж для просмотра
default selected_character = None

init python:
    def show_battle_menu():
        """Вызывает экран меню подготовки к бою"""
        renpy.call_screen("battle_menu")
    
    def get_party_members():
        """Возвращает список персонажей в отряде"""
        return [char for key, char in store.battle_characters.items() if char.get('in_party', False)]

# ============================================================================
# СТИЛИ В ДУХЕ PS2 ВЕРСИИ (деревянная текстура, тёплые тона)
# ============================================================================

init:
    # === ОСНОВНЫЕ ЦВЕТА ===
    # Деревянная тема как в оригинале
    define gui.battle_wood_dark = "#5c3d2e"      # Тёмное дерево (рамки)
    define gui.battle_wood_medium = "#8b5a2b"    # Среднее дерево (кнопки)
    define gui.battle_wood_light = "#a06030"     # Светлое дерево (hover)
    define gui.battle_panel_bg = "#e8d5b8"       # Бежевый фон панелей
    define gui.battle_panel_inner = "#dcbfa6"    # Внутренний фон
    define gui.battle_text_light = "#fff8e7"     # Светлый текст
    define gui.battle_text_shadow = "#3d2817"    # Тень текста

    # === ГЛАВНЫЙ КОНТЕЙНЕР (полноэкранный) ===
    style battle_fullscreen:
        background "#00000099"  # Полупрозрачный затемняющий слой

    # === ЗАГОЛОВОК МЕНЮ ===
    style battle_title_frame:
        background Frame("gui/battle/header_bg.png", 20, 10, 20, 10) 
        # Fallback если нет изображения:
        # background "#8b5a2b"
        padding (30, 8, 30, 8)
        xminimum 400

    style battle_title_text:
        color "#fff8e7"
        size 32
        bold True
        outlines [(2, "#3d2817", 0, 0)]
        text_align 0.5

    # === ОСНОВНАЯ ПАНЕЛЬ ===
    style battle_main_panel:
        background Frame("gui/battle/panel_bg.png", 15, 15, 15, 15)
        # Fallback:
        # background "#e8d5b8"
        padding (20, 20, 20, 20)

    # === КНОПКИ МЕНЮ (деревянный стиль) ===
    style battle_menu_button:
        background Frame("gui/battle/button_idle.png", 15, 8, 15, 8)
        hover_background Frame("gui/battle/button_hover.png", 15, 8, 15, 8)
        selected_background Frame("gui/battle/button_selected.png", 15, 8, 15, 8)
        # Fallback:
        # background "#8b5a2b"
        # hover_background "#a06030"
        padding (20, 12, 20, 12)
        xsize 280
        ysize 55

    style battle_menu_button_text:
        color "#fff8e7"
        hover_color "#ffffff"
        size 22
        bold True
        text_align 0.5
        outlines [(1, "#3d2817", 1, 1)]

    # === КНОПКА "НАЧАТЬ БОЙ" (выделенная) ===
    style battle_start_button:
        background Frame("gui/battle/button_start_idle.png", 15, 8, 15, 8)
        hover_background Frame("gui/battle/button_start_hover.png", 15, 8, 15, 8)
        # Fallback:
        # background "#c9763c"
        # hover_background "#e08850"
        padding (20, 15, 20, 15)
        xsize 280
        ysize 60

    style battle_start_button_text:
        color "#ffffff"
        hover_color "#ffffd0"
        size 26
        bold True
        text_align 0.5
        outlines [(2, "#5c3d2e", 0, 0)]

    # === ПАНЕЛЬ УЧАСТНИКОВ БОЯ ===
    style battle_participants_frame:
        background Frame("gui/battle/participants_bg.png", 12, 12, 12, 12)
        # Fallback:
        # background "#dcbfa6"
        padding (15, 15, 15, 15)

    style battle_participants_header:
        background "#8b5a2b"
        padding (15, 8, 15, 8)

    style battle_participants_header_text:
        color "#fff8e7"
        size 24
        bold True
        text_align 0.5
        outlines [(1, "#3d2817", 1, 1)]

    # === СЛОТ ПЕРСОНАЖА ===
    style battle_char_slot:
        background Frame("gui/battle/char_slot_bg.png", 8, 8, 8, 8)
        # Fallback:
        # background "#5c3d2e"
        padding (8, 8, 8, 8)

    style battle_char_slot_hover:
        background Frame("gui/battle/char_slot_hover.png", 8, 8, 8, 8)
        # Fallback:
        # background "#7a5040"
        padding (8, 8, 8, 8)

    # === HP/MP БАРЫ ===
    style battle_hp_bar:
        left_bar Solid("#4caf50")  # Зелёный HP
        right_bar Solid("#2d2d2d")
        thumb None
        ysize 14
        xsize 140

    style battle_mp_bar:
        left_bar Solid("#29b6f6")  # Голубой MP
        right_bar Solid("#2d2d2d")
        thumb None
        ysize 14
        xsize 140

    style battle_bar_label:
        color "#fff8e7"
        size 14
        bold True
        outlines [(1, "#000000", 0, 0)]

    # === ПАНЕЛЬ ИНФОРМАЦИИ О ПЕРСОНАЖЕ ===
    style battle_info_panel:
        background "#e8d5b8"
        padding (15, 15, 15, 15)

    style battle_char_name_text:
        color "#5c3d2e"
        size 20
        bold True

    # === ПУСТОЙ СЛОТ ===
    style battle_empty_slot:
        background "#4a4a4a"
        xsize 120
        ysize 120


# ============================================================================
# ЭКРАН МЕНЮ ПОДГОТОВКИ К БОЮ
# ============================================================================

screen battle_menu():
    tag menu
    modal True
    
    # Полноэкранный затемняющий фон
    add "#00000088"
    
    # Фоновое изображение (пентаграмма как в оригинале)
    # add "gui/battle/battle_bg.png" xalign 0.5 yalign 0.5
    
    # Главный контейнер
    frame:
        style_prefix "battle"
        xfill True
        yfill True
        background None
        padding (40, 30, 40, 30)
        
        vbox:
            xfill True
            yfill True
            spacing 15
            
            # === ЗАГОЛОВОК ===
            frame:
                style "battle_title_frame"
                xalign 0.5
                background "#8b5a2b"
                padding (40, 10)
                
                text "Подготовка к бою" style "battle_title_text"
            
            # === ОСНОВНАЯ ОБЛАСТЬ ===
            hbox:
                spacing 30
                xalign 0.5
                yalign 0.5
                
                # --- ЛЕВОЕ МЕНЮ ---
                vbox:
                    spacing 12
                    xsize 300
                    
                    # Предметы/Инвентарь
                    textbutton "Предметы":
                        style "battle_menu_button"
                        text_style "battle_menu_button_text"
                        action ShowMenu("inventory")  # Или ваш экран инвентаря
                    
                    # Просмотр персонажей
                    textbutton "Персонажи":
                        style "battle_menu_button"
                        text_style "battle_menu_button_text"
                        action ShowMenu("characters")  # Экран информации о персонажах
                    
                    # Выбор отряда (если есть больше персонажей)
                    textbutton "Выбор отряда":
                        style "battle_menu_button"
                        text_style "battle_menu_button_text"
                        action ShowMenu("party_select")
                    
                    # Разделитель
                    null height 20
                    
                    # Вернуться (закрыть меню без боя)
                    textbutton "Назад":
                        style "battle_menu_button"
                        text_style "battle_menu_button_text"
                        action Return("cancel")
                    
                    # Большой разделитель перед кнопкой боя
                    null height 40
                    
                    # НАЧАТЬ БОЙ - главная кнопка
                    textbutton "Начать бой":
                        style "battle_start_button"
                        text_style "battle_start_button_text"
                        action Return("start_battle")
                
                # --- ПРАВАЯ ПАНЕЛЬ: УЧАСТНИКИ БОЯ ---
                frame:
                    style "battle_participants_frame"
                    background "#dcbfa6"
                    xsize 650
                    ysize 450
                    
                    vbox:
                        spacing 15
                        xfill True
                        
                        # Заголовок панели
                        frame:
                            style "battle_participants_header"
                            xalign 0.5
                            xsize 300
                            
                            text "Участники боя" style "battle_participants_header_text" xalign 0.5
                        
                        # Слоты персонажей
                        hbox:
                            spacing 20
                            xalign 0.5
                            yalign 0.3
                            
                            for char_key, char_data in battle_characters.items():
                                if char_data.get('in_party', False):
                                    use battle_character_slot(char_key, char_data)
                        
                        # Нижняя информационная панель
                        frame:
                            style "battle_info_panel"
                            xalign 0.5
                            xsize 580
                            ysize 120
                            
                            if selected_character:
                                use battle_character_info(selected_character)
                            else:
                                text "Выберите персонажа для просмотра информации" xalign 0.5 yalign 0.5 color "#8b5a2b" size 18


# === КОМПОНЕНТ: СЛОТ ПЕРСОНАЖА ===
screen battle_character_slot(char_key, char_data):
    button:
        style "battle_char_slot"
        background "#5c3d2e"
        hover_background "#7a5040"
        xsize 200
        ysize 220
        action SetVariable("selected_character", char_data)
        
        vbox:
            spacing 8
            xalign 0.5
            
            # Портрет персонажа
            frame:
                background "#1a1a1a"
                xsize 140
                ysize 140
                xalign 0.5
                
                # Если есть портрет - показываем, иначе заглушка
                if char_data.get('portrait'):
                    add char_data['portrait'] xalign 0.5 yalign 0.5 fit "contain"
                else:
                    # Цветная заглушка для тестирования
                    if char_key == "saito":
                        add Solid("#1a237e") xsize 130 ysize 130 xalign 0.5 yalign 0.5
                    else:
                        add Solid("#7b1fa2") xsize 130 ysize 130 xalign 0.5 yalign 0.5
            
            # HP бар
            hbox:
                spacing 5
                xalign 0.5
                text "HP" style "battle_bar_label"
                bar:
                    style "battle_hp_bar"
                    value char_data['hp']
                    range char_data['max_hp']
            
            # MP бар
            hbox:
                spacing 5
                xalign 0.5
                text "MP" style "battle_bar_label"
                bar:
                    style "battle_mp_bar"
                    value char_data['mp']
                    range char_data['max_mp']


# === КОМПОНЕНТ: ИНФОРМАЦИЯ О ПЕРСОНАЖЕ ===
screen battle_character_info(char_data):
    hbox:
        spacing 20
        xfill True
        
        # Мини-портрет
        frame:
            background "#5c3d2e"
            xsize 80
            ysize 80
            
            if char_data.get('portrait'):
                add char_data['portrait'] xalign 0.5 yalign 0.5 fit "contain"
            else:
                add Solid("#333333") xsize 70 ysize 70 xalign 0.5 yalign 0.5
        
        # Информация
        vbox:
            spacing 8
            
            text char_data.get('name', 'Неизвестный') style "battle_char_name_text"
            
            hbox:
                spacing 20
                text "HP: [char_data['hp']]/[char_data['max_hp']]" color "#4caf50" size 18
                text "MP: [char_data['mp']]/[char_data['max_mp']]" color "#29b6f6" size 18
            
            # Можно добавить дополнительную информацию
            # text "Уровень: [char_data.get('level', 1)]" color "#5c3d2e" size 16


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
    background Frame("gui/button/quick_idle.png", 5, 5, 5, 5)
    hover_background Frame("gui/button/quick_hover.png", 5, 5, 5, 5)
    # Fallback стили
    # background "#8b5a2b99"
    # hover_background "#a0603099"
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
            textbutton "Назад":
                style "quick_button"
                text_style "quick_button_text"
                action Rollback()
            
            textbutton "История":
                style "quick_button"
                text_style "quick_button_text"
                action ShowMenu('history')
            
            textbutton "Пропуск":
                style "quick_button"
                text_style "quick_button_text"
                action Skip()
                alternate Skip(fast=True, confirm=True)
            
            textbutton "Авто":
                style "quick_button"
                text_style "quick_button_text"
                action Preference("auto-forward", "toggle")
            
            # Разделитель визуальный
            null width 15
            
            # НОВОЕ: Инвентарь
            textbutton "Инвентарь":
                style "quick_button"
                text_style "quick_button_text"
                action ShowMenu('inventory')
            
            # Разделитель
            null width 15
            
            # Системные функции
            textbutton "Сохранить":
                style "quick_button"
                text_style "quick_button_text"
                action ShowMenu('save')
            
            textbutton "Б.Сохр":
                style "quick_button"
                text_style "quick_button_text"
                action QuickSave()
            
            textbutton "Б.Загр":
                style "quick_button"
                text_style "quick_button_text"
                action QuickLoad()
            
            textbutton "Настр.":
                style "quick_button"
                text_style "quick_button_text"
                action ShowMenu('preferences')


# ============================================================================
# ДОПОЛНИТЕЛЬНЫЕ ЭКРАНЫ-ЗАГЛУШКИ
# (Нужно будет реализовать полноценно)
# ============================================================================

# Экран инвентаря (заглушка)
screen inventory():
    tag menu
    modal True
    
    add "#00000088"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 500
        background "#e8d5b8"
        padding (20, 20)
        
        vbox:
            spacing 15
            
            frame:
                background "#8b5a2b"
                xalign 0.5
                padding (30, 10)
                text "Инвентарь" color "#fff8e7" size 28 bold True
            
            text "Здесь будет список предметов..." xalign 0.5 color "#5c3d2e"
            
            textbutton "Закрыть":
                xalign 0.5
                style "battle_menu_button"
                text_style "battle_menu_button_text"
                action Return()


# Экран выбора отряда (заглушка)
screen party_select():
    tag menu
    modal True
    
    add "#00000088"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 550
        background "#e8d5b8"
        padding (20, 20)
        
        vbox:
            spacing 15
            
            frame:
                background "#8b5a2b"
                xalign 0.5
                padding (30, 10)
                text "Выбор отряда" color "#fff8e7" size 28 bold True
            
            text "Здесь можно будет выбрать участников боя..." xalign 0.5 color "#5c3d2e"
            
            textbutton "Закрыть":
                xalign 0.5
                style "battle_menu_button"
                text_style "battle_menu_button_text"
                action Return()


# Экран информации о персонажах (заглушка)
screen characters():
    tag menu
    modal True
    
    add "#00000088"
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 550
        background "#e8d5b8"
        padding (20, 20)
        
        vbox:
            spacing 15
            
            frame:
                background "#8b5a2b"
                xalign 0.5
                padding (30, 10)
                text "Персонажи" color "#fff8e7" size 28 bold True
            
            hbox:
                spacing 20
                xalign 0.5
                
                for char_key, char_data in battle_characters.items():
                    use character_detail_card(char_key, char_data)
            
            textbutton "Закрыть":
                xalign 0.5
                style "battle_menu_button"
                text_style "battle_menu_button_text"
                action Return()


# Карточка персонажа для экрана персонажей
screen character_detail_card(char_key, char_data):
    frame:
        background "#dcbfa6"
        xsize 280
        ysize 350
        padding (15, 15)
        
        vbox:
            spacing 10
            xalign 0.5
            
            # Портрет
            frame:
                background "#5c3d2e"
                xsize 150
                ysize 150
                xalign 0.5
                
                if char_key == "saito":
                    add Solid("#1a237e") xsize 140 ysize 140 xalign 0.5 yalign 0.5
                else:
                    add Solid("#7b1fa2") xsize 140 ysize 140 xalign 0.5 yalign 0.5
            
            text char_data.get('name', 'Неизвестный') xalign 0.5 color "#5c3d2e" size 22 bold True
            
            vbox:
                spacing 5
                text "HP: [char_data['hp']]/[char_data['max_hp']]" color "#4caf50" size 16
                text "MP: [char_data['mp']]/[char_data['max_mp']]" color "#29b6f6" size 16
