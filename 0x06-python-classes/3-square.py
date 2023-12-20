#!/usr/bin/python3
""" Square Class """


class Square:
    """ Square """

    def __init__(self, size=0):
        """ Initialize a new Square.

        Args:
             size (int): Size of the new Square.
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        self.__size = size

    def area(self):
        """ Return The area of the square """
        return (self.__size ** 2)
