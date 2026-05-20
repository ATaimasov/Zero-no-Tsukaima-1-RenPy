# 1. Объявление изображений (пути к вашим файлам)
image gui_sympathy_bar = "gui/sympathy/bar.png"
image gui_sympathy_arrow = "gui/sympathy/arrow.png"
image gui_sympathy_up = "gui/sympathy/up.png"
image gui_sympathy_down = "gui/sympathy/down.png"

# 2. Переменная симпатии
default louise_sympathy = 50

# 3. ATL-трансформации (анимации) вынесены на верхний уровень
transform sympathy_bar_anim:
    xalign 0.05
    yalign 0.04
    zoom 0.6
    alpha 0.0
    linear 0.2 alpha 1.0
    pause 1.5
    linear 0.3 alpha 0.0

transform sympathy_arrow_anim(target_x):
    xalign 0.05
    yalign 0.08
    zoom 0.6
    alpha 0.0
    linear 0.2 alpha 1.0
    linear 0.8 xalign target_x
    pause 0.9
    linear 0.3 alpha 0.0

transform sympathy_text_anim:
    xalign 0.98
    yalign 0.03
    zoom 0.6
    alpha 0.0
    pause 0.4
    linear 0.3 alpha 1.0
    pause 0.8
    linear 0.3 alpha 0.0

# 4. Экран интерфейса
screen sympathy_ui(change_value, max_value=100):
    zorder 100
    
    fixed:
        xalign 0.5
        yalign 0.5

        # Расчёт целевой позиции стрелки
        $ target_x = 0.5 + (change_value / (max_value * 2.5))
        $ target_x = max(0.18, min(0.82, target_x))

        # Применение анимаций через ключевое слово at
        add "gui_sympathy_bar" at sympathy_bar_anim
        add "gui_sympathy_arrow" at sympathy_arrow_anim(target_x)

        if change_value > 0:
            add "gui_sympathy_up" at sympathy_text_anim
        elif change_value < 0:
            add "gui_sympathy_down" at sympathy_text_anim

# 5. Python-функция вызова
init python:
    def update_sympathy(value, var_name="louise_sympathy", max_val=100):
        store = renpy.store
        current = getattr(store, var_name, 50)
        
        new_val = current + value
        new_val = max(0, min(max_val, new_val))
        
        setattr(store, var_name, new_val)
        
        renpy.show_screen("sympathy_ui", change_value=value, max_value=max_val)
        
        # Ждём завершения анимации (2.5 сек). 
        # soft=True позволяет голосовым репликам проигрываться параллельно
        renpy.pause(2.5, hard=False)
        
        renpy.hide_screen("sympathy_ui")
        return new_val