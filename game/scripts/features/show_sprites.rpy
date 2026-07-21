
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


# slide
transform slide_left_out_generic:
    yalign 1.0 zoom 0.55 alpha 1.0
    ease 0.4 xalign -0.3 alpha 0

transform slide_right_out_generic:
    yalign 1.0 zoom 0.55 alpha 1.0
    ease 0.4 xalign 1.3 alpha 0

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

# =============================================================================
#  ВАЖНО: персонаж определяется по ТЕГУ (первое слово имени образа).
#    "d 1 happy" -> тег "d"   |   "s 1 sad" -> тег "s"
#  Поэтому смена эмоции того же персонажа ("s 1 sad" -> "s 1") НЕ вызывает
#  слайд: меняется только картинка на месте (как обычный show с dissolve).
# =============================================================================

# =============================================================================
#  ГЕОМЕТРИЯ ПОЗИЦИЙ  (zoom, xalign, yalign)
#  Меняешь координаты здесь — меняются и точки покоя, и слайды.
# =============================================================================
init -1 python:

    CHARA_GEOM = {
        #  mode      side       zoom  xalign  yalign
        ("normal", "left"):   (0.55, -0.20, 1.00),
        ("normal", "center"): (0.55,  0.50, 1.00),
        ("normal", "right"):  (0.55,  1.20, 1.00),

        ("big",    "left"):   (0.70, -0.30, 1.00),
        ("big",    "center"): (0.70,  0.50, 0.15),
        ("big",    "right"):  (0.70,  1.40, 0.95),
    }

    def _geom(mode, side):
        return CHARA_GEOM.get((mode, side), CHARA_GEOM[("normal", "center")])

    # точка ЗА экраном для слайда
    def _off(side, direction):
        if side == "left":
            return -0.60
        if side == "right":
            return 1.70
        # центр: заезжает слева, уезжает вправо (как slide_*_to_center)
        return 1.70 if direction == "out" else -0.60

    # маркер «аргумент не задан» — чтобы отличить anim_out=None (мгновенно)
    # от anim_out не переданного вовсе (тогда берём значение anim_in).
    _ANIM_UNSET = object()

    # стартовая точка ЗА экраном для ВЪЕЗДА нового персонажа с учётом
    # заданного направления слайда:
    #   "right" (slide_right: персонаж движется ВПРАВО) -> старт слева  (-0.60)
    #   "left"  (slide_left:  персонаж движется ВЛЕВО)  -> старт справа ( 1.70)
    #   "nearest"/None -> прежнее поведение: из ближайшей к слоту стороны
    def _entry_x(slot, slide_dir):
        if slide_dir == "right":
            return -0.60
        if slide_dir == "left":
            return 1.70
        return _off(slot, "in")

    # конечная точка ЗА экраном для ВЫЕЗДА уходящего персонажа с учётом
    # заданного направления слайда:
    #   "left"  (slide_left:  персонаж уезжает ВЛЕВО)  -> уходит влево  (-0.60)
    #   "right" (slide_right: персонаж уезжает ВПРАВО) -> уходит вправо ( 1.70)
    #   "nearest"/None -> прежнее поведение: в ближайшую к слоту сторону
    def _exit_x(slot, slide_dir):
        if slide_dir == "left":
            return -0.60
        if slide_dir == "right":
            return 1.70
        return _off(slot, "out")

    # -------------------------------------------------------------------------
    #  ДИНАМИЧЕСКАЯ ДЛИТЕЛЬНОСТЬ СЛАЙДА (на «физике»)
    #  Идея: чем длиннее путь по горизонтали (в единицах xalign), тем дольше
    #  слайд. Короткие перемещения (центр -> бок, вход сбоку в свой слот)
    #  остаются быстрыми (~базовая длительность), а длинные (левый край ->
    #  правый край, вход/выход через весь экран) занимают больше времени.
    #
    #  Настраивается ОДНИМ коэффициентом SLIDE_SPEED в самом файле (см. ниже,
    #  рядом с _SLIDE_DUR). В аргументы show_sprites ничего заносить не нужно.
    #  Зависимость sqrt(dist) даёт «физичный» разгон/торможение: время растёт
    #  медленнее, чем расстояние, поэтому дальние переходы не кажутся вялыми.
    #
    #  x0, x1 — стартовый и конечный xalign перемещения.
    def _slide_dur(x0, x1):
        import math
        # выключено -> постоянная длительность (с учётом коэффициента скорости)
        if not SLIDE_DYNAMIC:
            return _SLIDE_DUR / max(SLIDE_SPEED, 0.01)
        dist = abs(float(x1) - float(x0))
        ref  = max(_SLIDE_REF_DIST, 0.001)
        dur  = _SLIDE_DUR * math.sqrt(max(dist, 0.0) / ref)
        dur  = dur / max(SLIDE_SPEED, 0.01)   # >1 быстрее, <1 медленнее
        return max(_SLIDE_DUR_MIN, min(_SLIDE_DUR_MAX, dur))

    # порядок наложения. центральный (например derflinger) может быть
    # на переднем плане (center_front=True) или под боковыми (False).
    def _zorder(side, center_front):
        if side == "center":
            if center_front is True:
                return 50
            if center_front is False:
                return 5
            return 15
        return 20

    def _tag_of(image_name):
        # тег = первое слово имени образа ("d 1 happy" -> "d")
        return image_name.split()[0]

    def _all_hide_tags():
        tags = list(CHARA_TAGS)
        for _s, _rec in store._sprite_slots.items():
            _t = _rec[0]
            if _t not in tags:
                tags.append(_t)
        return tags    

