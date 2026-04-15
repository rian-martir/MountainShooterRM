import pygame

class Background:
    def __init__(self, name, position):
        self.name = name
        self.image = pygame.image.load(f'./asset/{name}.png').convert()
        self.rect = self.image.get_rect(topleft=position)

    def draw(self, window):
        window.blit(self.image, self.rect)
