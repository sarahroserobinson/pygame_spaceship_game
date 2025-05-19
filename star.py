import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent the a single star."""

    def __init__(self, space_game):
        "Initialises he star and sets its starting position"
        super().__init__()
        self.screen = space_game.screen
        self.screen_rect = self.screen.get_rect()

        # Load the image of the star and set its starting position.
        self.image = pygame.image.load('images/star.bmp')
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        self.rect.top = self.rect.height
        self.rect.right = self.screen_rect.right - 20

    def blitme(self):
        self.screen.blit(self.image, self.rect)


