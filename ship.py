import pygame

class Ship():
    """A class representing the spaceship, its behaviours and assets."""

    def __init__(self, space_game):
        """Initialise the ship and set its starting position."""
        self.screen = space_game.screen
        self.screen_rect = space_game.screen.get_rect()

        # Load the ship image and set it's position.
        self.image = pygame.image.load('images/spaceship.bmp')
        self.image = pygame.transform.scale(self.image, (130, 130))
        self.rect = self.image.get_rect()

        # Start ship at centre left of the screen.
        self.rect.left = self.screen_rect.left

        self.x = float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)