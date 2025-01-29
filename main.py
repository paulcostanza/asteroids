import pygame as p
from constants import *

def main():
    p.init() # runs pygame in your program
    screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # creates the screen size
    game_is_running = True

    # changing the fps to save CPU power
    clock = p.time.Clock()
    dt = 0

    # game loop
    while game_is_running:

        # makes the window's close button work
        for event in p.event.get():
            if event.type == p.QUIT:
                return
        ######

        p.Surface.fill(screen, (0,0,0))
        p.display.flip()

        dt = clock.tick(60) / 1000


    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    

if __name__=="__main__":
    main()