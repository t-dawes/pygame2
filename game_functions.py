import sys
import pygame


def check_events():
    """Respond to keypress and mouse evewnts."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

