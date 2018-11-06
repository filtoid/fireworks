import pygame, sys
from pygame.locals import *
from firework import Firework
import time

# set up pygame
pygame.init()


if __name__ == "__main__":
    # set up the window
    screen = pygame.display.set_mode((500, 400), 0, 32)
    pygame.display.set_caption('Fireworks Display')
    firework = Firework(100)

    # run the game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))    
        
        # Update assets and draw
        firework.update()
        firework.draw(screen)

        pygame.display.flip()
        
        time.sleep(0.1)
