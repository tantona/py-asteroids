import pyray as pr
import asteroid
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class World:
    def __init__(self):
        self.reset()

    def reset(self):
        self.score = 0
        self.game_over = False
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
        pr.draw_fps(0, 0)
        pr.draw_text("Score: {0}".format(self.score), 10, 10, 20, pr.WHITE)

        if self.game_over:
            msg = "GAME OVER"
            msg2 = "Press spacebar to reset"
            offset = pr.measure_text(msg, 20) / 2
            offset2 = pr.measure_text(msg2, 20) / 2
            pr.draw_text(msg,
                         int((SCREEN_WIDTH/2) - offset), int(SCREEN_HEIGHT/2), 20, pr.RED)
            pr.draw_text(msg2,
                         int((SCREEN_WIDTH/2) - offset2), int(SCREEN_HEIGHT/2) + 30, 20, pr.RED)

        for obj in self.objects:
            obj.draw()

    def cleanup(self):
        self.objects = list(
            filter(lambda obj: obj.destroyed is False, self.objects))


world = World()
