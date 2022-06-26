"""import pygame"""
import pygame

from bullet import Bullet


"""class containing two functions, init and update doing nothing """


class SpaceShip:

    """create constructor placing the ship from ship.png. Use pygame.transform to set the image size to 50x50. Save the rect to a separate field in this class. Position the rect on the center and put it 20px above the bottom of the screen."""

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("ship.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.bottom = self.screen.get_rect().bottom - 20
        self.spacebar_was_pressed = False
        self.bullets = []

    """update function display the ship on the screen, move it left, up, down, right by one pixel per frame when user presses the cursor keys. When the spacebar is clicked create a new bullet object and add it to the list of bullets. When the bullet is out of the screen remove it from the list of bullets. Shoot bullets only when spacebar was not pressed in previous frame."""

    def update(self):
        self.screen.blit(self.image, self.rect)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x -= 1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x += 1
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.rect.y -= 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.rect.y += 1
        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.spacebar_was_pressed:
            self.bullets.append(
                Bullet(self.screen, self.rect.centerx, self.rect.top))
        self.spacebar_was_pressed = pygame.key.get_pressed()[pygame.K_SPACE]
        for bullet in self.bullets:
            bullet.update()
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
