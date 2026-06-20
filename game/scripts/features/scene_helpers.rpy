# =============================================================================
#  scene_helpers.rpy
#  Готовые методы: затухание сцены, скрытие/возврат интерфейса,
#  умный показ 1-3 персонажей, flash со сбросом спрайтов.
#  Просто положи файл в game/ — переписывать существующий код не нужно.
#
#  ВАЖНО: персонаж определяется по ТЕГУ (первое слово имени образа).
#    "d 1 happy" -> тег "d"   |   "s 1 sad" -> тег "s"
#  Поэтому смена эмоции того же персонажа ("s 1 sad" -> "s 1") НЕ вызывает
#  слайд: меняется только картинка на месте (как обычный show с dissolve).
# =============================================================================


# =============================================================================
#  ГЕОМЕТРИЯ ПОЗИЦИЙ  (zoom, xalign, yalign) — значения совпадают с твоими
#  transform normal_left / normal_center / normal_right и close_center.
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


# =============================================================================
#  ПАРАМЕТРИЧЕСКИЕ ТРАНСФОРМЫ
# =============================================================================

# точка покоя (для появления/обновления без движения)
transform chara_at(z, xa, ya):
    zoom z
    xalign xa
    yalign ya

# плавный въезд из-за экрана в точку покоя
transform chara_slide_in(z, xa, ya, sx):
    zoom z
    yalign ya
    xalign sx
    alpha 0.0
    easein 0.4 xalign xa alpha 1.0

# плавный выезд из точки покоя за экран
transform chara_slide_out(z, xa, ya, ex):
    zoom z
    yalign ya
    xalign xa
    alpha 1.0
    easeout 0.4 xalign ex alpha 0.0

# плавное ПЕРЕМЕЩЕНИЕ из старой точки покоя в новую (например center -> left),
# когда тот же персонаж остаётся на экране, но меняет позицию/размер.
transform chara_move(z0, xa0, ya0, z1, xa1, ya1):
    zoom z0
    xalign xa0
    yalign ya0
    ease 0.4 zoom z1 xalign xa1 yalign ya1


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

define _SLIDE_DUR = 0.4   # длительность слайда (синхронно с ease в трансформах)


# =============================================================================
#  СКРЫТЬ ВСЕХ ПЕРСОНАЖЕЙ ОДНОЙ КОМАНДОЙ
#     $ clear_chars()           — с dissolve
#     $ clear_chars(anim=None)  — мгновенно
# =============================================================================
init -1 python:

    def clear_chars(anim="dissolve"):
        for tag in CHARA_TAGS:
            renpy.hide(tag)
        store._sprite_slots = {}
        store._sprite_z = 0
        renpy.with_statement(dissolve if anim == "dissolve" else None)


# =============================================================================
#  1. ЗАТУХАНИЕ СЦЕНЫ  (всё внутри fade): спрайты сняты, интерфейс скрыт,
#     музыка затихает по флагу, фон меняется на new_bg или на чёрный.
#
#     $ fade_clear()                         -> в чёрный, музыка играет
#     $ fade_clear(stop_music=True)          -> в чёрный + музыка затихает
#     $ fade_clear("bg forest")              -> сразу новый фон под затуханием
#     $ fade_clear("bg forest", True)        -> новый фон + стоп музыки
#     $ fade_clear("bg forest", new_music="t17")  -> фон + завести трек audio.t17
#         (new_music сам останавливает старую музыку — stop_music не нужен)
# =============================================================================
init -1 python:

    def fade_clear(new_bg=None, stop_music=False, music_fadeout=1.0,
                   new_music=None, music_fadein=1.0):
        # 1) убрать всех персонажей
        for tag in CHARA_TAGS:
            renpy.hide(tag)
        store._sprite_slots = {}
        store._sprite_z = 0

        # 2) спрятать интерфейс на время затухания
        store.quick_menu = False
        if hasattr(store, "sympathy_hud_visible"):
            store._fade_hud_was = store.sympathy_hud_visible
            store.sympathy_hud_visible = False

        # 3) очистить мастер-слой и поставить фон/чёрный
        renpy.scene()
        if new_bg is not None:
            renpy.show(new_bg, at_list=[bg_center])
        else:
            renpy.show("black")

        # 4) музыка: при стопе или при смене трека гасим старую
        if stop_music or new_music is not None:
            renpy.music.stop(fadeout=music_fadeout)

        # 5) всё проигрывается ВНУТРИ затухания
        renpy.with_statement(fade)

        # 6) завести новый трек по короткому имени ("t17" -> audio.t17,
        #    либо передай полный путь "audio/bgm/t17.ogg")
        if new_music is not None:
            track = getattr(store.audio, new_music, new_music)
            renpy.music.play(track, fadein=music_fadein)

        # вернуть быстрые кнопки для последующих реплик
        store.quick_menu = True


