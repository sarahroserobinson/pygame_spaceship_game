import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, space_game):
        "Creates a bullet object at the ships position"
        super().__init__()
        self.screen = space_game.screen
        self.colour = (30, 30, 30)
        self.bullet_height = 10
        self.bullet_width = 10
        self.bullet_speed = 4

        self.image = pygame.image.load('images/bullet.bmp')
        self.image = pygame.transform.scale(self.image, (10, 10))

        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midright = space_game.ship.rect.midright
        self.x = float(self.rect.x)
    
    def update(self):
        """Move the bullet to the right of the screen."""
        self.x += self.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.colour, self.rect)

