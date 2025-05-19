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
        self.speed = 1.5

        # Start ship at centre left of the screen.
        self.rect.left = self.screen_rect.left

        self.y = float(self.rect.y)

        # Movement flags
        self.moving_down = False
        self.moving_up = False
    
    def update(self):
        """Update the spaceship's position based on the movement flags."""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.speed
        
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)