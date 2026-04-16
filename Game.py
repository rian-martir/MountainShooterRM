import pygame
from Const import WIN_WIDTH, WIN_HEIGHT, BG_LIST

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        self.background = pygame.image.load(BG_LIST).convert()
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        while self.running:
            # 1. Captura de Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # 2. Desenho (View)
            self.window.blit(source=self.background, dest=(0, 0))

            # 3. Atualização da Tela
            pygame.display.flip()
            self.clock.tick(60) # Mantém 60 FPS

        pygame.quit()
