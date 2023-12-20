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

    # Getter method
    @property
    def size(self):
        """ Retrive the Size of the Square """
        return (self.__size)

    # Setter method
    @size.setter
    def size(self, size):
        """ Set the size of a Square """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

        self.__size = size
