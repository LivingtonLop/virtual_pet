import pygame

from helpers import Helpers
class ScreenManager(Helpers):
    def __init__(self, screen_width:int , screen_height:int,list_label_sprite:list, number_row_sprite_sheet:int, number_column_sprite_sheet:int):
        super().__init__(list_label_sprite, number_row_sprite_sheet, number_column_sprite_sheet)
        
        pygame.init()
        self.screen = pygame.display.set_mode((screen_height,screen_width))
        self.clock = pygame.time.Clock()

    def update_screen(self):
        pygame.display.flip()

    def draw_elements(self, elements:list): #geo y text
        for element in elements:
            element.draw(self.screen)

    def blit_elements(self, elements:list): #img
        for element in elements:
            element.blit(self.screen)

    def handle_elements(self, elements:list, event):
        for element in elements:
            element.handle_event(event)

    def update_elements(self, elements:list):
        for element in elements:
            element.update(self.screen)