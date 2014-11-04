"""
Collider classes manages and resolves collisions.

"""
import itertools as it

class Collider():
    """ Detect and manage collisions. """

    def __init__(self, world_objects):
        """ Init w/ objects. """
        self.objects = world_objects

    def detect(self):
        """ Cycle through all objects and find collisions. """
        for one, two in it.combinations(self.objects, 2):
            if one.__class__.__name__ == 'Rect':
                one_rect = one
            elif hasattr(one, 'rect'):
                one_rect = one.rect
            else:
                continue
            if two.__class__.__name__ == 'Rect':
                two_rect = two
            elif hasattr(two, 'rect'):
                two_rect = two.rect
            else:
                continue

            if one_rect.colliderect(two_rect):
                try:
                    one.collide(two)
                except AttributeError:
                    # e.g. A wall cannot respond.
                    pass
                try:
                    two.collide(one)
                except AttributeError:
                    pass

