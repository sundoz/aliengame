import pygame


class Ship:
    def __init__(self, ai_settings, screen):
        """Initalize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        self.image.set_alpha()
        self.image.set_colorkey((255, 0, 255))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)

        self.rect.bottom = self.screen_rect.bottom
        self.bottom = float(self.rect.bottom)
        self.moving_right = False
        self.moving_left = False

#        self.moving_up = False
#        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)