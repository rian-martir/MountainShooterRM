import pygame
import sys
from player import Player, PlayerCategory, PlayerKeyboardMapping

screen_width = 1280
screen_height = 720

screen_width_half = screen_width / 2
screen_height_half = screen_height / 2

screen_width_two_half = screen_width_half / 2
screen_height_two_half = screen_height_half / 2

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Mountain Shooter")

clock = pygame.time.Clock()

dt = 0

# Grupo que vai conter todos os sprites Sprite é qualquer objeto visual que se move ou interage no jogo
all_sprites = pygame.sprite.Group()

player_one_mapping = PlayerKeyboardMapping(up=pygame.K_w, down=pygame.K_s, left=pygame.K_a, right=pygame.K_d)
player_two_mapping = PlayerKeyboardMapping(up=pygame.K_UP, down=pygame.K_DOWN, left=pygame.K_LEFT, right=pygame.K_RIGHT)

# Criando o player no centro da tela, já adicionando ao grupo LEMBRAR DE MUDAR A POSIÇÃO PRO CANTO
player_one = Player(pos=(screen_width_half, screen_height_half), groups=all_sprites, category=PlayerCategory.ONE, mapping=player_one_mapping)
player_two = Player(pos=(screen_width_half, screen_height_half * 1.2), groups=all_sprites, category=PlayerCategory.TWO, mapping=player_two_mapping)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill("purple")

    # Atualiza todos os sprites (chama o update() de cada um)
    all_sprites.update(dt)

    # Desenhando todos os sprites na tela
    all_sprites.draw(screen)

    # LEMBRAR DE COMPREENDER A NECESSIDADE
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()
