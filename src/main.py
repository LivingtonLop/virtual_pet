
#player


# import pygame
# import sys

# from helpers import Helpers
# from buttons import Button
# # Inicializar Pygame
# pygame.init()

# screen_width = 400
# screen_height = 400
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Animación de la primera fila")

# list_backgorund = {
#     "sleep" : "sleep_virtual_pet128x128",
#     "eat" : "eat_virtual_pet128x128",
#     "play" : "play_virtual_pet128x128",
#     "bath" : "bath_virtual_pet128x128",
#     "normal":"house_virtual_pet128x128"
    
# }

# #Temporal
# def on_btn_click(variable):
#     global background, sprite_a

#     filename = list_backgorund.get(variable)
#     sprite_a = sprite_all[variable]
#     background = helper.load_background(background=filename)
#     print(variable)

# sprite_position = (150, 230)  # Cambia estas coordenadas según lo que desees
# current_sprite_index = 0
# animation_speed = 200  # 200 ms
# clock = pygame.time.Clock()

# list_label_sprite = ["normal","sleep","eat","play","bath","dead"]

# helper = Helpers(screen_width=400,screen_height=400,resized_button_width=70,resized_button_height=70,resized_sprite_width=100,resized_sprite_height=100,number_row_sprite_sheet=6, number_column_sprite_sheet=4,list_label_sprite=list_label_sprite)

# background = helper.load_background(background="house_virtual_pet128x128")
# sprite_all = helper.load_sprite_sheet(sprite_sheet="virtual_pet_sprite_sheet128x192")

# button_sleep_image = helper.load_images_button(button_image="button_sleep_virtual_pet32x32")
# button_eat_image = helper.load_images_button(button_image="button_eat_virtual_pet32x32")
# button_play_image = helper.load_images_button(button_image="button_play_virtual_pet32x32")
# button_bath_image = helper.load_images_button(button_image="button_bath_virtual_pet32x32")
# button_house_image = helper.load_images_button(button_image="button_house_virtual_pet32x32")

# button_state_pressed = helper.load_images_button(button_image="button_states_pressed_virtual_pet32x32")



# button_house = Button(330,30,200,100,image_normal=button_house_image, image_pressed=button_state_pressed, on_click=lambda : on_btn_click("normal"))
# button_sleep = Button(30,70,200,100,image_normal=button_sleep_image,image_pressed=button_state_pressed,on_click=lambda : on_btn_click("sleep"))
# button_eat = Button(30,140,200,100,image_normal=button_eat_image,image_pressed=button_state_pressed,on_click=lambda : on_btn_click("eat"))
# button_play = Button(30,210,200,100,image_normal=button_play_image,image_pressed=button_state_pressed,on_click=lambda : on_btn_click("play"))
# button_bath = Button(30,280,200,100,image_normal=button_bath_image,image_pressed=button_state_pressed,on_click=lambda : on_btn_click("bath"))


# sprite_a = sprite_all["normal"]

# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)


# running = True
# while running:

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         else:
#             #load btns
#             button_sleep.handle_event(event=event)
#             button_eat.handle_event(event=event)
#             button_play.handle_event(event=event)
#             button_bath.handle_event(event=event)
#             button_house.handle_event(event=event)



#     screen.blit(background, (0, 0))
#     button_sleep.update(screen=screen)
#     button_eat.update(screen=screen)
#     button_play.update(screen=screen)
#     button_bath.update(screen=screen)
#     button_house.update(screen=screen)

#     current_sprite = sprite_a[current_sprite_index]
#     screen.blit(current_sprite, sprite_position)


#     pygame.display.flip()

#     pygame.time.wait(animation_speed)

#     current_sprite_index = (current_sprite_index + 1) % len(sprite_a)

#     clock.tick(60)

# pygame.quit()
# sys.exit()


# screen_manager = ScreenManager()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     elements_to_draw = []  # Agrega tus elementos aquí

#     screen_manager.draw_elements(elements_to_draw)

#     screen_manager.update_screen()

#     screen_manager.clock.tick(60)

# pygame.quit()
# sys.exit()
