#!/usr/bin/python3
"""
A class for Rectangle module
"""


class Rectangle:
    """A class that defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """
        An instantalization of the attributes width and height.

        Args:
            width (int): Rectangle width.
            height (int): Rectangle height.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """returns the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns The area of the rectangle"""
        return (self.__width * self.__height)

    def __repr__(self):
        """Return the string reprsentation"""
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return rec
