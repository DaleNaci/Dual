import pygame

from .game_object import GameObject


class Player(GameObject):
    def __init__(self, win, x, y, colors, health):
        self.health = health
        GameObject.__init__(self, win, x, y, 5, 5, 50, 50, colors)


    def get_dimensions(self):
        return (self.x, self.y, self.width, self.height)


    def draw(self):
        pygame.draw.rect(self.win, self.colors, self.get_dimensions())
