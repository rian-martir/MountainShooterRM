import pygame

class Background:
    def __init__(self, path, width, height, scroll_speed=100):
        self.path = path
        self.image = pygame.image.load(path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()

        self.width = self.image.get_width()
        self.scroll_speed = scroll_speed

        # This 'offset' acts exactly like a Texture U-Coordinate
        self.u_offset = 0

    def update(self, dt):
        # Increment the "texture coordinate"
        self.u_offset += self.scroll_speed * dt

        # Modulo the offset by the width to keep it seamless
        # This is the software version of GL_REPEAT
        self.u_offset %= self.width

    def draw(self, window):
        # Calculate the split point (the 'frame' jump)
        # We draw the remainder of the image, then the start of the image
        window.blit(self.image, (-self.u_offset, 0))
        window.blit(self.image, (self.width - self.u_offset, 0))
