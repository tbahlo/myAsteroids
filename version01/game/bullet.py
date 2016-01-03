import pyglet
from version01.game.physicalObject import PhysicalObject
from version01.game.resources import *


class Bullet(PhysicalObject):
    """Bullets fired by the player"""

    def __init__(self, *args, **kwargs):
        super(Bullet, self).__init__(
                pyglet.image("bullet.png"), *args, **kwargs
        )+
