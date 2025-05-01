import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player, Shot


def main():
    """main function of the asteroids game"""

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Shot.containers = (shots, updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables

    the_player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        # the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatables.update(dt)

        screen.fill(BLACK)

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        for asteroid in asteroids:
            if asteroid.check_collisions(the_player):
                sys.exit("Game Over!")
            for shot in shots:
                if asteroid.check_collisions(shot):
                    asteroid.split()
                    shot.kill()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