# =============================================================================
#  4. УМНЫЙ ПОКАЗ 1-3 ПЕРСОНАЖЕЙ
# -----------------------------------------------------------------------------
#  show_sprites(chars, mode="normal", anim="dissolve", side=None, center_front=None)
#
#    chars  — строка (1 персонаж) или список/кортеж из 1..3 имён образов:
#               1 -> позиция из side (по умолчанию "center")
#               2 -> [левый, правый]
#               3 -> [левый, центр, правый]
#    mode   — "normal" / "big"
#    anim   — "dissolve" / "slide" / None (None = мгновенно, без анимации,
#                                          в т.ч. при смене эмоции)
#    side   — только для одного персонажа: "left"/"center"/"right"
#    center_front — порядок наложения для ЦЕНТРАЛЬНОГО при ПЕРВОМ показе:
#                   True  — центр сразу поверх боковых,
#                   False — центр сразу под боковыми,
#                   None  — обычный порядок.
#
#  ZORDER (наложение спрайтов):
#   • любой ПОКАЗАННЫЙ/ИЗМЕНЁННЫЙ в этом вызове спрайт получает новый, самый
#     высокий zorder -> «новый элемент перекрывает всех остальных»;
#   • неизменившиеся спрайты сохраняют свой прежний zorder и относительный
#     порядок (если d перекрывал s и оба не менялись — d так и перекрывает s).
#
#  ЛОГИКА (сравнение со старым раскладом по ТЕГУ персонажа):
#   • тот же персонаж в том же слоте  -> только смена эмоции/размера на месте;
#   • тот же персонаж в другом слоте  -> плавно переезжает (chara_move);
#   • персонаж пропал/сменился        -> старый уезжает (slide) или гаснет,
#                                         pause(0.2), затем заезжает новый;
#   • неизменившийся слот             -> остаётся как есть.
# =============================================================================
init -1 python:

    def show_sprites(chars, mode="normal", anim="slide", side=None,
                     center_front=None, hide_window=False):
        if isinstance(chars, str):
            chars = [chars]
        chars = list(chars)
        n = len(chars)

        if n == 1:
            layout = {(side or "center"): chars[0]}
        elif n == 2:
            layout = {"left": chars[0], "right": chars[1]}
        elif n == 3:
            layout = {"left": chars[0], "center": chars[1], "right": chars[2]}
        else:
            raise Exception("show_sprites: поддерживается от 1 до 3 персонажей")

        _apply_layout(layout, mode, anim, center_front, hide_window)


    def _apply_layout(layout, mode, anim, center_front, hide_window=False):
        slots  = store._sprite_slots         # slot -> (tag, img, mode, z)
        slide  = (anim == "slide")
        noanim = (anim is None)

        # Текстбокс в режиме "window auto" гаснет на каждом переходе (with).
        # По умолчанию УДЕРЖИВАЕМ окно на экране; hide_window=True — спрятать.
        if hide_window:
            _window_hide(None)
        else:
            _window_show(None)

        # новый расклад: slot -> (tag, image)
        new = {}
        for s, img in layout.items():
            new[s] = (_tag_of(img), img)

        # индексируем по ТЕГУ персонажа: кто ушёл / переехал / новый
        old_by_tag = {tag: (s, oimg, om, oz)
                      for s, (tag, oimg, om, oz) in slots.items()}
        new_by_tag = {tag: (s, nimg) for s, (tag, nimg) in new.items()}

        leavers  = []   # (slot, tag, img, mode)
        movers   = []   # (old_slot, new_slot, tag, img, old_mode)
        inplace  = []   # (slot, tag, img)
        entrants = []   # (slot, tag, img)

        for tag, (os_, oimg, om, oz) in old_by_tag.items():
            if tag not in new_by_tag:
                leavers.append((os_, tag, oimg, om))

        for tag, (ns_, nimg) in new_by_tag.items():
            old = old_by_tag.get(tag)
            if old is None:
                entrants.append((ns_, tag, nimg))
            else:
                os_, oimg, om, oz = old
                if os_ != ns_:
                    movers.append((os_, ns_, tag, nimg, om))
                elif oimg != nimg or om != mode:
                    inplace.append((ns_, tag, nimg))

        # ---- НАЗНАЧИТЬ ZORDER показанным/изменённым слотам ----
        # порядок начисления внутри вызова управляется center_front для центра:
        #   False -> центр получает z первым (ниже боковых этого вызова),
        #   True  -> центр последним (выше всех в этом вызове),
        #   None  -> естественный порядок.
        shown_slots = [m[1] for m in movers] + [p[0] for p in inplace] \
                      + [e[0] for e in entrants]

        def _order_key(s):
            if s != "center":
                return 1
            if center_front is True:
                return 2
            if center_front is False:
                return 0
            return 1

        slot_z = {}
        for s in sorted(shown_slots, key=_order_key):
            store._sprite_z += 1
            slot_z[s] = store._sprite_z

        # zorder неизменившихся слотов берём из прежнего состояния
        old_z_by_slot = {s: oz for s, (tag, oimg, om, oz) in slots.items()}

        # ---- 1) УХОДЯЩИЕ ----
        if leavers:
            if slide:
                for s, tag, oimg, om in leavers:
                    z, xa, ya = _geom(om, s)
                    renpy.show(oimg, at_list=[chara_slide_out(z, xa, ya, _off(s, "out"))],
                               tag=tag, zorder=old_z_by_slot.get(s, 20))
                renpy.with_statement(None)
                renpy.pause(_SLIDE_DUR)
                for s, tag, oimg, om in leavers:
                    renpy.hide(tag)
                renpy.with_statement(None)
            else:
                for s, tag, oimg, om in leavers:
                    renpy.hide(tag)
                renpy.with_statement(None if noanim else dissolve)

        # ---- 2) ПЕРЕЕЗЖАЮЩИЕ ----
        if movers:
            for os_, ns_, tag, nimg, om in movers:
                z1, xa1, ya1 = _geom(mode, ns_)
                if noanim:
                    renpy.show(nimg, at_list=[chara_at(z1, xa1, ya1)],
                               tag=tag, zorder=slot_z[ns_])
                else:
                    z0, xa0, ya0 = _geom(om, os_)
                    renpy.show(nimg, at_list=[chara_move(z0, xa0, ya0, z1, xa1, ya1)],
                               tag=tag, zorder=slot_z[ns_])
            renpy.with_statement(None)

        # небольшая задержка перед появлением новых (пропускаем без анимации)
        if (leavers or movers) and entrants and not noanim:
            renpy.pause(0.2)

        # ---- 3) СМЕНА ЭМОЦИИ/РАЗМЕРА НА МЕСТЕ ----
        if inplace:
            for s, tag, nimg in inplace:
                z, xa, ya = _geom(mode, s)
                renpy.show(nimg, at_list=[chara_at(z, xa, ya)],
                           tag=tag, zorder=slot_z[s])
            renpy.with_statement(None if noanim else dissolve)

        # ---- 4) НОВЫЕ ПЕРСОНАЖИ ----
        if entrants:
            if slide:
                for s, tag, nimg in entrants:
                    z, xa, ya = _geom(mode, s)
                    renpy.show(nimg, at_list=[chara_slide_in(z, xa, ya, _off(s, "in"))],
                               tag=tag, zorder=slot_z[s])
                renpy.with_statement(None)
                renpy.pause(_SLIDE_DUR)
            else:
                for s, tag, nimg in entrants:
                    z, xa, ya = _geom(mode, s)
                    renpy.show(nimg, at_list=[chara_at(z, xa, ya)],
                               tag=tag, zorder=slot_z[s])
                renpy.with_statement(None if noanim else dissolve)

        # ---- ПЕРЕСТРОИТЬ СОСТОЯНИЕ СЛОТОВ (с актуальным zorder) ----
        new_state = {}
        for s, (tag, nimg) in new.items():
            z = slot_z.get(s, old_z_by_slot.get(s, 0))
            new_state[s] = (tag, nimg, mode, z)
        store._sprite_slots = new_state


