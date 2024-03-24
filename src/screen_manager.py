import pygame

class ScreenManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()

    def update_screen(self):
        pygame.display.flip()

    def draw_elements(self, elements): #geo y text
        for element in elements:
            element.draw(self.screen)

    def blit_elements(self, elements): #img
        for element in elements:
            element.blit(self.screen)