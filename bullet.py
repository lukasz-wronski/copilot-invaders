import pygame


class Bullet:
    """Bullet class init function creating a 4x4 white rectangle at the position pointed as a param"""

    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.Surface((4, 4))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y

    """Bullet class update function moving the bullet up by three pixel per frame"""

    def update(self):
        self.rect.y -= 3
        self.screen.blit(self.image, self.rect)
