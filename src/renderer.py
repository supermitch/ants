"""
Renderer is in charge of all drawing graphics to the screen.

The game did define the screen size, but otherwise it's all here.

"""
import math

import pygame

class Renderer():
    def __init__(self, surface, world):
        self.surface = surface
        self.world = world

    def render(self):
        self.surface.fill(self.world.bg_color)
        self.__render_ants()
        pygame.display.update()

    def __render_ants(self):
        for ant in self.world.ants:
            color = {
                'black': (0, 0, 0, 128),
                'red': (255, 0, 0, 128),
            }[ant.breed]
            ant_surface = pygame.Surface((ant.width, ant.height),
                                         pygame.SRCALPHA, 32)
            ant_surface.fill(color)
            ant_surface = pygame.transform.rotate(ant_surface,
                math.degrees(ant.orientation))
            # Re-center our ant, after rotation
            w, h = ant_surface.get_width(), ant_surface.get_height()
            top_left = (ant.pos[0] - w/2, ant.pos[1] - h/2)

            self.surface.blit(ant_surface, top_left) 
    
            # Draw outline and center
            #outline = pygame.Rect(top_left[0], top_left[1], w, h)
            #pygame.draw.rect(self.surface, (0, 255, 0, 255), outline, 1) 
            #pygame.draw.circle(self.surface, (255, 0, 0, 255), ant.pos, 20, 1)


