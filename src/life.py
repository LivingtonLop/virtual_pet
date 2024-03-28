import random

from helpers import Helpers

class Life(Helpers):
    
    def __init__(self, pet : dict):
        super().__init__(list_label_sprite=[],number_column_sprite_sheet=0, number_row_sprite_sheet=0)
        self.pet = pet
        self.limit = 1000
    def plus_status(self):
        
        if self.pet["sleep"] <= self.limit:
            self.pet["sleep"] += random.randint(0,2)

        if self.pet["play"] <= self.limit:
            self.pet["play"] += random.randint(0,3)

        if self.pet["eat"] <= self.limit:
            self.pet["eat"] += random.randint(0,4)

        if self.pet["bath"] <= self.limit:
            self.pet["bath"] += random.randint(0,1)

        self.save_entitys(name_pet=self.pet["pet_name"], number_sleep=self.pet["sleep"], number_eat=self.pet["eat"], number_play=self.pet["play"], number_bath=self.pet["bath"])

    def rest_status(self, status : str):
        print(f"- status : {status}")
        print(f"{status}: {self.pet[status]}")

        self.pet[status] = 0

        self.save_entitys(name_pet=self.pet["pet_name"], number_sleep=self.pet["sleep"], number_eat=self.pet["eat"], number_play=self.pet["play"], number_bath=self.pet["bath"])

        #1 to 100 = / 1 to 10 this function rest 10 to 100