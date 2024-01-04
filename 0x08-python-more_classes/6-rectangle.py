#!/usr/bin/python3
""" Rectangle Class. """


class Rectangle:
    """ Represent a rectangle.

    Attributes:
       width: rectangle width
       height: rectangle hieght
    """

    number_of_instances = 0

    # Initiaisation
    def __init__(self, width=0, height=0):
        """ Initialize new Rectangle.

        Args:
             widht (int): new rectangle width
             height (int): new rectangle height
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

        Rectangle.number_of_instances += 1

    # width Getter and Setter
    @property
    def width(self):
        """ gets rectangle width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ Set rectangle width """
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
        """ Set rectangle height """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")
        self.__height = value

    # Other methods
    def area(self):
        """ gets rectangle area """
        return (self.__width * self.__height)

    def perimeter(self):
        """ gets rectangle perimeter
        if width or height is equal to 0 return 0
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """ Produce string representation of object """
        if self.__width == 0 or self.__height == 0:
            return ("")
        row = "#" * self.__width
        return ('\n'.join([row] * self.__height))

    def __repr__(self):
        """ Return reprsentation of rectangle """
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        """ Print messege when deleting rectangle """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
