import random

import pygame

from bullet import Bullet


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups, target, bullet_group):
        super().__init__(groups)
        self.target = target
        self.bullet_group = bullet_group
        self._base_image = pygame.image.load("assets/enemy-1.png").convert_alpha()
        self.image = self._base_image
        self.rect = self.image.get_rect(center=pos)
        self.speed = 180
        self.direction = pygame.Vector2(0, 0)
        self._wander_timer = 0.0
        self._wander_interval = 1.2
        self._bullet_speed = 420
        self._shoot_timer = 0.0
        self._shoot_cooldown = random.uniform(0.35, 1.4)

    def _pick_random_direction(self):
        v = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        if v.length_squared() < 1e-6:
            return self._pick_random_direction()
        return v.normalize()

    def _face_target(self):
        dx = self.target.rect.centerx - self.rect.centerx
        flip_x = dx > 0
        center = self.rect.center
        self.image = pygame.transform.flip(self._base_image, flip_x, False)
        self.rect = self.image.get_rect(center=center)

    def _wander(self, dt):
        self._wander_timer += dt
        if self._wander_timer >= self._wander_interval:
            self._wander_timer = 0.0
            self.direction = self._pick_random_direction()

    def move(self, dt):
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()

        surface = pygame.display.get_surface()
        screen_width, screen_height = pygame.Surface.get_size(surface)
        sprite_width, sprite_height = self.image.get_size()

        if self.direction.x > 0 and self.rect.x + sprite_width < screen_width:
            self.rect.x += self.direction.x * self.speed * dt
        if self.direction.x < 0 and self.rect.x > 0:
            self.rect.x += self.direction.x * self.speed * dt
        if self.direction.y > 0 and self.rect.y + sprite_height < screen_height:
            self.rect.y += self.direction.y * self.speed * dt
        if self.direction.y < 0 and self.rect.y > 0:
            self.rect.y += self.direction.y * self.speed * dt

    def _try_shoot(self, dt):
        self._shoot_timer += dt
        if self._shoot_timer < self._shoot_cooldown:
            return
        self._shoot_timer = 0.0
        self._shoot_cooldown = random.uniform(0.35, 1.4)
        to_target = pygame.Vector2(self.target.rect.center) - pygame.Vector2(self.rect.center)
        if to_target.length_squared() < 4:
            return
        velocity = to_target.normalize() * self._bullet_speed
        Bullet(self.rect.center, velocity, self.bullet_group)

    def update(self, dt):
        self._wander(dt)
        self.move(dt)
        self._face_target()
        self._try_shoot(dt)
