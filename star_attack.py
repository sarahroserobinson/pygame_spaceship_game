import pygame
import sys
from ship import Ship

class StarAttack():
    """A class to manage the game assets and functions."""
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.bg_colour = (100, 100, 100)
        self.ship = Ship(self)

        pygame.display.set_caption("Star Attack")
        
        self.running = True

    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_colour)
            self.ship.blitme()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    space_game = StarAttack()
    space_game.run_game()
        