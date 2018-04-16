import sys
import pygame
from ship import Ship
from settings import Settings


def run_game():
    # Initialize game
    pygame.init()
    ai_settings = Settings()
    print(ai_settings.screen_height)
    print(ai_settings.screen_width)
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make drg
    ship = Ship(screen)

    bg_color = (230, 230, 230)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()
        screen.fill(ai_settings.bg_color)
        ship.blitme()


run_game()
