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

    def __str__(self):
        """
        Returns the visible structure of the area.

       '#' are symbols used to represent the building blocks.
       """

        if self.__width == 0 or self.__height == 0:
            return ("")
        rec = []

        for i in range(self.__height):
            accum = "#" * self.__width
            rec.append(accum)
            if i != (self.__height - 1):
                rec.append("\n")

        return ("".join(rec))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
