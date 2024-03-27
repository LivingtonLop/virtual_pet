import pygame
import sys

from player import Player
from pet import Pet

list_label_sprite = ["normal","sleep","eat","play","bath","dead"]

player = Player(400,400)

player.list_label_sprite = list_label_sprite
player.number_row_sprite_sheet = 6
player.number_column_sprite_sheet = 4

sprite_all = player.load_sprite_sheet(sprite_sheet="virtual_pet_sprite_sheet128x192")

game = player.welcome_init(background="house_virtual_pet128x128",sprite_init=sprite_all["normal"])

if type(game) is dict:
    print("Continuamos con el juego pero con la clase Pet")

    player = None
    player = Pet(400,400)
    game = None
    game = player.welcome_init()

pygame.quit()
sys.exit()



