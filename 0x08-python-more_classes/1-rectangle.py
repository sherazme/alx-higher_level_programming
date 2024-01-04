#!/usr/bin/python3
""" Rectangle Class """


class Rectangle:
    """ Represent a rectangle

    Attributes:
       width: width of rectangle
       height: hieght of traingle
    """

    def __init__(self, width=0, height=0):
        """ Initializing

        Args:
             widht (int): width of new rectangle
             height (int): height of new rectangle
        """
        if isinstance(width, int):
            if width < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        self.__width = width

        if isinstance(height, int):
            if height < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
        self.__height = height

    # width Getter and Setter
    @property
    def width(self):
        """ gets rectangle width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Sets rectangle width """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
        self.__width = value

    # height Getter and Setter
    @property
    def height(self):
        """ gets rectangle height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ Sets rectangle height """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
        self.__height = value
