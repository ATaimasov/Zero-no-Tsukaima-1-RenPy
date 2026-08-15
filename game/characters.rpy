define s = Character(_("Saito"), color="#3874a3")
define l = Character(_("Louise"), color="#fd7589")
define k = Character(_("Kirche"), color="#e36566")
define t = Character(_("Tabitha"), color="#b4dfec")
define c = Character(_("Kolbert"), color="#5e5b51")
define h = Character(_("Henrietta"), color="#782163")
define si = Character(_("Siesta"), color="#535a6a")
define ha = Character(_("Haruna"), color="#4b4d51")
define g = Character(_("Guiche"), color="#f3e69d")
define d = Character(_("Derflinger"), color="#9d996b")
define o = Character(_("Osmond"), color="#ddd7d4")
define m = Character(_("Montmorency"), color="#e2d79d")


define npc1 = Character(_("Сommander"), color="#797979")
define npc2 = Character(_("Soldier"), color="#797979")
define mage = Character(_("Mage"), color="#d82b2b")
define unds = Character(_("Underlings"), color="#d82b2b")


define unk = Character(_("???"), color="#000000") #protagonist
define unk_ha = Character(_("???"), color="#4b4d51") # haruna
define unk_k = Character(_("???"), color="#e36566") #kirche


define th = Character(None, 
    what_italic=True,
    what_color="#3874a3",
    window_style='thought_window'
)

# ----------------------------------------------------------------------------
#  ОБЩИЙ СЛОВАРЬ СУЩНОСТЕЙ ПЕРСОНАЖЕЙ
#  Здесь хранятся портреты (для экрана с портретами) и спрайты (для экрана
#  со спрайтом сбоку). Один общий реестр на всю игру - добавляй персонажей сюда.
#
#    "name"     - отображаемое имя (можно использовать в подписях/подсказках)
#    "portrait" - путь к портрету (карточка лица) для portrait_choice
#    "sprite"   - спрайт для sprite_choice. Это может быть либо тег
#                 существующего image ("si 1", "l 1" ...), либо путь к файлу
#                 ("images/sprites/siesta.webp"). Оба варианта работают в add.
# ----------------------------------------------------------------------------
define char_data = {
    "saito":       {"name": "Saito",       "portrait_choise": "gui/system/portraits/choises/s_full.webp",  "sprite_choise": "s 1"},
    "louise":      {"name": "Louise",      "portrait_choise": "gui/system/portraits/choises/l_full.webp",  "sprite_choise": "l 1"},
    "siesta":      {"name": "Siesta",      "portrait_choise": "gui/system/portraits/choises/si_full.webp", "sprite_choise": "si 1"},
    "tabitha":     {"name": "Tabitha",     "portrait_choise": "gui/system/portraits/choises/t_full.webp",  "sprite_choise": "t 1"},
    "kirche":      {"name": "Kirche",      "portrait_choise": "gui/system/portraits/choises/k_full.webp",  "sprite_choise": "k 1"},
    "henrietta":   {"name": "Henrietta",   "portrait_choise": "gui/system/portraits/choises/h_full.webp",  "sprite_choise": "h 1"},
    "montmorency": {"name": "Montmorency", "portrait_choise": "gui/system/portraits/choises/m_full.webp",  "sprite_choise": "m 1"},
    "haruna": {"name": "Haruna", "portrait_choise": "gui/system/portraits/choises/ha_full.webp",  "sprite_choise": "ha 1"},
}




# define tiffania = Character(_("Тиффания"), color="#fec979")
# define agnes = Character(_("Агнес"), color="#ede2ba")
