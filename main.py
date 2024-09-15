# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
import sys

def main():
    pygame.init()

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    Shot.containers =  (updatable,drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()


    while True:
        # end game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # draw black    
        screen.fill((0,0,0))
        for element in updatable:
            element.update(dt)
        for element in drawable:
            element.draw(screen)
        for asteroid in asteroids:
            if asteroid.collision(player) == True:
                sys.exit("Game over!")
        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()



    """"
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    """