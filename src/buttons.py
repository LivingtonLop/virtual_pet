import pygame

class Button:
    def __init__(self, x, y, width, height, color=None, image_normal=None, image_pressed=None, on_click=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.image_normal = image_normal
        self.image_pressed = image_pressed
        self.on_click = on_click
        self.is_pressed = False 
        
    def draw(self, screen):
        if self.color:
            pygame.draw.rect(screen, self.color, self.rect)
        elif self.image_normal:
            if self.is_pressed and self.image_pressed:
                screen.blit(self.image_pressed, self.rect.topleft)
            else:
                screen.blit(self.image_normal, self.rect.topleft)

    def set_pressed(self, is_pressed):
        self.is_pressed = is_pressed

    def update(self, screen):
        self.draw(screen)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.is_pressed = True
                if self.on_click:
                    self.on_click()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.is_pressed = False
