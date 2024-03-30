import random
import pygame

from helpers import Helpers

class Life(Helpers):
    
    def __init__(self, pet : dict, screen):
        super().__init__(list_label_sprite=[],number_column_sprite_sheet=0, number_row_sprite_sheet=0)
        self.pet = pet
        self.limit = 100

        self.font = pygame.font.Font(None, 20)
        self.messages = {
            "sleep":["Necesita Dormir!!",0],
            "play": ["Necesita Jugar!!",0],
            "eat":["Necesita Comer",0],
            "bath":["Necesita Banarse",0]
        }
        self.screen = screen
        self.y_text_on_screen = self.screen.get_height()-50 

    def plus_status(self):
        
        if self.pet["sleep"] <= self.limit: self.pet["sleep"] += random.randint(0,2)
        else:  self.display_message_of_status(status = "sleep",y = self.y_text_on_screen)

        if self.pet["play"] <= self.limit: self.pet["play"] += random.randint(0,3)
        else: self.display_message_of_status(status = "play",y = self.y_text_on_screen )

        if self.pet["eat"] <= self.limit: self.pet["eat"] += random.randint(0,4)
        else: self.display_message_of_status(status = "eat",y = self.y_text_on_screen )

        if self.pet["bath"] <= self.limit: self.pet["bath"] += random.randint(0,1)
        else: self.display_message_of_status(status = "bath",y = self.y_text_on_screen )

        self.save_entitys(name_pet=self.pet["pet_name"], number_sleep=self.pet["sleep"], number_eat=self.pet["eat"], number_play=self.pet["play"], number_bath=self.pet["bath"])

    def rest_status(self, status : str):
        print(f"- status : {status}")
        print(f"{status}: {self.pet[status]}")

        self.pet[status] = 0

        self.save_entitys(name_pet=self.pet["pet_name"], number_sleep=self.pet["sleep"], number_eat=self.pet["eat"], number_play=self.pet["play"], number_bath=self.pet["bath"])

    def display_message_of_status(self, status:str, y:int):

        if self.messages[status][1] == 0:
            self.messages[status][1] = y

            text_surface = self.font.render(self.messages[status][0], True, (0, 0, 0))
            text_rect = text_surface.get_rect(bottomright=(self.screen.get_width() - 10, y))
            pygame.draw.rect(self.screen, (255, 255, 255), text_rect)
            self.screen.blit(text_surface, text_rect)
        
            self.y_text_on_screen -= text_rect.height + 5

        else:
            text_surface = self.font.render(self.messages[status][0], True, (0, 0, 0))
            text_rect = text_surface.get_rect(bottomright=(self.screen.get_width() - 10, self.messages[status][1]))
            pygame.draw.rect(self.screen, (255, 255, 255), text_rect)
            self.screen.blit(text_surface, text_rect)
        