
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_wigth, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_game()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
