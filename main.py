import sys
import pygame

from settings import Settings
from ship import Ship


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_wigth, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    while True:

        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
