import pygame

from .game_object import GameObject


class Bullet(GameObject):
    """A class used to represent a bullet that a player shoots

    An instance should be created when a player shoots, and destroyed
    when it either goes out of bounds or it hits a player.

    Attributes
    ----------
    ready : bool
        The state of a bullet. Determines whether an instance is
        available to be shot
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

    def __init__(self):
        self.ready = True
        GameObject.__init__(self, 0, 0, 0, 0, 5, 5, (0, 255, 0))


    def draw(self, win):
        """Draws the bullet on the screen

        Parameters
        ----------
        win : pygame.Surface
            This is the Pygame surface that is drawn on
        """
        pygame.draw.rect(win, self.colors, self.get_dimensions())


    def move(self, win): # NOTE: Is this win parameter necessary?
        """Changes the x and y values of the bullet

        This change is based on the velocity attributes. This also updates its
        state if the bullet moves out of bounds.

        Parameters
        ----------
        win : pygame.Surface
            This is the Pygame surface that is drawn on
        """
        self.x += self.vel_x
        self.y -= self.vel_y

        if not self.inbounds(win):
            self.ready = True


    def set_movement(self, x, y, vel_x, vel_y):
        """Sets the all of the movement variables

        This sets up a vector that starts at a certain point.

        Parameters
        ----------
        x : int
            This is the x coordinate for the movement to start at
        y : int
            This is the y coordinate for the movement to start at
        vel_x : int
            This is the x velocity for the movement to travel with
        vel_y : int
            This is the y velocity for the movement to travel with
        """
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y


    def is_ready(self):
        """This method provides the state of the bullet

        Returns
        -------
        ready : bool
            This determines whether the bullet is ready to be used
        """
        return self.ready


    def get_dimensions(self):
        """Returns the dimensions of the bullet"""
        return (self.x, self.y, self.width, self.height)


    def inbounds(self, win):
        """Checks whether the bullet is inbounds

        This function currently uses the x and y coordinates, so
        it's technically checking if the top left corner of the
        rectangle is inbounds.

        Parameters
        ----------
        win : Pygame.Surface
            This is the Pygame surface that is drawn on
        Returns
        -------
        bool
            True if the bullet is inbounds, False otherwise
        """
        w, h = win.get_size()
        return (0 < self.x < w) and (0 < self.y < h)
