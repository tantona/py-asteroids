import math
import random
import time
from time import time

import pyray as pr

from world import SCREEN_HEIGHT, SCREEN_WIDTH


def get_random_positon():
    system_random = random.SystemRandom(time())
    return pr.Vector2(system_random.randint(0, SCREEN_WIDTH), system_random.randint(0, SCREEN_HEIGHT))


def distance(p1, p2):
    return math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))
