class GameObject:
    destroyed = False

    def draw(self):
        pass

    def handle_input(self):
        pass

    def update(self):
        pass

    def destroy(self):
        self.destroyed = True
