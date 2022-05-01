import math
import pyray as pr
from game_object import GameObject
from world import world, SCREEN_WIDTH, SCREEN_HEIGHT
from bullet import Bullet


class Ship(GameObject):
    position: pr.Vector2
    velocity: pr.Vector2

    def __init__(self, position: pr.Vector2) -> None:
        self.position = position
        self.rotation = 0
        self.size = 30
        self.rotational_speed = 0.075
        self.velocity = pr.Vector2(0, 0)
        self.thrust = 0.1
        self.hit_box_radius = 10

    def get_rotated_point(self, point: pr.Vector2):
        x1 = point.x
        x0 = self.origin.x
        y1 = point.y
        y0 = self.origin.y
        theta = self.rotation
        return pr.Vector2((x1-x0) * math.cos(theta)+(y1-y0) * math.sin(theta)+x0, -(x1-x0) * math.sin(theta)+(y1-y0) * math.cos(theta)+y0)

    @property
    def left_wing(self):
        offset = (self.size/2)
        return pr.Vector2(self.position.x - offset,
                          self.position.y - offset)

    @property
    def nose(self):
        offset = (self.size/2)
        return pr.Vector2(self.position.x + offset, self.position.y)

    @property
    def right_wing(self):
        offset = (self.size/2)
        return pr.Vector2(self.position.x - offset, self.position.y + offset)

    @property
    def origin(self):
        return pr.Vector2((self.nose.x + self.left_wing.x + self.right_wing.x) / 3, (self.nose.y + self.left_wing.y + self.right_wing.y) / 3)

    @property
    def thrust_vector(self):
        return pr.Vector2(math.cos(self.rotation) * self.thrust, -math.sin(self.rotation) * self.thrust)

    def update(self):

        self.position = pr.Vector2(
            (self.position.x + self.velocity.x) % SCREEN_WIDTH,
            (self.position.y + self.velocity.y) % SCREEN_HEIGHT)

    def add_thrust(self):
        self.velocity = pr.Vector2(
            self.velocity.x + self.thrust_vector.x, self.velocity.y + self.thrust_vector.y)

    def fire(self):
        world.add_object(Bullet(self.position, self.rotation))

    def handle_input(self):
        if pr.is_key_down(pr.KEY_LEFT):
            self.rotate("left")
        if pr.is_key_down(pr.KEY_RIGHT):
            self.rotate("right")
        if pr.is_key_down(pr.KEY_UP):
            self.add_thrust()

        if pr.is_key_pressed(pr.KEY_SPACE):
            self.fire()

    def draw(self):
        nose = self.get_rotated_point(self.nose)
        left_wing = self.get_rotated_point(self.left_wing)
        right_wing = self.get_rotated_point(self.right_wing)
        pr.draw_triangle(nose, left_wing, right_wing, pr.WHITE)

        pr.draw_circle(int(self.origin.x), int(self.origin.y), 3, pr.RED)

    def rotate(self, dir):
        if dir == "left":
            self.rotation += self.rotational_speed
        if dir == "right":
            self.rotation -= self.rotational_speed
