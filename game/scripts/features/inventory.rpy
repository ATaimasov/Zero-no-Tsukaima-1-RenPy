# ## inventory.rpy - Система инвентаря

# default curr_items = {
#     "Bread": 3,
#     "Herb": 3,
#     "Elixir": 3,
# }


# init python:
#     # items dict
#     items = {
#         "Bread": {
#             "description": "Restore HP",
#         },
#         "Herb": {
#             "description": "Restore MP"
#         },
#         "Elixir": {
#             "description": "Restore HP and MP"
#         }
#     }

# # Экран инвентаря (заглушка)
# screen inventory():
#     tag menu
#     modal True
    
#     add "#00000088"
    
#     frame:
#         xalign 0.5
#         yalign 0.5
#         xsize 800
#         ysize 500
#         background "#e8d5b8"
#         padding (20, 20)
        
#         vbox:
#             spacing 15
            
#             frame:
#                 background "#8b5a2b"
#                 xalign 0.5
#                 padding (30, 10)
#                 text "Items" color "#fff8e7" size 28 bold True
            
#             text "Здесь будет список предметов..." xalign 0.5 color "#5c3d2e"
            
#             textbutton "Close":
#                 xalign 0.5
#                 style "battle_menu_button"
#                 text_style "battle_menu_button_text"
#                 action Return()

