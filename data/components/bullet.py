import pygame

from .game_object import GameObject


class Bullet(GameObject):
    def __init__(self, win):
        self.ready = True
        GameObject.__init__(self, win, 0, 0, 0, 0, 5, 5, (0, 255, 0))


    def is_ready(self):
        return self.ready


    def get_dimensions(self):
        return (self.x, self.y, self.width, self.height)


    def draw(self):
        pygame.draw.rect(self.win, self.colors, self.get_dimensions())
