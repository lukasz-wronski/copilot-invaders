import pygame


class Enemy:

    """Constructor creating a sprite of an enemy using enemy.png file. Set it's size to 35x35. Position it at x and y coordinates provided as constructor params."""

    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("enemy.png")
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    """Update function moving the enemy down by one pixel per frame."""

    def update(self):
        self.rect.y += 1
        self.screen.blit(self.image, self.rect)