# =============================================================================
#  СОСТОЯНИЕ: slot ("left"/"center"/"right") -> (tag, image, mode, z)
#  z — текущий zorder спрайта. Растёт от _sprite_z: кто показан/изменён
#  последним, тот выше всех (новый элемент перекрывает остальных).
# =============================================================================
default _sprite_slots = {}
default _sprite_z = 0

# Все теги персонажей — чтобы снести всех одной командой.
define CHARA_TAGS = [
    "l", "s", "k", "t", "c", "h", "si", "ha", "g", "d", "o", "m",
    "npc_left", "npc_right", "mage",
]

# --- НАСТРОЙКА СКОРОСТИ СЛАЙДА (правь тут, в аргументы функции не выносится) ---
define _SLIDE_DUR      = 0.4    # базовая длительность короткого слайда (сек)
define SLIDE_DYNAMIC   = True   # True: длительность зависит от пути; False: всегда _SLIDE_DUR
define SLIDE_SPEED     = 1.3    # общий коэффициент: >1 быстрее, <1 медленнее
define _SLIDE_REF_DIST = 0.5    # опорный путь (в xalign), дающий базовую длительность
define _SLIDE_DUR_MIN  = 0.3    # нижняя граница длительности (сек)
define _SLIDE_DUR_MAX  = 0.9    # верхняя граница длительности (сек)

# =============================================================================
#  ПАРАМЕТРИЧЕСКИЕ ТРАНСФОРМЫ
#  dur — длительность движения (вычисляется _slide_dur по длине пути).
# =============================================================================

# точка покоя (для появления/обновления без движения)
transform chara_at(z, xa, ya):
    zoom z
    xalign xa
    yalign ya
    alpha 1.0

# плавный въезд из-за экрана в точку покоя
transform chara_slide_in(z, xa, ya, sx, dur=0.4):
    zoom z
    yalign ya
    xalign sx
    alpha 0.0
    easein dur xalign xa alpha 1.0

# плавный выезд из точки покоя за экран
transform chara_slide_out(z, xa, ya, ex, dur=0.4):
    zoom z
    yalign ya
    xalign xa
    alpha 1.0
    easeout dur xalign ex alpha 0.0

# плавное ПЕРЕМЕЩЕНИЕ из старой точки покоя в новую (например center -> left),
# когда тот же персонаж остаётся на экране, но меняет позицию/размер.
transform chara_move(z0, xa0, ya0, z1, xa1, ya1, dur=0.4):
    zoom z0
    xalign xa0
    yalign ya0
    alpha 1.0
    ease dur zoom z1 xalign xa1 yalign ya1

