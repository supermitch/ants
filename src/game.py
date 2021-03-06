import sys

import pygame
from pygame.locals import *

from src.collider import Collider
from src.renderer import Renderer
from src.world import World


class Game():
    def __init__(self):
        self.screen_size = (800, 800)
        self.FPS = 60
        self.fps_clock = pygame.time.Clock()

        self.world = World(self.screen_size)  # Generate the world
        self.world.generate()  # Populate world

        self.collider = Collider(self.world.objects, self.world.walls,
                                 self.screen_size)

        self.win_surf = pygame.display.set_mode(self.screen_size,
                                                RESIZABLE, 32)
        pygame.display.set_caption('Ants! 1.0')

        self.renderer = Renderer(self.win_surf, self.world, self.fps_clock)
    
    def run(self):

        frame_counter = 0
        while True:
            # Main game loop
            dt = self.fps_clock.tick(self.FPS)
            frame_counter += 1
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.terminate()
                    elif event.key == K_p:
                        self.pause_game()
                    elif event.key == K_x:
                        self.game_over()
                    elif event.key == K_LEFT:
                        print('left') 
                    elif event.key == K_RIGHT:
                        print('right')
                    elif event.key == K_SPACE:
                        print('space')
            
            self.world.update(dt)
            self.collider.update()
            self.renderer.render()

    def terminate(self):
        """ Shut 'er down. """
        pygame.quit()  # uninitialize
        sys.exit()

