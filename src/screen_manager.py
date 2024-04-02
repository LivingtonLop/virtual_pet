import pygame

from helpers import Helpers
class ScreenManager(Helpers):
    def __init__(self, screen_width:int , screen_height:int,list_label_sprite:list, number_row_sprite_sheet:int, number_column_sprite_sheet:int):
        super().__init__(list_label_sprite, number_row_sprite_sheet, number_column_sprite_sheet)
        
        pygame.init()
        self.screen = pygame.display.set_mode((screen_height,screen_width))
        self.clock = pygame.time.Clock()
        self.text = ''
        self.rect = pygame.Rect(220, 180, 100, 36)
        self.visible = False
        self.active = False

    def update_screen(self):
        pygame.display.flip()

    def draw_elements(self, elements:list): #geo y text
        for element in elements:
            element.draw(self.screen)

    def blit_elements(self, elements:list, position): #img
        for element in elements:
            self.screen.blit(element, position)

    def handle_elements(self, elements:list, event):
        for element in elements:
            element.handle_event(event= event)

    def update_elements(self, elements:list):
        for element in elements:
            element.update(screen = self.screen)

    def draw_label(self, text:str,x:int, y:int):
        if self.visible:
            font = pygame.font.Font(None, 36)
            text_surface = font.render(text, True, (255, 255, 255))
            text_rect = text_surface.get_rect(topleft=(x, y))
            self.screen.blit(text_surface, text_rect)

    def handle_event_input(self, event)->bool:
        confirm = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    confirm = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
        return confirm
    def draw_input(self,rect):
        if self.visible:
            color = (255, 255, 255) if self.active else (200, 200, 200)
            pygame.draw.rect(self.screen, color, rect)
            font = pygame.font.Font(None, 36)
            text_surface = font.render(self.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=rect.center)
            self.screen.blit(text_surface, text_rect)
