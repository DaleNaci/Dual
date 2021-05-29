from .game_object import GameObject


class Bullet(GameObject):
    def __init__(self):
        self.ready = True
        GameObject.__init__(self, 0, 0, 0, 0, 5, 5, (0, 255, 0))


    def is_ready(self):
        return self.ready


    def draw(self):
        pass
