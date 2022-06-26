"""import pygame"""
import pygame
import random

from enemy import Enemy
from spaceship import SpaceShip

"""function named init returning zero and not calling show window function"""


class Game:
    """Init function creating an instance of a spaceship and putting it into variable spaceship. Create an empty list of enemies"""

    def init(self):
        self.spaceship = SpaceShip(self.screen)
        self.enemies = []
        self.last_enemy_spawn_time = 0
        self.score_font = pygame.font.Font(None, 30)
        self.score = 0

    """function calling spaceship update. Spawn an enemy every second. Put it at the top of the screen at the random x position. When the enemy is out of the screen remove it from the list of enemies. Show the score at the top right corner and increment it every time an enemy is shot down."""

    def update(self):
        if pygame.time.get_ticks() - self.last_enemy_spawn_time > 1000:
            self.enemies.append(Enemy(self.screen, random.randint(0, 640), 0))
            self.last_enemy_spawn_time = pygame.time.get_ticks()
        for enemy in self.enemies:
            enemy.update()
            if enemy.rect.bottom > 480:
                self.enemies.remove(enemy)
        for bullet in self.spaceship.bullets:
            for enemy in self.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    self.enemies.remove(enemy)
                    self.spaceship.bullets.remove(bullet)
                    self.score += 1
        self.spaceship.update()
        self.screen.blit(self.spaceship.image, self.spaceship.rect)
        for enemy in self.enemies:
            self.screen.blit(enemy.image, enemy.rect)
        for bullet in self.spaceship.bullets:
            self.screen.blit(bullet.image, bullet.rect)
        self.screen.blit(self.score_font.render(
            "Score: " + str(self.score), True, (255, 255, 255)), (0, 0))

    """Constructor showing a game window with 640x480 dimensions using pygame for the game named "Space Invaders" running Game.init function at the start of the constructor and Game.update function at every frame. Make sure the framerate is 60fps using tick function. Store the screen in a field called screen. Clear the screen in every frame."""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.init()
        while True:
            self.clock.tick(60)
            self.screen.fill((0, 0, 0))
            self.update()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


if __name__ == "__main__":
    game = Game()
