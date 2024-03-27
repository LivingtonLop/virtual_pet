import pygame 

from screen_manager import ScreenManager
from buttons import Button
class Pet(ScreenManager):
    def __init__(self, screen_width :int, screen_height:int):
        list_label_sprite = ["normal","sleep","eat","play","bath","dead"]

        super().__init__(screen_width=screen_width, screen_height=screen_height, list_label_sprite=list_label_sprite, number_row_sprite_sheet=6, number_column_sprite_sheet=4)
        #load buttons
        self.init_game = True
        
        self.list_background = {
            "sleep" : "sleep_virtual_pet128x128",
            "eat" : "eat_virtual_pet128x128",
            "play" : "play_virtual_pet128x128",
            "bath" : "bath_virtual_pet128x128",
            "normal":"house_virtual_pet128x128"
        }

        self.background = self.load_background(background=self.list_background["normal"]) #background
        self.sprite_all = self.load_sprite_sheet(sprite_sheet="virtual_pet_sprite_sheet128x192") #sprites
        self.sprite_a = self.sprite_all["normal"]
        #buttons
        button_sleep_image = self.load_images_button(button_image="button_sleep_virtual_pet32x32")
        button_eat_image = self.load_images_button(button_image="button_eat_virtual_pet32x32")
        button_play_image = self.load_images_button(button_image="button_play_virtual_pet32x32")
        button_bath_image = self.load_images_button(button_image="button_bath_virtual_pet32x32")
        button_house_image = self.load_images_button(button_image="button_house_virtual_pet32x32")

        button_state_pressed = self.load_images_button(button_image="button_states_pressed_virtual_pet32x32")

        button_house = Button(330,30,200,100,image_normal=button_house_image, image_pressed=button_state_pressed, on_click=lambda : self.on_btn_click("normal"))
        button_sleep = Button(30,70,200,100,image_normal=button_sleep_image,image_pressed=button_state_pressed,on_click=lambda : self.on_btn_click("sleep"))
        button_eat = Button(30,140,200,100,image_normal=button_eat_image,image_pressed=button_state_pressed,on_click=lambda : self.on_btn_click("eat"))
        button_play = Button(30,210,200,100,image_normal=button_play_image,image_pressed=button_state_pressed,on_click=lambda : self.on_btn_click("play"))
        button_bath = Button(30,280,200,100,image_normal=button_bath_image,image_pressed=button_state_pressed,on_click=lambda : self.on_btn_click("bath"))

        self.list_buttons_to_draw = [button_house, button_sleep, button_eat, button_play, button_bath]

    def on_btn_click(self, action:str):
        filename = self.list_background.get(action)
        self.sprite_a = self.sprite_all[action]
        self.background = self.load_background(background=filename)
        print(action)

    def welcome_init(self)-> dict:
        sprite_position = (150, 230)
        current_sprite_index = 0
        animation_speed = 200

        while self.init_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.init_game = False
                else:
                    #load btns
                    self.handle_elements(elements=self.list_buttons_to_draw,event=event)

                self.screen.blit(self.background, (0, 0))
                self.update_elements(elements=self.list_buttons_to_draw)
                
                current_sprite = self.sprite_a[current_sprite_index]
                self.screen.blit(current_sprite, sprite_position)

                pygame.display.flip()

                pygame.time.wait(animation_speed)

                current_sprite_index = (current_sprite_index + 1) % len(self.sprite_a)

                self.clock.tick(60)

        return self.init_game

    