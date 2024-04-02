import pygame 

from screen_manager import ScreenManager
from buttons import Button
class Player(ScreenManager):
    def __init__(self, screen_width :int, screen_height:int):
        super().__init__(screen_width=screen_width, screen_height=screen_height, list_label_sprite=[], number_row_sprite_sheet=0, number_column_sprite_sheet=0)
        #load buttons
        self.init_game = True

        self.resized_button_height = 50
        self.resized_button_width = 50

        button_new_pet = self.load_images_button("button_new_virtual_pet32x32")
        button_pressed_new_pet = self.load_images_button("button_pressed_new_virtual_pet32x32")
        self.list_pets = self.saved_entitys()
        if type(self.list_pets) is dict:        
            self.resized_button_height = 70
            self.resized_button_width = 70

            button_pressed_continue_pet = self.load_images_button("button_states_pressed_virtual_pet32x32")
            button_continue_new_pet = self.load_images_button("button_continue_virtual_pet32x32")
            self.button_continue_pet = Button(x=300,y=170,width=200,height=100,image_normal=button_continue_new_pet, image_pressed=button_pressed_continue_pet, on_click=lambda : self.finish_welcome())

        self.button_new_pet = Button(x=300,y=70,width=200,height=100,image_normal=button_new_pet, image_pressed=button_pressed_new_pet, on_click=lambda : self.get_name_pet())


    def welcome_init(self,background : str,sprite_init : list)-> dict:
        background_init = self.load_background(background=background) #background
        current_sprite_index = 0
        sprite_position = (150, 230)

        font = pygame.font.Font(None,36)

        for i in range(101):
            pygame.time.wait(50)
            if i >= 95 :pygame.time.wait(1000)
            background_init.set_alpha(i * 2,55)
            self.screen.blit(background_init, (0,0))
            texture_surface = font.render(f"Cargando: {i}%", True, (255,255,255))
            self.screen.blit(texture_surface,(100,200))
            self.update_screen()
            self.screen.fill((0,0,0))
        quit_screen = False
        while self.init_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.init_game = False
                    quit_screen = True
                else:
                    self.button_new_pet.handle_event(event=event)
                    if type(self.list_pets) is dict:self.button_continue_pet.handle_event(event=event)
                if not self.handle_event_input(event=event):self.finish_welcome()

            self.screen.blit(background_init, (0,0))
            
            current_sprite = sprite_init[current_sprite_index]
            
            self.screen.blit(current_sprite, sprite_position)
            
            self.button_new_pet.update(self.screen)
            if type(self.list_pets) is dict:self.button_continue_pet.update(self.screen)
            pygame.time.wait(200)

            current_sprite_index = (current_sprite_index + 1) % len(sprite_init)
            self.draw_label(text="New Pet",x=100,y=180)
            self.draw_input(rect=self.rect)
            self.update_screen()
            self.clock.tick(60)
            self.screen.fill((0,0,0))

        return self.saved_entitys() if not quit_screen else []

    def finish_welcome(self):
        self.save_entitys(name_pet=self.text,number_sleep=0, number_eat=0, number_play=0, number_bath=0)
        self.text = ""
        self.init_game = False
        self.list_pets = self.saved_entitys()

    def get_name_pet(self): #draw
        self.active = True
        self.visible = True 
    