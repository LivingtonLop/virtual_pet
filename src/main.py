
import pygame
import sys

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

helper = Helpers(screen_width=400,screen_height=400,resized_sprite_width=100,resized_sprite_height=100,number_row_sprite_sheet=6, number_column_sprite_sheet=4)

background = helper.load_background(background="house_virtual_pet128x128")
sprite_all = helper.load_sprite_sheet(sprite_sheet="virtual_pet_sprite_sheet128x192")
sprite_a = sprite_all[0]


running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    current_sprite = sprite_a[current_sprite_index]
    screen.blit(current_sprite, sprite_position)

    pygame.display.flip()

    pygame.time.wait(animation_speed)

    current_sprite_index = (current_sprite_index + 1) % len(sprite_a)

    clock.tick(60)

pygame.quit()
sys.exit()
