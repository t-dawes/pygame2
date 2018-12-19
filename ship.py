import pygame


class Ship:
    def __init__(self, screen):
        """Initialize ship and starting position"""
        self.screen = screen

        # load images
        self.image = pygame.image.load('images/dragon.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start at bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw drg at  its current location"""
        self.screen.blit(self.image, self.rect)
