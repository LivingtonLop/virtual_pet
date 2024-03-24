import os
import json

class Player():
    def __init__(self) -> None:
        pass
    
    def welcome_init(self):
        pass

    def get_name_pet(self):
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
    