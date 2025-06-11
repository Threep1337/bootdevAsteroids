import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots,updatable, drawable)

    asteroidField = AsteroidField()
    player = Player(SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2)
    
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for item in updatable:
            item.update(dt)


        for item in asteroids:
            if (player.check_collission(item)):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.check_collission(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
