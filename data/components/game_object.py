from abc import ABC, abstractmethod
import pygame


class GameObject(ABC):
    """
    A class used to represent a game object on a Pygame screen

    These objects should not be created by clients. The expectation is
    that classes will be a subclass of GameObject. This class provides
    the baseline for objects to function on a Pygame window.

    Attributes
    ----------
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

    Methods
    -------
    draw()
        Abstract method for drawing to be implemented by subclasses
    get_rect()
        Returns a Pygame Rect object with the object's attributes
    """

    def __init__(self, x, y, vel_x,
                 vel_y, width, height, colors):
        """
        Parameters
        ----------
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
            A tuple of 3 values [0-255] that correspond to RGB values.
        """
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.width = width
        self.height = height
        self.colors = colors


    @abstractmethod
    def draw(self):
        """Abstract method to draw on a Pygame surface.

        The Pygame surface needs to be provided in some way. This can
        be done through a parameter, or through a class variable, or
        some other method.
        """
        pass


    def get_rect(self):
        """Returns Pygame Rectangle with class dimensions.

        Obtaining a Pygame Rect object is used to call its methods
        """
        return pygame.Rect(self.x, self.y, self.width, self.height)
