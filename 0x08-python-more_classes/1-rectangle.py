#!/usr/bin/python3
"""A class that defines a rectangle"""

class Rectangle:
    """
    Rectangle that defines a rectangle by:
    Private instance attribute: width (int)
    Private instance attribute: height (int)
    Instantiation with optional width and height
    """
    __width = None
    __height = None

    def __init__(self, width=0, height=0):
        """
        Initializes private attribute width and height
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        width setter
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        height setter
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
