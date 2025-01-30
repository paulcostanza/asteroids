import pygame as p
from constants import *
from asteroid import Asteroid
from asteroidfield import *
from shoot import Shoot
from player import Player

def main():
    p.init() # runs pygame in your program
    screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # creates the screen size
    game_is_running = True

    # changing the fps to save CPU power
    clock = p.time.Clock()
    dt = 0

    # groups - player
    updateable = p.sprite.Group()
    drawable = p.sprite.Group()
    Player.containers = (updateable, drawable)

    # our player
    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # groups - asteroids
    asteroids = p.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)

    asteroid_field = AsteroidField()

    # groups - shots
    shots = p.sprite.Group()
    Shoot.containers = (shots, updateable, drawable)

    # game loop
    while game_is_running:

        # makes the window's close button work
        for event in p.event.get():
            if event.type == p.QUIT:
                return
        # # # # # # # # # # # # # # # # # # # 

        p.Surface.fill(screen, (0,0,0))

        # reads user's input
        updateable.update(dt)

        # Ends game if collision occurs between asteroid and player
        for asteroid in asteroids:
            if asteroid.collision_detection(player_1):
                raise SystemExit("G A M E O V E R")

            for shot in shots:
                if asteroid.collision_detection(shot):
                    shot.kill()
                    asteroid.split()

        for obj in drawable:
            obj.draw(screen)
        p.display.flip()

        dt = clock.tick(60) / 1000


    # TESTING
    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")

    

if __name__=="__main__":
    main()