# =============================================================================
#  3. СКРЫТЬ / ВЕРНУТЬ ВЕСЬ ИНТЕРФЕЙС  (для окон инвентаря и т.п.)
#     call hide_interface  /  call show_interface
#     либо  $ hide_ui()  /  $ show_ui()
# =============================================================================
init -1 python:

    def hide_ui():
        store.quick_menu = False
        if hasattr(store, "sympathy_hud_visible"):
            store._ui_hud_was = store.sympathy_hud_visible
            store.sympathy_hud_visible = False
        renpy.hide_screen("quick_menu")
        renpy.hide_screen("sympathy_hud_icon")
        renpy.with_statement(None)

    def show_ui():
        store.quick_menu = True
        if hasattr(store, "_ui_hud_was"):
            store.sympathy_hud_visible = store._ui_hud_was
        renpy.show_screen("quick_menu")
        renpy.with_statement(None)

    # Python-версии, чтобы можно было вызывать ВНУТРИ обычных python-функций
    # (например в update_sympathy) как hide_interface() / show_interface().
    # Внутри def НЕЛЬЗЯ писать "$ hide_interface" — это синтаксис скрипта Ren'Py,
    # а не Python. Поэтому зови просто hide_interface() без знака $.
    def hide_interface():
        renpy.window_hide()
        hide_ui()

    def show_interface():
        show_ui()
        renpy.window_show()

