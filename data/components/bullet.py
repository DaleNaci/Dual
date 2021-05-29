import pygame

from .game_object import GameObject


class Bullet(GameObject):
    def __init__(self, win):
        self.ready = True
        GameObject.__init__(self, win, 0, 0, 0, 0, 5, 5, (0, 255, 0))


    def draw(self):
        pygame.draw.rect(self.win, self.colors, self.get_dimensions())


    def move(self):
        self.x += self.vel_x
        self.y -= self.vel_y

        if not self.inbounds():
            self.ready = True


    def set_movement(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y


    def is_ready(self):
        return self.ready


    def get_dimensions(self):
        return (self.x, self.y, self.width, self.height)


    def inbounds(self):
        w, h = self.win.get_size()
        return (0 < self.x < w) and (0 < self.y < h)
