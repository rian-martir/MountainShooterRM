import pygame
from Const import WIN_WIDTH, WIN_HEIGHT, ASSET_BG
from player import Player, PlayerCategory, PlayerKeyboardMapping
from enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Mountain Shooter")
        self.clock = pygame.time.Clock()
        self.running = True


        self.background = pygame.image.load(ASSET_BG).convert()
        self.background = pygame.transform.scale(self.background, (WIN_WIDTH, WIN_HEIGHT))


        self.all_sprites   = pygame.sprite.Group()
        self.enemy_group   = pygame.sprite.Group()
        self.bullet_group  = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()


        self.player = Player(
            pos=(WIN_WIDTH // 4, WIN_HEIGHT // 2),
            groups=self.all_sprites,
            category=PlayerCategory.ONE
        )


        Enemy(
            pos=(WIN_WIDTH - 100, WIN_HEIGHT // 2),
            groups=[self.all_sprites, self.enemy_group],
            target=self.player,
            bullet_group=self.bullet_group
        )


        self.bullet_group.add()

    def _handle_collisions(self):
        hits = pygame.sprite.spritecollide(self.player, self.bullet_group, dokill=True)
        if hits:
            print("Jogador foi atingido!")
    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False


            self.all_sprites.update(dt)
            self.bullet_group.update(dt)
            self._handle_collisions()


            self.window.blit(self.background, (0, 0))
            self.all_sprites.draw(self.window)          
            self.bullet_group.draw(self.window)


            pygame.display.flip()

        pygame.quit()
