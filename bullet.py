class Bullet:
    def __init__(self):
        self.ready = True
        self.x = 0
        self.y = 0
        self.vel_x = 0
        self.vel_y = 0


    def is_ready(self):
        return self.ready
