import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, velocity: pygame.Vector2, groups):
        super().__init__(groups)
        self.velocity = velocity
        surf = pygame.Surface((10, 10), pygame.SRCALPHA)
        pygame.draw.circle(surf, (255, 90, 40), (5, 5), 5)
        self.image = surf
        self.rect = self.image.get_rect(center=pos)

    def update(self, dt):
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt

        surface = pygame.display.get_surface()
        w, h = pygame.Surface.get_size(surface)
        if self.rect.right < 0 or self.rect.left > w or self.rect.bottom < 0 or self.rect.top > h:
            self.kill()
