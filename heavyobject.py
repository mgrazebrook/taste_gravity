import pygame

g = 0.02

class HeavyObject:
    def __init__(self, screen, imageName, position = (0, 0),
                 speed = (2.0, 0.0), mass = 1.0, gravity = g):
        self._image = pygame.image.load('ball.gif')
        self._ballrect = self._image.get_rect()
        self._x, self._y = position
        self._dx, self._dy = speed
        self._gravity = gravity
        self._screen = screen
        self._bounciness = 0.90
        self._mass = mass
        r = screen.get_bounding_rect()
        self._maxx = float(r.right)
        self._maxy = (r.bottom)


    def __str__(self):
        fmt = 'at ({x},{y}) moving ({dx},{dy}); {mass} kg, g={g}'
        args = {
            'x': self._x,
            'y': self._y,
            'dx': self._dx,
            'dy': self._dy,
            'mass': self._mass,
            'g': self._gravity,
        }
        return fmt.format(**args)
        


    def move(self):
        self._x = self._x + self._dx
        self._y = self._y + self._dy
        speed = [ self._x - self._ballrect.left, self._y - self._ballrect.top]

        self._ballrect.topleft = (self._x, self._y)

        self._screen.blit( self._image, self._ballrect )

        self._dy += self._gravity
        if (self._ballrect.left  <= 0 and self._dx < 0.0 or
            self._ballrect.right >= self._maxx and self._dx > 0.0 ):
            self._dx = -self._dx * self._bounciness

        if (self._ballrect.top < 0 and self._dy < 0.0
            or self._ballrect.bottom > self._maxy and self._dy > 0.0):
            self._dy = -self._dy * self._bounciness

    def rect(self):
        return self._ballrect


    def speed(self, s):
        self._dx, self._dy = s


if __name__ == "__main__":
    # Do some sort of test for this module
    pass
