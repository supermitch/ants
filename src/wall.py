class Wall():
    """ A wall object is just a wrapper for a Rect. """
    def __init__(self, rect):
        self.mass = float('inf')  # Infinity!
        self.rect = rect

