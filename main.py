import math
import pyray as pr
from ship import Ship

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class World:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def handle_input(self):

        for obj in self.objects:
            obj.handle_input()

    def update(self):
        for obj in self.objects:
            obj.update()

    def draw(self):
        for obj in self.objects:
            obj.draw()


world = World()
world.add_object(Ship(pr.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)))


def update():
    world.update()


def handle_input():
    world.handle_input()


def draw():
    world.draw()


pr.init_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Asteroids")


def run():

    while not pr.window_should_close():
        pr.begin_drawing()
        pr.clear_background(pr.BLACK)

        handle_input()

        update()

        draw()

        pr.end_drawing()
    pr.close_window()


run()
