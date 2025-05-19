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
            self._check_events()
            self.ship.update()
            self.screen.fill(self.bg_colour)
            self.ship.blitme()
            pygame.display.flip()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.ship.moving_up = True
                    if event.key == pygame.K_DOWN:
                        self.ship.moving_down = True


if __name__ == "__main__":
    space_game = StarAttack()
    space_game.run_game()
        