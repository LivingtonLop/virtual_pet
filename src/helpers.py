import pygame
import json
import os
class Helpers ():
    def __init__(self, list_label_sprite : list, number_row_sprite_sheet :int, number_column_sprite_sheet:int, screen_width=400,screen_height=400,resized_button_width = 70, resized_button_height = 70, resized_sprite_width=100,resized_sprite_height=100):

        self.screen_width = screen_width
        self.screen_height = screen_height

        self.resized_sprite_width = resized_sprite_width
        self.resized_sprite_height = resized_sprite_height

        self.resized_button_height = resized_button_height
        self.resized_button_width = resized_button_width

        self.number_row_sprite_sheet = number_row_sprite_sheet
        self.number_column_sprite_sheet = number_column_sprite_sheet

        self.list_label_sprite = list_label_sprite

    def load_background(self, background : str):
        background_init = pygame.image.load(f"assets/images/backgrounds/{background}.png")
        background_init = pygame.transform.scale(background_init, (self.screen_width, self.screen_height))
        return background_init
    
    def load_sprite_sheet(self, sprite_sheet: str) -> dict:
        sprite_sheet_init = pygame.image.load(f"assets/sprites/{sprite_sheet}.png")
        
        sheet_width, sheet_height = sprite_sheet_init.get_size()
        sprite_width = sheet_width // 4 
        sprite_height = sheet_height // 6
        
        list_sprites = []

        for y in range(self.number_row_sprite_sheet):
            sprites_row = []
            for x in range(self.number_column_sprite_sheet):
                sprite_x = x * sprite_width
                sprite_y = y * sprite_height

                sprite = sprite_sheet_init.subsurface((sprite_x, sprite_y, sprite_width, sprite_height))
                resized_sprite = pygame.transform.scale(sprite, (self.resized_sprite_width, self.resized_sprite_height))

                sprites_row.append(resized_sprite) #[0,1,2,4]

            list_sprites.append(sprites_row) #[[A],[B]...]

        sprites_all = {}

        for label, sprite_row in zip(self.list_label_sprite, list_sprites):
            sprites_all[label] = sprite_row

        return sprites_all
    
    def load_images_button(self,button_image:str):
        button_init = pygame.image.load(f"assets/images/buttons/{button_image}.png")
        button_init = pygame.transform.scale(button_init, (self.resized_button_width, self.resized_button_height))
        return button_init
        
    def saved_entitys(self)->dict:
        file = "data/pets/pets.json"
        pets = None
        if os.path.exists(file):
            with open(file, "r") as file_json:
                pets = json.load(file_json)
        return pets

    def save_entitys(self, name_pet:str, number_sleep:int, number_eat:int, number_play:int, number_bath:int):
        pet = {"pet_name": name_pet, "sleep":number_sleep , "play":number_play , "eat": number_eat,"bath":number_bath}
        file = "data/pets/pets.json"
        pets = {}
        
        if os.path.exists(file):
            with open(file, "r") as file_json:
                pets = json.load(file_json)
        pets.update(pet)
        with open(file, "w") as archivo_json:
            json.dump(pets, archivo_json, indent=4)