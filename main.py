import math
import random
import time
from time import time

import pyray as pr

from asteroid import Asteroid
from ship import Ship
from utils import get_random_positon
from world import SCREEN_HEIGHT, SCREEN_WIDTH, world


def reset():
    world.reset()
    world.add_object(Ship(pr.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)))
    world.add_object(Asteroid(get_random_positon()))
    world.add_object(Asteroid(get_random_positon()))
    world.add_object(Asteroid(get_random_positon()))


def update():
    world.update()


def handle_input():

    world.handle_input()

    if world.game_over and pr.is_key_pressed(pr.KEY_SPACE):
        reset()


def draw():
    world.draw()


def cleanup():
    world.cleanup()


pr.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Asteroids")


def run():
    pr.set_target_fps(60)
    reset()

    while not pr.window_should_close():
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        handle_input()

        update()

        draw()

        cleanup()

        pr.end_drawing()
    pr.close_window()


run()
