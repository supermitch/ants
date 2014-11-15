"""
Renderer is in charge of all drawing graphics to the screen.

The game did define the screen size, but otherwise it's all here.

"""
import math

import pygame

class Renderer():
    def __init__(self, surface, world, clock):
        self.surface = surface
        self.world = world
        self.clock = clock

    def render(self):
        self.surface.fill(self.world.bg_color)
        self.__render_ants()
        self.__render_fps()
        pygame.display.update()

    def __render_fps(self):
        pygame.font.init()
        font = pygame.font.Font(None, 36)
        text = '{:.2f}'.format(self.clock.get_fps())
        text_surface = font.render(text, True, (200, 155, 155))
        text_pos = text_surface.get_rect(centerx=self.surface.get_width()/2)
        self.surface.blit(text_surface, text_pos)

    def __render_ants(self):
        for ant in self.world.ants:
            ant_surf = pygame.Surface((ant.width, ant.height),
                                         pygame.SRCALPHA, 32)
            ant_surf.fill(ant.color)
            ant_surf = pygame.transform.rotate(ant_surf,
                math.degrees(ant.orientation))
            # Re-center our ant, after rotation
            w, h = ant_surf.get_width(), ant_surf.get_height()
            pos_x, pos_y = ant.rect.center
            top_left = (pos_x - w/2, pos_y - h/2)
            self.surface.blit(ant_surf, top_left)
    
            # Draw outline and center
            #outline = pygame.Rect(top_left[0], top_left[1], w, h)
            #pygame.draw.rect(self.surface, (0, 255, 0, 255), outline, 1) 
            #pygame.draw.circle(self.surface, (255, 0, 0, 255), ant.rect.center, 20, 1)

