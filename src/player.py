import os
import json
import pygame 

from screen_manager import ScreenManager
from buttons import Button
class Player(ScreenManager):
    def __init__(self, screen_width :int, screen_height:int):
        super().__init__(screen_width=screen_width, screen_height=screen_height, list_label_sprite=[], number_row_sprite_sheet=0, number_column_sprite_sheet=0)
        
        #load buttons
        self.resized_button_height = 50
        self.resized_button_width = 50

        button_new_pet = self.load_images_button("button_new_virtual_pet32x32")
        button_pressed_new_pet = self.load_images_button("button_pressed_new_virtual_pet32x32")

        self.resized_button_height = 70
        self.resized_button_width = 70

        button_pressed_continue_pet = self.load_images_button("button_states_pressed_virtual_pet32x32")
        button_continue_new_pet = self.load_images_button("button_continue_virtual_pet32x32")

        self.button_new_pet = Button(x=300,y=70,width=200,height=100,image_normal=button_new_pet, image_pressed=button_pressed_new_pet, on_click=lambda : print("Nuevo"))
        self.button_continue_pet = Button(x=300,y=170,width=200,height=100,image_normal=button_continue_new_pet, image_pressed=button_pressed_continue_pet, on_click=lambda : print("continuamos"))


    def welcome_init(self,background : str,sprite_init : list):
        background_init = self.load_background(background=background) #background
        current_sprite_index = 0
        sprite_position = (150, 230)

        font = pygame.font.Font(None,36)

        for i in range(101):
            pygame.time.wait(50)
            #print("Cargando: ", i, "%")
            if i >= 95 :pygame.time.wait(1000)
            background_init.set_alpha(i * 2,55)
            self.screen.blit(background_init, (0,0))
            texture_surface = font.render(f"Cargando: {i}%", True, (255,255,255))
            self.screen.blit(texture_surface,(100,200))
            self.update_screen()
            self.screen.fill((0,0,0))

        init_game = True
        while init_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    init_game = False
                else:
                    self.button_new_pet.handle_event(event=event)
                    self.button_continue_pet.handle_event(event=event)


            self.screen.blit(background_init, (0,0))
            
            current_sprite = sprite_init[current_sprite_index]
            self.screen.blit(current_sprite, sprite_position)
            self.button_new_pet.update(self.screen)
            self.button_continue_pet.update(self.screen)
            pygame.time.wait(200)

            current_sprite_index = (current_sprite_index + 1) % len(sprite_init)

            self.update_screen()
            self.clock.tick(60)
            self.screen.fill((0,0,0))



    def get_name_pet(self): #draw
        pass

    def save_pet(self, name_pet:str, number_sleep:int, number_eat:int, number_play:int, number_clear:int):
        pet = {"pet_name": name_pet, "sleep":number_sleep , "play":number_play , "eat": number_eat,"clear":number_clear}
        file = "data/pets/pets.json"
        pets = {}
        
        if os.path.exists(file):
            with open(file, "r") as file_json:
                pets = json.load(file_json)

        pets.update(pet)

        with open(file, "w") as archivo_json:
            json.dump(pets, archivo_json, indent=4)
    