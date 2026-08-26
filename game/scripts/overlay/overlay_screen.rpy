#show overlay img with text

# styles presets
default overlay_styles = {
    'black': {
        'title': { 'size': 78, 'color': "#000000", 'outlines': [(2, "#000000", 0, 0), (1, "#000000", 2, 2)] },
        'subtitle': { 'size': 50, 'color': "#000000", 'outlines': [(1, "#000000", 0, 0)] },
        'line': { 'color': "#000000", 'outline_color': "#000000", 'thickness': 6, 'width': 1000 }
    },
    'white': {
        'title': { 'size': 55, 'color': "#ffffff", 'outlines': [(2, "#ffffff", 0, 0), (1, "#ffffff", 2, 2)] },
        'subtitle': { 'size': 55, 'color': "#ffffff", 'outlines': [(1, "#ffffff", 0, 0)] },
        'line': { 'color': "#ffffff", 'outline_color': "#ffffff", 'thickness': 6, 'width': 1000 }
    },
    'beige': {
        'title': { 'size': 78, 'color': "#000000", 'outlines': [(2, "#d9dac6", 0, 0), (1, "#d9dac6", 2, 2)] },
        'subtitle': { 'size': 50, 'color': "#000000", 'outlines': [(1, "#d9dac6", 0, 0)] },
        'line': { 'color': "#000000", 'outline_color': "#d9dac6", 'thickness': 6, 'width': 1000 }
    },
    'orange': {
        'title': { 'size': 78, 'color': "#fe9e5e", 'outlines': [(2, "#875109", 0, 0), (1, "#875109", 2, 2)] },
        'subtitle': { 'size': 50, 'color': "#fe9e5e", 'outlines': [(1, "#875109", 0, 0)] },
        'line': { 'color': "#fd9754", 'outline_color': "#875109", 'thickness': 6, 'width': 1000 }
    },
}


# overlay screen
screen chapter_title_overlay(title_text, show_subtitle=False, style_dict={}):
    zorder 100
    vbox:
        align (0.5, 0.5)  # Центрируем по X и сдвигаем на 40% по Y
        xfill False        # Запрещаем растягивать vbox на всю ширину экрана
        spacing 20         # Отступы между заголовком, линией и подзаголовком

        # Заголовок
        text title_text:
            xalign 0.5
            text_align 0.5
            antialias True
            size style_dict['title']['size']
            color style_dict['title']['color']
            outlines style_dict['title']['outlines']

        # Линия и подзаголовок
        if show_subtitle:
            $ line_width = style_dict['line']['width']
            $ line_thickness = style_dict['line']['thickness']
            $ glow_color = style_dict['line']['outline_color']

            # Контейнер для линии. Убран yalign 0.5, добавлены фиксированные размеры
            fixed:
                xalign 0.5
                xsize line_width + 14
                ysize line_thickness + 14
                
                # Основная линия
                add Solid(style_dict['line']['color']) xysize (line_width, line_thickness) xalign 0.5 yalign 0.5

            # Подзаголовок
            text "The Familiar of Zero":
                xalign 0.5
                text_align 0.5
                antialias True
                size style_dict['subtitle']['size']
                color style_dict['subtitle']['color']
                outlines style_dict['subtitle']['outlines']


# overlay func
label overlay_screen(scene_name=None, title_text="", show_subtitle=False, text_mode='beige', delay=2.0, isUseBlur=True, sound_path=None):
    # get Style from presets
    $ current_style = overlay_styles.get(text_mode, overlay_styles['beige'])

    # clear old
    hide screen chapter_title_overlay
    pause 0.05

    # show bg
    if scene_name is None:
        scene black with dissolve
        $ show_subtitle = False ## no need
    elif isUseBlur is True:
        scene expression "bg " + scene_name + "_blurred" at fullscreen with dissolve
    else:
        scene expression "bg " + scene_name at fullscreen with dissolve
    pause 0.2

    # show title
    show screen chapter_title_overlay(
        title_text=title_text,
        show_subtitle=show_subtitle,
        style_dict=current_style
    )
    with dissolve

    if sound_path is not None:
        voice sound_path
    
    # pause
    $ renpy.pause(delay, hard=True)

    # hide title
    hide screen chapter_title_overlay
    with dissolve
    pause 0.2

    # return original scene
    if scene_name is not None and isUseBlur is True:
        scene expression "bg " + scene_name at fullscreen with dissolve
        pause 0.2
    return