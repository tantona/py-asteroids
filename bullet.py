import math
import pyray as pr
from world import SCREEN_WIDTH, SCREEN_HEIGHT
from game_object import GameObject


class Bullet(GameObject):
    def __init__(self, positon: pr.Vector2, rotation) -> None:
        self.position = positon
        self.rotation = rotation
        self.speed = 10

    @property
    def velocity(self):
        return pr.Vector2(math.cos(self.rotation) * self.speed, -math.sin(self.rotation) * self.speed)

    def update(self):
        self.position = pr.Vector2(
            self.velocity.x + self.position.x, self.velocity.y + self.position.y)

        if self.is_out_of_bounds():
            self.destroy()

    def is_out_of_bounds(self):
        return self.position.x > SCREEN_WIDTH or self.position.x < 0 or self.position.y > SCREEN_HEIGHT or self.position.y < 0

    def draw(self):
        pr.draw_circle(int(self.position.x), int(self.position.y), 3, pr.WHITE)