# Лейблы для вызова из скрипта:  call hide_interface  /  call show_interface
label hide_interface:
    $ hide_interface()
    return

label show_interface:
    $ show_interface()
    return


# =============================================================================
#  5.1 FLASH, ГАСЯЩИЙ СПРАЙТЫ ОДНОВРЕМЕННО СО ВСПЫШКОЙ
# -----------------------------------------------------------------------------
#  $ flash_clear()             -> вспышка + все персонажи исчезают внутри неё
#  $ flash_clear("bg forest")  -> ещё и фон сменится под вспышкой
#  после — добавляем нужных вручную:
#     $ show_sprites("s 1", side="center", mode="big")
# =============================================================================
init -1 python:

    def flash_clear(new_bg=None):
        for tag in CHARA_TAGS:
            renpy.hide(tag)
        store._sprite_slots = {}
        store._sprite_z = 0
        if new_bg is not None:
            renpy.show(new_bg, at_list=[bg_center])
        renpy.with_statement(flash)


# =============================================================================
#  5.2 ТРЯСКА ЭКРАНА  (shake / flash / fade) С КОНТРОЛЕМ СПРАЙТОВ
# -----------------------------------------------------------------------------
#  Проблема "scene bg forest with hit_shake": команда scene стирает ВСЕ слои,
#  включая спрайты, а состояние слотов об этом не знает -> show_sprites потом
#  «не видит» снесённые спрайты и часть из них не возвращается.
#
#  shake_scene НЕ вызывает scene: по умолчанию спрайты ОСТАЮТСЯ на месте и
#  просто трясутся вместе с фоном. Дальше можно менять эмоции через show_sprites
#  — анимируется только изменившийся, остальные на месте.
#
#  shake_scene(sound=None, effect="shake", new_bg=None, clear=False)
#    sound  — путь к звуку, напр. "audio/sfx/punch.ogg" (None — без звука)
#    effect — "shake" (hit_shake) / "flash" / "fade" / None (без перехода)
#    new_bg — сменить фон под эффектом (None — фон не трогаем)
#    clear  — True: убрать ВСЕХ персонажей и сбросить слоты (после нужно
#             заново показать всех через show_sprites);
#             False (по умолчанию): спрайты остаются.
#
#  Примеры:
#    # тряхнуть всё как есть + звук удара, спрайты на месте:
#    $ shake_scene(sound="audio/sfx/punch.ogg")
#    $ show_sprites(("l 1 angry", "s 3 angry"))   # меняем только эмоции
#
#    # вспышка, всех снести, потом показать заново:
#    $ shake_scene(sound="audio/sfx/punch.ogg", effect="flash", clear=True)
#    $ show_sprites(("l 1 angry", "s 3 angry"))
#
#    # тряска со сменой фона:
#    $ shake_scene(effect="shake", new_bg="bg forest")
# =============================================================================
init -1 python:

    def shake_scene(sound=None, effect="shake", new_bg=None, clear=False):
        if sound is not None:
            renpy.sound.play(sound)

        if clear:
            for tag in CHARA_TAGS:
                renpy.hide(tag)
            store._sprite_slots = {}
            store._sprite_z = 0

        if new_bg is not None:
            renpy.show(new_bg, at_list=[bg_center])

        trans = {
            "shake": hit_shake,
            "flash": flash,
            "fade":  fade,
            None:    None,
        }.get(effect, hit_shake)

        renpy.with_statement(trans)
