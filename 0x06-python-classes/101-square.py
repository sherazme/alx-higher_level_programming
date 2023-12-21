#!/usr/bin/python3
""" Square Class """


class Square:
    # Initialisation
    """ Square """

    def __init__(self, size=0, position=(0, 0)):
        """ Initialization

        Args:
             size (int): Size Square
             position (tuple): position where to print square
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__size = size

        if not (
                isinstance(position, tuple)
                and len(position) == 2
                and all(isinstance(num, int) and num >= 0 for num in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    # Getter methods
    @property
    def size(self):
        """ Retrive square Size """
        return (self.__size)

    @property
    def position(self):
        """ retrive square Position """
        return (self.__position)

    # Setter method
    @size.setter
    def size(self, size):
        """ Set size of Square """
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        self.__size = size

    @position.setter
    def position(self, position):
        """ Set position of Square """
        if not (
                isinstance(position, tuple)
                and len(position) == 2
                and all(isinstance(num, int) and num >= 0 for num in position)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    # Methods
    def area(self):
        """ calculate area """
        return (self.__size ** 2)

    def my_print(self):
        """ Print Squar using # """
        if self.__size == 0:
            print("")
            return
        for y in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

    def __str__(self):
        """ Change print() result """
        if self.__size != 0:
            for i in range(self.__position[1]):
                print("")
        for j in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for y in range(self.__size):
                print("#", end="")
            if j != self.__size - 1:
                print()
        return ("")