# =============================================================================
#  СКРЫТЬ ВСЕХ ПЕРСОНАЖЕЙ ОДНОЙ КОМАНДОЙ
#     $ clear_chars()           — с dissolve
#     $ clear_chars(anim=None)  — мгновенно
# =============================================================================
init -1 python:

    def _hide_all(anim="dissolve"):
        slots = store._sprite_slots

        # уже пусто
        if not slots:
            store._sprite_slots = {}
            store._sprite_z = 0
            if anim == "dissolve":
                renpy.with_statement(dissolve)
            return

        # скип / откат / прокрутка колесом — мгновенно
        if renpy.is_skipping() or renpy.in_rollback():
            for tag in _all_hide_tags():
                renpy.hide(tag)
            store._sprite_slots = {}
            store._sprite_z = 0
            renpy.with_statement(None)
            return

        # --- без слайда: None (мгновенно) или dissolve ---
        if anim is None or anim == "dissolve":
            for tag in _all_hide_tags():
                renpy.hide(tag)
            store._sprite_slots = {}
            store._sprite_z = 0
            renpy.with_statement(dissolve if anim == "dissolve" else None)
            return

        # --- слайд: выбираем направление для каждого слота ---
        if anim == "slide_left":
            dir_of = lambda s: "left"
        elif anim == "slide_right":
            dir_of = lambda s: "right"
        elif anim == "slide":
            # каждый в свою сторону
            dir_of = lambda s: "left" if s == "left" else "right"
        else:
            # неизвестное значение -> мгновенно (безопасный фолбэк)
            for tag in _all_hide_tags():
                renpy.hide(tag)
            store._sprite_slots = {}
            store._sprite_z = 0
            renpy.with_statement(None)
            return

        # запускаем выезд из ТЕКУЩЕЙ позиции.
        # ВАЖНО: берём геометрию по РЕАЛЬНОМУ режиму спрайта (mode хранится в
        # слоте), а не по хардкод-трансформам slide_*_out_generic с zoom 0.55.
        # Иначе big-спрайт (zoom 0.70) в самом начале анимации «прыгал» в
        # normal-размер. chara_slide_out сохраняет zoom/yalign во время выезда.
        _max_dur = _SLIDE_DUR_MIN
        for s, (tag, img, m, z) in slots.items():
            zoom_, xa, ya = _geom(m, s)
            ex = _exit_x(s, dir_of(s))
            d = _slide_dur(xa, ex)               # путь: точка покоя -> за экран
            _max_dur = max(_max_dur, d)
            renpy.show(img, at_list=[chara_slide_out(zoom_, xa, ya, ex, d)],
                       tag=tag, zorder=z)
        renpy.with_statement(None)
        renpy.pause(_max_dur)                     # ждём самый долгий слайд

        # снести и сбросить состояние
        for tag in _all_hide_tags():
            renpy.hide(tag)
        store._sprite_slots = {}
        store._sprite_z = 0
        renpy.with_statement(None)


