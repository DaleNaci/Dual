from abc import ABC, abstractmethod


class GameObject(ABC):
    def __init__(self, win, x, y, vel_x,
                 vel_y, width, height, colors):
        self.win = win
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.width = width
        self.height = height
        self.colors = colors


    @abstractmethod
    def draw(self):
        pass
