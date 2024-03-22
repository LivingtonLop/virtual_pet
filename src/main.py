
import pygame
import sys
import time

from helpers import Helpers

# Inicializar Pygame
pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Animación de la primera fila")



sprite_position = (150, 230)  # Cambia estas coordenadas según lo que desees
current_sprite_index = 0
animation_speed = 200  # 200 ms
clock = pygame.time.Clock()

list_label_sprite = ["normal","sleep","eat","play","bath","dead"]

helper = Helpers(screen_width=400,screen_height=400,resized_button_width=70,resized_button_height=70,resized_sprite_width=100,resized_sprite_height=100,number_row_sprite_sheet=6, number_column_sprite_sheet=4,list_label_sprite=list_label_sprite)

background = helper.load_background(background="house_virtual_pet128x128")
sprite_all = helper.load_sprite_sheet(sprite_sheet="virtual_pet_sprite_sheet128x192")

button_sleep = helper.load_images_button(button_image="button_sleep_virtual_pet32x32")
button_eat = helper.load_images_button(button_image="button_eat_virtual_pet32x32")
button_play = helper.load_images_button(button_image="button_play_virtual_pet32x32")
button_bath = helper.load_images_button(button_image="button_bath_virtual_pet32x32")

sprite_a = sprite_all["normal"]

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

#Temporal
def on_btn_click(message):
    print(message)

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    current_sprite = sprite_a[current_sprite_index]
    screen.blit(current_sprite, sprite_position)

    #draw btns

    helper.draw_button(screen=screen,button_image=button_sleep,x=0,y=100, action_button=on_btn_click,msg = "dormir")
    helper.draw_button(screen=screen,button_image=button_eat,x=0,y=170, action_button=on_btn_click, msg = "comer")
    helper.draw_button(screen=screen,button_image=button_play,x=0,y=240, action_button=on_btn_click, msg = "jugar")
    helper.draw_button(screen=screen,button_image=button_bath,x=0,y=310, action_button=on_btn_click, msg = "banarse")


    pygame.display.flip()

    pygame.time.wait(animation_speed)

    current_sprite_index = (current_sprite_index + 1) % len(sprite_a)

    clock.tick(60)

pygame.quit()
sys.exit()
