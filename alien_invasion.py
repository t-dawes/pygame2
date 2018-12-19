import sys
import pygame
from ship import Ship
from settings import Settings
import game_functions as gf

def run_game():
    # Initialize game
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make drg
    ship = Ship(screen)
    while True:
        gf.check_events()

        pygame.display.flip()
        screen.fill(ai_settings.bg_color)
        ship.blitme()


run_game()
