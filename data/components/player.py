import pygame
from itertools import count

from .game_object import GameObject


class Player(GameObject):
    """A class used to represent a player

    An instance should be created when a player shoots, and destroyed
    when it either goes out of bounds or it hits a player.

    Attributes
    ----------
    id : int
        This represents the player id. eg. Player 1 -> id=1
    health : int
        This health starts at a certain value and drops when a bullet
        hits the player
    x : int
        The x-coordinate of the game object
    y : int
        The y-coordinate of the game object
    vel_x : int
        The x-velocity of the game object
    vel_y : int
        The y-velocity of the game object
    width : int
        The width of the game object
    height : int
        The height of the game object
    colors : tuple
        A tuple of 3 values [0-255] that correspond to RGB values
    """

    _ids = count(1)
    MAX_SPEED_X = 5
    MAX_SPEED_Y = 5


    def __init__(self, x, y, colors, health):
        """
        Parameters
        ----------
        id : int
            This represents the player id. eg. Player 1 -> id=1
        health : int
            This health starts at a certain value and drops when a bullet
            hits the player
        x : int
            The x-coordinate of the game object
        y : int
            The y-coordinate of the game object
        """
        self.id = next(self._ids)
        self.health = health
        GameObject.__init__(self, x, y, 5, 5, 50, 50, colors)


    def __str__(self):
        """Converting an instance to a string provides info

        To run this method, use the built-in str() function on an
        instance.

        Returns
        -------
        s : str
            A multi-line string that reads out information about a
            player instance.
        """
        s = f"id: {self.id}\n" \
            + f"x: {self.x}\n" \
            + f"y: {self.y}\n" \
            + f"vel x: {self.velx}\n" \
            + f"vel y: {self.vely}\n" \
            + f"width: {self.width}\n" \
            + f"height: {self.height}\n" \
            + f"colors: {self.colors}\n"
        return s


    def __set_vels(self):
        """Set the velocities based on the current keys being pressed

        This looks at the WASD keys and sets the velocity variables
        accordingly. If two opposing keys are both being pressed, it
        sets the velocities to 0.
        """
        keys = pygame.key.get_pressed()
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
        """These return the limits of where a player can go on a Pygame
        surface

        The bounds are dependent on Pygame surface and the id of the
        player.

        Parameters
        ----------
        win : pygame.Surface
            This is the Pygame surface that is drawn on

        Returns
        -------
        bounds : dict
            A dictionary with four string keys {L, R, U, D} that
            represent Left, Right, Up, and Down. Each key's value
            corresponds to a coordinate line on the window that
            signifies the bound.
        """
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
        """Returns the dimensions of the player"""
        return (self.x, self.y, self.width, self.height)


    def draw(self, win):
        """Draws the bullet on the screen

        Parameters
        ----------
        win : pygame.Surface
            This is the Pygame surface that is drawn on
        """
        pygame.draw.rect(win, self.colors, self.get_dimensions())


    def move(self, win):
        """Changes the x and y values of the player

        This change is based on the velocity attributes. That are
        updated by calling the __set_vels() function. This also stops a
        player from moving out of bounds.

        Parameters
        ----------
        win : pygame.Surface
            This is the Pygame surface that is drawn on
        """
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
