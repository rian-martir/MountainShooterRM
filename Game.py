import pygame
from Const import WIN_WIDTH, WIN_HEIGHT, ASSET_BG0, ASSET_BG1, ASSET_BG2, ASSET_BG3, ASSET_BG4, ASSET_BG5, ASSET_BG6
from player import Player, PlayerCategory, PlayerKeyboardMapping
from enemy import Enemy
from Background import Background

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Mountain Shooter")
        self.clock = pygame.time.Clock()
        self.running = True


        self.background0 = Background(ASSET_BG0, WIN_WIDTH, WIN_HEIGHT, 0)
        self.background1 = Background(ASSET_BG1, WIN_WIDTH, WIN_HEIGHT, 50)
        self.background2 = Background(ASSET_BG2, WIN_WIDTH, WIN_HEIGHT, 150)
        self.background3 = Background(ASSET_BG3, WIN_WIDTH, WIN_HEIGHT, 200)
        self.background4 = Background(ASSET_BG4, WIN_WIDTH, WIN_HEIGHT, 250)
        self.background5 = Background(ASSET_BG5, WIN_WIDTH, WIN_HEIGHT, 350)
        self.background6 = Background(ASSET_BG6, WIN_WIDTH, WIN_HEIGHT, 300)


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
            dt = self.clock.tick(160) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            self.background0.update(dt)
            self.background1.update(dt)
            self.background2.update(dt)
            self.background3.update(dt)
            self.background4.update(dt)
            self.background5.update(dt)
            self.background6.update(dt)
            self.all_sprites.update(dt)
            self.bullet_group.update(dt)
            self._handle_collisions()

            self.background1.draw(self.window)
            self.background0.draw(self.window)
            self.background3.draw(self.window)
            self.background2.draw(self.window)
            self.background4.draw(self.window)
            self.background6.draw(self.window)
            self.background5.draw(self.window)
            self.all_sprites.draw(self.window)
            self.bullet_group.draw(self.window)


            pygame.display.flip()

        pygame.quit()
