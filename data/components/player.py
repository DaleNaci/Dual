import pygame
from itertools import count

from .game_object import GameObject


class Player(GameObject):
    _ids = count(1)
    MAX_SPEED_X = 5
    MAX_SPEED_Y = 5


    def __init__(self, win, x, y, colors, health):
        self.id = next(self._ids)
        self.health = health
        GameObject.__init__(self, None, x, y, 5, 5, 50, 50, colors)


    def __str__(self):
        s = f"id: {self.id}\n" \
            + f"win: {self.win}\n" \
            + f"x: {self.x}\n" \
            + f"y: {self.y}\n" \
            + f"vel x: {self.velx}\n" \
            + f"vel y: {self.vely}\n" \
            + f"width: {self.width}\n" \
            + f"height: {self.height}\n" \
            + f"colors: {self.colors}\n"
        return s


    def __set_vels(self):
        keys = pygame.key.get_pressed()
        d = {}

        if self.id == 1:
            d = {
                "L": keys[pygame.K_LEFT],
                "R": keys[pygame.K_RIGHT],
                "U": keys[pygame.K_UP],
                "D": keys[pygame.K_DOWN]
            }
        elif self.id == 2:
            d = {
                "L": keys[pygame.K_a],
                "R": keys[pygame.K_d],
                "U": keys[pygame.K_w],
                "D": keys[pygame.K_s]
            }

        if d["L"] == d["R"]:
            self.velx = 0
        elif d["L"]:
            self.velx = -self.MAX_SPEED_X
        else:
            self.velx = self.MAX_SPEED_X

        if d["U"] == d["D"]:
            self.vely = 0
        elif d["D"]:
            self.vely = self.MAX_SPEED_Y
        else:
            self.vely = -self.MAX_SPEED_Y


    def __get_bounds(self, win):
        w, h = win.get_size()
        bounds = {
            "L": 0,
            "R": w - self.width
        }

        if self.id == 1:
            bounds["U"] = 0
            bounds["D"] = (h // 2) - self.height
        elif self.id == 2:
            bounds["U"] = h // 2
            bounds["D"] = h - self.height

        return bounds


    def get_dimensions(self):
        return (self.x, self.y, self.width, self.height)


    def draw(self, win):
        pygame.draw.rect(win, self.colors, self.get_dimensions())


    def move(self, win):
        self.__set_vels()

        self.x += self.velx
        self.y += self.vely

        bounds = self.__get_bounds(win)

        if self.x < bounds["L"]:
            self.x = bounds["L"]
        elif self.x > bounds["R"]:
            self.x = bounds["R"]

        if self.y < bounds["U"]:
            self.y = bounds["U"]
        elif self.y > bounds["D"]:
            self.y = bounds["D"]
