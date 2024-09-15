from asteroid import *
from constants import *

class Shot(Asteroid):
    containers = ()
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    