# =============================================================================
#  ДИНАМИЧЕСКИЙ ПОКАЗ 1-3 ПЕРСОНАЖЕЙ
# -----------------------------------------------------------------------------
#  show_sprites(chars, mode="normal", anim="dissolve", side=None, center_front=None)
#
#    chars  — строка (1 персонаж) или список/кортеж из 1..3 имён образов:
#               1 -> позиция из side (по умолчанию "center")
#               2 -> [левый, правый]
#               3 -> [левый, центр, правый]
#    mode     — "normal" / "big"
#    anim_in  — анимация ПОЯВЛЯЮЩИХСЯ / ЗАМЕНЯЕМЫХ персонажей
#               "dissolve" / "slide" / "slide_left" / "slide_right" / None
#               (None = мгновенно), либо кортеж/список направлений по
#               персонажам (в порядке chars).
#    anim_out — анимация УХОДЯЩИХ персонажей (тех, кого заменяют/убирают).
#               Те же значения. Если не задан — повторяет anim_in.
#    anim     — устаревший алиас anim_in (оставлен для совместимости).
#  5 вариантов анимации скрытия (аргумент anim_out при chars=None,
#  либо anim/anim_in как алиас):
#      None           — мгновенно, без анимации
#      "dissolve"     — плавное растворение
#      "slide_right"  — ОБА (все) спрайта уезжают вправо
#      "slide_left"   — ОБА (все) спрайта уезжают влево
#      "slide"        — каждый в свою сторону: левый слот -> влево,
#                       правый слот -> вправо (центр -> вправо)
#
#  НАПРАВЛЕНИЕ ВЪЕЗДА НОВЫХ / ЗАМЕНЯЕМЫХ ПЕРСОНАЖЕЙ (anim при показе):
#      "slide"        — по умолчанию: каждый заезжает из ближайшей стороны
#                       (левый слот -> слева, правый -> справа);
#      "slide_right"  — ВСЕ новые заезжают СЛЕВА и едут вправо на своё место;
#      "slide_left"   — ВСЕ новые заезжают СПРАВА и едут влево на своё место;
#      кортеж/список  — направление отдельно для каждого персонажа, в том же
#                       порядке, что и chars. Напр. для 2 персонажей:
#                         anim=("slide_left", "slide_right")
#                       левый заедет справа-влево, правый — слева-вправо.
#                       Элементы: "slide"/"slide_left"/"slide_right".
#    side   — только для одного персонажа: "left"/"center"/"right"
#    center_front — порядок наложения для ЦЕНТРАЛЬНОГО при ПЕРВОМ показе:
#                   True  — центр сразу поверх боковых,
#                   False — центр сразу под боковыми,
#                   None  — обычный порядок.
#    raise_z=False — изменённый спрайт СОХРАНЯЕТ свой прежний zorder слота, поэтому смена эмоции/размера не «выдёргивает» его вперёд.
#
#  ZORDER (наложение спрайтов):
#   • любой ПОКАЗАННЫЙ/ИЗМЕНЁННЫЙ в этом вызове спрайт получает новый, самый
#     высокий zorder -> «новый элемент перекрывает всех остальных»;
#   • неизменившиеся спрайты сохраняют свой прежний zorder и относительный
#     порядо�� (если d перекрывал s и оба не менялись — d так и перекрывает s).
#
#  ЛОГИКА (сравнение со старым раскладом по ТЕГУ персонажа):
#   • тот же персонаж в том же слоте, сменился РАЗМЕР (normal<->big)
#                                     -> плавный scale (chara_move), в ОБЕ стороны;
#   • тот же персонаж в том же слоте, сменилась ТОЛЬКО эмоция -> dissolve на месте;
#   • тот же персонаж в другом слоте  -> плавно переезжает (chara_move);
#   • персонаж пропал/сменился        -> старый уезжает (slide) или гаснет,
#                                         pause(0.2), затем заезжает новый;
#   • неизменившийся слот             -> остаётся как есть.
# =============================================================================
init -1 python:

    # разбор направления въезда для новых/заменяемых персонажей.
    #   anim может быть строкой ("slide"/"slide_left"/"slide_right"/"dissolve"/None)
    #   ИЛИ кортежем/списком той же длины, что chars — тогда направление задаётся
    #   отдельно для каждого персонажа (в порядке слотов slots_order).
    # Возвращает (anim_family, dir_by_slot):
    #   anim_family — общий режим анимации для _apply_layout ("slide"/"dissolve"/None),
    #   dir_by_slot — slot -> "left"/"right"/"nearest" для въезда новых спрайтов.
    def _parse_show_anim(anim, slots_order):
        dir_by_slot = {}

        # кортеж/список -> н��правление на каждого персонажа
        if isinstance(anim, (tuple, list)):
            for i, a in enumerate(anim):
                if i >= len(slots_order):
                    break
                s = slots_order[i]
                if a == "slide_left":
                    dir_by_slot[s] = "left"
                elif a == "slide_right":
                    dir_by_slot[s] = "right"
                else:
                    dir_by_slot[s] = "nearest"   # "slide"/прочее -> ближайшая сторона
            # слоты, не указанные в кортеже -> ближайшая сторона
            for s in slots_order:
                dir_by_slot.setdefault(s, "nearest")
            return "slide", dir_by_slot

        # строка
        if anim == "slide_left":
            for s in slots_order:
                dir_by_slot[s] = "left"
            return "slide", dir_by_slot
        if anim == "slide_right":
            for s in slots_order:
                dir_by_slot[s] = "right"
            return "slide", dir_by_slot
        if anim == "slide":
            for s in slots_order:
                dir_by_slot[s] = "nearest"
            return "slide", dir_by_slot
        if anim is None:
            return None, dir_by_slot
        # "dissolve" и всё неизвестное -> dissolve
        return "dissolve", dir_by_slot

    def show_sprites(chars, mode="normal", anim_in="slide", anim_out=_ANIM_UNSET, side=None, center_front=None, hide_window=False, raise_z=True, anim=_ANIM_UNSET):
        # anim — устаревший алиас anim_in.
        if anim is not _ANIM_UNSET:
            anim_in = anim
        # anim_out не задан -> повторяет anim_in (как было с единым anim).
        if anim_out is _ANIM_UNSET:
            anim_out = anim_in

        if chars is None:
            _hide_all(anim_out)
            return

        if isinstance(chars, str):
            chars = [chars]
        chars = list(chars)
        n = len(chars)

        # порядок слотов совпадает с порядком chars — чтобы кортеж anim
        # сопоставлялся с персонажами один-к-одному.
        if n == 1:
            slots_order = [side or "center"]
        elif n == 2:
            slots_order = ["left", "right"]
        elif n == 3:
            slots_order = ["left", "center", "right"]
        else:
            raise Exception("show_sprites: поддерживается от 1 до 3 персонажей")

        layout = {slots_order[i]: chars[i] for i in range(n)}

        # anim_in -> направление ВЪЕЗДА новых (по порядку chars).
        anim_family_in, dir_in = _parse_show_anim(anim_in, slots_order)
        # anim_out -> направление ВЫЕЗДА уходящих. Кортеж сопоставляем с
        # каноническим порядком слотов, т.к. уходящих нет в chars.
        anim_family_out, dir_out = _parse_show_anim(anim_out, ["left", "center", "right"])

        _apply_layout(layout, mode, anim_family_in, anim_family_out,
                      center_front, hide_window, raise_z, dir_in, dir_out)


    def _apply_layout(layout, mode, anim_in, anim_out, center_front, hide_window=False, raise_z=True, dir_in=None, dir_out=None):
        slots  = store._sprite_slots         # slot -> (tag, img, mode, z)
        # dir_in  — slot -> "left"/"right"/"nearest": направление ВЪЕЗДА новых.
        # dir_out — slot -> "left"/"right"/"nearest": направление ВЫЕЗДА уходящих.
        # Пусто -> ближайшая сторона (прежнее поведение).
        if dir_in is None:
            dir_in = {}
        if dir_out is None:
            dir_out = {}

        # Мгновенный режим: скип/перемотка (Ctrl), А ТАКЖЕ откат/прокрутка
        # колесом мыши (rollback / roll-forward). В этих состояниях реальное
        # время НЕ идёт: renpy.pause() возвращается сразу, а alpha-слайды
        # «застревают» прозрачными. is_skipping() ловит только скип, поэтому
        # колесо мыши (rollback) раньше оставляло спрайты невидимыми.
        _instant = renpy.is_skipping() or renpy.in_rollback()

        # флаги отдельно для приходящих (in) и уходящих (out)
        slide_in   = (anim_in == "slide")
        noanim_in  = (anim_in is None)
        slide_out  = (anim_out == "slide")
        noanim_out = (anim_out is None)

        # Текстбокс
        if hide_window:
            _window_hide(None)
        else:
            _window_show(None)

        # базовый тег = первое слово имени образа ("npc 1 angry" -> "npc")
        base_tags = {s: _tag_of(img) for s, img in layout.items()}
        tag_counts = {}
        for _bt in base_tags.values():
            tag_counts[_bt] = tag_counts.get(_bt, 0) + 1

        new = {}
        for s, img in layout.items():
            bt = base_tags[s]
            # коллизия (один персонаж/образ в неск. слотов) -> уникализируем по слоту
            tag = bt if tag_counts[bt] == 1 else (bt + "__" + s)
            new[s] = (tag, img)
        # ... дальше без изменений:
        # old_by_tag = {...}; new_by_tag = {...}; и т.д.
        #
        # Замечание: диффинг по-прежнему идёт по тегам. Так как дубли уникальны
        # по слоту, повторный show того же расклада (тот же слот) корректно
        # определяется как "без изменений"/"смена эмоции", а исчезновение одного
        # из дублей — как leaver (гасится по сохранённому тегу).    

        # индексируем по ТЕГУ персонажа
        old_by_tag = {tag: (s, oimg, om, oz)
                      for s, (tag, oimg, om, oz) in slots.items()}
        new_by_tag = {tag: (s, nimg) for s, (tag, nimg) in new.items()}

        # ---- БЫСТРЫЙ ПУТЬ: МГНОВЕННЫЙ ПОКАЗ (скип / откат / прокрутка) ----
        # Никаких pause и alpha-анимаций — сразу ставим всех актуальных
        # персонажей в точку покоя с полной непрозрачностью, гасим лишних.
        # Это убирает «прозрачные/невидимые» спрайты при быстром ЛКМ и колесе.
        if _instant:
            new_tags = set(new_by_tag.keys())
            for tag, (os_, oimg, om, oz) in old_by_tag.items():
                if tag not in new_tags:
                    renpy.hide(tag)

            def _order_key_fast(item):
                s = item[0]
                if s != "center":
                    return 1
                if center_front is True:
                    return 2
                if center_front is False:
                    return 0
                return 1

            old_z_by_slot_fast = {s: oz for s, (tag, oimg, om, oz) in slots.items()}
            slot_z = {}
            for s, (tag, nimg) in sorted(new.items(), key=_order_key_fast):
                if not raise_z and s in old_z_by_slot_fast:
                    slot_z[s] = old_z_by_slot_fast[s]      # сохраняем слой слота
                else:
                    store._sprite_z += 1
                    slot_z[s] = store._sprite_z
                z, xa, ya = _geom(mode, s)
                renpy.show(nimg, at_list=[chara_at(z, xa, ya)],
                           tag=tag, zorder=slot_z[s])
            renpy.with_statement(None)

            new_state = {}
            for s, (tag, nimg) in new.items():
                new_state[s] = (tag, nimg, mode, slot_z[s])
            store._sprite_slots = new_state
            return

        # набор ФАКТИЧЕСКИ назначенных новых тегов в этом вызове —
        # чтобы случайно не погасить только что показанный спрайт
        new_tags_set = set(t for (t, _img) in new.values())

        # --- группировка по БАЗОВОМУ тегу (устойчиво к прежней уникализации) ---
        old_groups = {}
        for _s, (_otag, _oimg, _om, _oz) in slots.items():
            _b = _tag_of(_oimg)
            old_groups.setdefault(_b, []).append((_s, _otag, _oimg, _om, _oz))

        new_groups = {}
        for _s, (_ntag, _nimg) in new.items():
            _b = _tag_of(_nimg)
            new_groups.setdefault(_b, []).append((_s, _ntag, _nimg))

        leavers  = []   # (slot, tag, img, mode)                          -> уходит совсем
        movers   = []   # (old_slot, new_slot, old_tag, new_tag, img, old_mode)
        resizes  = []   # (slot, old_tag, new_tag, img, old_mode)         -> тот же слот, сменился размер
        emotions = []   # (slot, old_tag, new_tag, img)                   -> тот же слот, сменилась эмоция
        entrants = []   # (slot, tag, img)                                -> новый

        for _b in (set(old_groups) | set(new_groups)):
            olds = old_groups.get(_b, [])
            news = new_groups.get(_b, [])
            used_old = set()
            used_new = set()

            # 1) сперва сшиваем совпадающие СЛОТЫ (персонаж остался на месте)
            for ni, (ns_, ntag, nimg) in enumerate(news):
                for oi, (os_, otag, oimg, om, oz) in enumerate(olds):
                    if oi in used_old:
                        continue
                    if os_ == ns_:
                        used_old.add(oi)
                        used_new.add(ni)
                        if om != mode:
                            resizes.append((ns_, otag, ntag, nimg, om))
                        elif oimg != nimg:
                            emotions.append((ns_, otag, ntag, nimg))
                        # иначе слот не изменился -> сохранит прежний zorder
                        break

            rem_old = [olds[i] for i in range(len(olds)) if i not in used_old]
            rem_new = [news[i] for i in range(len(news)) if i not in used_new]

            # 2) оставшихся старых ПЕРЕИСПОЛЬЗУЕМ как movers к оставшимся слотам
            #    (это и есть фикс: центр -> бок вместо «исчез + появился»)
            k = min(len(rem_old), len(rem_new))
            for i in range(k):
                os_, otag, oimg, om, oz = rem_old[i]
                ns_, ntag, nimg = rem_new[i]
                movers.append((os_, ns_, otag, ntag, nimg, om))

            # 3) реальный излишек: старые -> уходят, новые -> появляются
            for i in range(k, len(rem_old)):
                os_, otag, oimg, om, oz = rem_old[i]
                leavers.append((os_, otag, oimg, om))
            for i in range(k, len(rem_new)):
                ns_, ntag, nimg = rem_new[i]
                entrants.append((ns_, ntag, nimg))

        # ---- НАЗНАЧИТЬ ZORDER показанным/изменённым слотам ----
        shown_slots = [m[1] for m in movers] + [r[0] for r in resizes] \
                      + [e[0] for e in emotions] + [e[0] for e in entrants]

        def _order_key(s):
            if s != "center":
                return 1
            if center_front is True:
                return 2
            if center_front is False:
                return 0
            return 1

        old_z_by_slot = {s: oz for s, (tag, oimg, om, oz) in slots.items()}

        slot_z = {}
        for s in sorted(shown_slots, key=_order_key):
            if not raise_z and s in old_z_by_slot:
                slot_z[s] = old_z_by_slot[s]               # НЕ поднимаем слой
            else:
                store._sprite_z += 1
                slot_z[s] = store._sprite_z

        # ---- 1) УХОДЯЩИЕ ---- (анимация по anim_out)
        if leavers:
            if slide_out:
                _max_dur = _SLIDE_DUR_MIN
                for s, tag, oimg, om in leavers:
                    z, xa, ya = _geom(om, s)   # om — старый режим слота (big/normal)
                    ex = _exit_x(s, dir_out.get(s))
                    d = _slide_dur(xa, ex)     # путь: точка покоя -> за экран
                    _max_dur = max(_max_dur, d)
                    renpy.show(oimg, at_list=[chara_slide_out(z, xa, ya, ex, d)],
                               tag=tag, zorder=old_z_by_slot.get(s, 20))
                renpy.with_statement(None)
                renpy.pause(_max_dur)
                for s, tag, oimg, om in leavers:
                    renpy.hide(tag)
                renpy.with_statement(None)
            else:
                for s, tag, oimg, om in leavers:
                    renpy.hide(tag)
                renpy.with_statement(None if noanim_out else dissolve)

        # ---- 2) ПЕРЕЕЗЖАЮЩИЕ (другой слот) ---- (остаются на экране -> anim_in)
        if movers:
            for os_, ns_, otag, ntag, nimg, om in movers:
                z1, xa1, ya1 = _geom(mode, ns_)
                if noanim_in:
                    renpy.show(nimg, at_list=[chara_at(z1, xa1, ya1)],
                               tag=ntag, zorder=slot_z[ns_])
                else:
                    z0, xa0, ya0 = _geom(om, os_)
                    d = _slide_dur(xa0, xa1)   # путь: старый слот -> новый слот
                    renpy.show(nimg, at_list=[chara_move(z0, xa0, ya0, z1, xa1, ya1, d)],
                               tag=ntag, zorder=slot_z[ns_])
                # тег сменился (дубликаты образа) -> гасим старый, чтобы не завис
                if otag != ntag and otag not in new_tags_set:
                    renpy.hide(otag)
            renpy.with_statement(None)

        # ---- 3a) СМЕНА РАЗМЕРА (normal<->big) -> ПЛАВНЫЙ SCALE, без dissolve ----
        if resizes:
            for s, otag, ntag, nimg, om in resizes:
                z1, xa1, ya1 = _geom(mode, s)
                if noanim_in:
                    renpy.show(nimg, at_list=[chara_at(z1, xa1, ya1)],
                               tag=ntag, zorder=slot_z[s])
                else:
                    z0, xa0, ya0 = _geom(om, s)            # старая геометрия того же слота
                    # смена размера — это scale на месте (xalign почти не меняется),
                    # держим базовую длительность с учётом коэффициента скорости.
                    d = _SLIDE_DUR / max(SLIDE_SPEED, 0.01)
                    renpy.show(nimg, at_list=[chara_move(z0, xa0, ya0, z1, xa1, ya1, d)],
                               tag=ntag, zorder=slot_z[s])
                if otag != ntag and otag not in new_tags_set:
                    renpy.hide(otag)
            renpy.with_statement(None)                      # без dissolve и без alpha

        # ---- 3b) СМЕНА ЭМОЦИИ (картинка изменилась, размер тот же) -> dissolve ----
        if emotions:
            for s, otag, ntag, nimg in emotions:
                z, xa, ya = _geom(mode, s)
                renpy.show(nimg, at_list=[chara_at(z, xa, ya)],
                           tag=ntag, zorder=slot_z[s])
                if otag != ntag and otag not in new_tags_set:
                    renpy.hide(otag)
            renpy.with_statement(None if noanim_in else dissolve)

        # задержка перед появлением новых
        if (leavers or movers) and entrants and not noanim_in:
            renpy.pause(0.2)

        # ---- 4) НОВЫЕ ПЕРСОНАЖИ ---- (анимация по anim_in)
        if entrants:
            if slide_in:
                _max_dur = _SLIDE_DUR_MIN
                for s, tag, nimg in entrants:
                    z, xa, ya = _geom(mode, s)
                    # старт въезда с учётом заданного направления (slide_left /
                    # slide_right / кортеж), по умолчанию — из ближайшей стороны.
                    sx = _entry_x(s, dir_in.get(s))
                    d = _slide_dur(sx, xa)     # путь: за экраном -> точка покоя
                    _max_dur = max(_max_dur, d)
                    renpy.show(nimg, at_list=[chara_slide_in(z, xa, ya, sx, d)],
                               tag=tag, zorder=slot_z[s])
                renpy.with_statement(None)
                renpy.pause(_max_dur)
                for s, tag, nimg in entrants:
                    z, xa, ya = _geom(mode, s)
                    renpy.show(nimg, at_list=[chara_at(z, xa, ya)],
                               tag=tag, zorder=slot_z[s])
                renpy.with_statement(None)
            else:
                for s, tag, nimg in entrants:
                    z, xa, ya = _geom(mode, s)
                    renpy.show(nimg, at_list=[chara_at(z, xa, ya)],
                               tag=tag, zorder=slot_z[s])
                renpy.with_statement(None if noanim_in else dissolve)

        # ---- ПЕРЕСТРОИТЬ СОСТОЯНИЕ СЛОТОВ ----
        new_state = {}
        for s, (tag, nimg) in new.items():
            z = slot_z.get(s, old_z_by_slot.get(s, 0))
            new_state[s] = (tag, nimg, mode, z)
        store._sprite_slots = new_state
