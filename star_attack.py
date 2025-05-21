import pygame
import sys
from ship import Ship
from star import Star
from bullet import Bullet
from random import randint

class StarAttack():
    """A class to manage the game assets and functions."""
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_height = self.screen.get_height()
        self.screen_width = self.screen.get_width()
        self.bg_colour = (100, 100, 100)
        self.ship = Ship(self)
        self.stars = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self._create_galaxy()

        pygame.display.set_caption("Star Attack")
        
        self.running = True


    def run_game(self):
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self._update_bullets()
            pygame.display.flip()
            self.clock.tick(60)
    
    def _create_star(self, x_position, y_position):
        new_star = Star(self)
        new_star.x = x_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _create_galaxy(self):
    # Continue adding stars to the right hand side of the screen.
        star = Star(self)
        star_width, star_height = star.rect.size

        current_y = star_height
        while current_y < (self.screen_height - 2 * star_height):
            current_x = self.screen_width - 2 * star_width
            while current_x > 15 * star_width:
                self._create_star(current_x, current_y)
                random_position = randint(1, 3)
                current_x -= random_position * star_width
            current_y += 2 * star_height


    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._shoot_bullet()
        elif event.key == pygame.K_q:
            sys.exit() 

    def _shoot_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        bullets_allowed = 5
        if len(self.bullets) < bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        """Update position of bullets and delete shot bullets."""
        self.bullets.update()
        # Delete bullets that have been shot and gone past the screen.
        for bullet in self.bullets.copy():
            if bullet.rect.right <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        "Update images on the screen and flip to the new screen."
        self.screen.fill(self.bg_colour)
        self.ship.blitme()
        self.stars.draw(self.screen)
        self.bullets.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    space_game = StarAttack()
    space_game.run_game()
        