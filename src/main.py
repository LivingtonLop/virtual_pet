import pygame
import sys

from player import Player

list_label_sprite = ["normal","sleep","eat","play","bath","dead"]

player = Player(400,400)

player.list_label_sprite = list_label_sprite
player.number_row_sprite_sheet = 6
player.number_column_sprite_sheet = 4

sprite_all = player.load_sprite_sheet(sprite_sheet="virtual_pet_sprite_sheet128x192")

player.welcome_init(background="house_virtual_pet128x128",sprite_init=sprite_all["normal"])


pygame.quit()
sys.exit()


# import pygame
# import sys

# from helpers import Helpers
# from buttons import Button
# from screen_manager import  ScreenManager

# screen_width = 400
# screen_height = 400

# list_background = {
#     "sleep" : "sleep_virtual_pet128x128",
#     "eat" : "eat_virtual_pet128x128",
#     "play" : "play_virtual_pet128x128",
#     "bath" : "bath_virtual_pet128x128",
#     "normal":"house_virtual_pet128x128"
# }

# list_label_sprite = ["normal","sleep","eat","play","bath","dead"]


# #Temporal
# def on_btn_click(variable):
#     global background, sprite_a

#     filename = list_background.get(variable)
#     sprite_a = sprite_all[variable]
#     background = screen_manager.load_background(background=filename)
#     print(variable)

# #inits
# screen_manager = ScreenManager(screen_width=screen_width,screen_height=screen_height,list_label_sprite=list_label_sprite, number_row_sprite_sheet=6, number_column_sprite_sheet=4)

# #Animation Pets
# sprite_position = (150, 230)
# current_sprite_index = 0
# animation_speed = 200

# background = screen_manager.load_background(background="house_virtual_pet128x128") #background
# sprite_all = screen_manager.load_sprite_sheet(sprite_sheet="virtual_pet_sprite_sheet128x192") #sprites

# #buttons
# button_sleep_image = screen_manager.load_images_button(button_image="button_sleep_virtual_pet32x32")
# button_eat_image = screen_manager.load_images_button(button_image="button_eat_virtual_pet32x32")
# button_play_image = screen_manager.load_images_button(button_image="button_play_virtual_pet32x32")
# button_bath_image = screen_manager.load_images_button(button_image="button_bath_virtual_pet32x32")
# button_house_image = screen_manager.load_images_button(button_image="button_house_virtual_pet32x32")

# button_state_pressed = screen_manager.load_images_button(button_image="button_states_pressed_virtual_pet32x32")

# button_house = Button(330,30,200,100,image_normal=button_house_image, image_pressed=button_state_pressed, on_click=lambda : on_btn_click("normal"))
# button_sleep = Button(30,70,200,100,image_normal=button_sleep_image,image_pressed=button_state_pressed,on_click=lambda : on_btn_click("sleep"))
# button_eat = Button(30,140,200,100,image_normal=button_eat_image,image_pressed=button_state_pressed,on_click=lambda : on_btn_click("eat"))
# button_play = Button(30,210,200,100,image_normal=button_play_image,image_pressed=button_state_pressed,on_click=lambda : on_btn_click("play"))
# button_bath = Button(30,280,200,100,image_normal=button_bath_image,image_pressed=button_state_pressed,on_click=lambda : on_btn_click("bath"))


# sprite_a = sprite_all["normal"] #First Row to Normal

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

#     screen_manager.screen.blit(background, (0, 0))
#     button_sleep.update(screen=screen_manager.screen)
#     button_eat.update(screen=screen_manager.screen)
#     button_play.update(screen=screen_manager.screen)
#     button_bath.update(screen=screen_manager.screen)
#     button_house.update(screen=screen_manager.screen)

#     current_sprite = sprite_a[current_sprite_index]
#     screen_manager.screen.blit(current_sprite, sprite_position)


#     pygame.display.flip()

#     pygame.time.wait(animation_speed)

#     current_sprite_index = (current_sprite_index + 1) % len(sprite_a)

#     screen_manager.clock.tick(60)

# pygame.quit()
# sys.exit()


