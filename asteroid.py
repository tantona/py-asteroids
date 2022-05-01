import math
import random
from turtle import position
import pyray as pr
from bullet import Bullet
from ship import Ship
from utils import distance
from world import SCREEN_HEIGHT, SCREEN_WIDTH, world
from game_object import GameObject


class Asteroid(GameObject):
    def __init__(self, positon: pr.Vector2, size=50) -> None:
        self.position = positon
        self.direction = random.randint(0, 360)
        self.rotation = 0
        self.rotation_speed = 0.5 * (random.randint(0, 1) * -1)
        self.speed = 1
        self.size = size

    @property
    def velocity(self):
        return pr.Vector2(math.cos(self.direction) * self.speed, -math.sin(self.direction) * self.speed)

    def check_collision(self, obj):
        if type(obj) == Bullet and distance(obj.position, self.position) <= self.size:
            if self.size == 50:
                world.score += 50
                world.add_object(Asteroid(self.position, 30))
                world.add_object(
                    Asteroid(pr.Vector2(10 + self.position.x, 30 + self.position.y), 30))

            if self.size == 30:
                world.score += 30
                world.add_object(Asteroid(self.position, 10))
                world.add_object(Asteroid(self.position, 10))
                world.add_object(
                    Asteroid(pr.Vector2(10 + self.position.x, 10 + self.position.y), 10))

            if self.size == 10:
                world.score += 10

            obj.destroy()
            self.destroy()

        if type(obj) == Ship and distance(obj.position, self.position) <= self.size + obj.hit_box_radius:
            obj.destroy()
            world.game_over = True

    def update(self):
        self.rotation += self.rotation_speed
        self.position = pr.Vector2(
            (self.position.x + self.velocity.x) % SCREEN_WIDTH, (self.position.y + self.velocity.y) % SCREEN_HEIGHT)

        for obj in world.objects:
            if obj != self:
                self.check_collision(obj)

    def draw(self):
        pr.draw_poly_lines(self.position, 5, self.size,
                           self.rotation, pr.WHITE)
