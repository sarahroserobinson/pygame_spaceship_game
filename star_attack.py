import pygame
import sys

class StarAttack():

    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        pygame.display.set_caption("Star Attack")
        
        self.running = True

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == "__main__":
    space_game = StarAttack()
    space_game.run_game()
        