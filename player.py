import pygame

from enum import Enum

class PlayerCategory(Enum):
    ONE = 1
    TWO = 2

class PlayerKeyboardMapping():
   def __init__(self, up, down, left, right):
      self.up = up
      self.down = down
      self.left = left
      self.right = right

standard_mapping = PlayerKeyboardMapping(up=pygame.K_w, down=pygame.K_s, left=pygame.K_a, right=pygame.K_d)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, category=PlayerCategory.ONE, mapping=standard_mapping):
        super().__init__(groups)  # registra o player nos grupos de sprites IMAGEM

        image_path = 'asset/player-1.png'

        match category:
            case PlayerCategory.ONE:
              image_path = 'asset/player-1.png'
            case PlayerCategory.TWO:
              image_path = 'asset/player-2.png'

        self.mapping = mapping

        # Carregando a imagem e guardanddo como superfície do sprite IMAGEM
        self.image = pygame.image.load(image_path).convert_alpha()

        # Redimensionando  a imagem sr (largura x altura em pixels) foi onde deu o erro inexists
        # self.image = pygame.transform.scale(self.image, (64, 64))

        # Rect é o "retângulo" que define posição e tamanho do sprite
        self.rect = self.image.get_rect(center=pos)

        # Velocidade de movimento
        self.speed = 300

    def handle_input(self):
        keys = pygame.key.get_pressed()
        # Vetor de direção: começa zerado a cada frame
        self.direction = pygame.Vector2(0, 0)

        if keys[self.mapping.up]:
            self.direction.y = -1
        if keys[self.mapping.down]:
            self.direction.y = 1
        if keys[self.mapping.left]:
            self.direction.x = -1
        if keys[self.mapping.right]:
            self.direction.x = 1

    def move(self, dt):
        # Normaliza o vetor para movimento diagonal não ser mais rápido
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()  # ESTA INTERPRETANDO O TECLADO  E DEFININDO A DIREÇ

        surface = pygame.display.get_surface()

        [screen_width, screen_height] = pygame.Surface.get_size(surface)

        [sprite_width, sprite_height] = self.image.get_size()

        if self.direction.x > 0:
            if self.rect.x + sprite_width < screen_width:
              self.rect.x += self.direction.x * self.speed * dt

        if self.direction.x < 0:
            if self.rect.x > 0:
              self.rect.x += self.direction.x * self.speed * dt

        if self.direction.y > 0:
            if self.rect.y + sprite_height < screen_height:
              self.rect.y += self.direction.y * self.speed * dt

        if self.direction.y < 0:
            if self.rect.y > 0:
              self.rect.y += self.direction.y * self.speed * dt

    def update(self, dt):
        self.handle_input()
        self.move(dt)
