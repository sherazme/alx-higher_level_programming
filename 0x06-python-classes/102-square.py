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

    def __eq__(self, other):
        """Compare two Square objects for equality.

        Args:
          other (Square): The other Square object to compare to.

        Returns:
          bool: True if the sizes of the two Square objects are equal,
                False otherwise.
          NotImplemented: If the comparison is not applicable with
                          the given object.
        """
        if isinstance(other, Square):
            return (self.area() == other.area())
        return NotImplemented

    def __ne__(self, other):
        """Compare two Square objects for not equal.

        Args:
          other (Square): The other Square object to compare to.

        Returns:
          bool: True if the sizes of the two Square objects are not equal,
                False otherwise.
          NotImplemented: If the comparison is not applicable with
                          the given object.
        """
        if isinstance(other, Square):
            return (self.area() != other.area())
        return NotImplemented

    def __lt__(self, other):
        """Compare two Square objects for less than.

        Args:
           other (Square): The other Square object to compare to.

        Returns:
           bool: True if the size of the current Square is less than the other
                 Square, False otherwise.
           NotImplemented: If the comparison is not applicable with
                           the given object.
        """
        if isinstance(other, Square):
            return (self.area() < other.area())
        return NotImplemented

    def __le__(self, other):
        """Compare two Square objects for less than or equal to.

        Args:
           other (Square): The other Square object to compare to.

        Returns:
           bool: True if the size of the current Square is less than or equal
                 to the other Square, False otherwise.
           NotImplemented: If the comparison is not applicable with
                           the given object.
        """
        if isinstance(other, Square):
            return (self.area() <= other.area())
        return NotImplemented

    def __gt__(self, other):
        """Compare two Square objects for greater than.

         Args:
           other (Square): The other Square object to compare to.

         Returns:
           bool: True if the size of the current Square is greater than the
                 other Square, False otherwise.
           NotImplemented: If the comparison is not applicable with
                           the given object.
        """
        if isinstance(other, Square):
            return (self.area() > other.area())
        return NotImplemented

    def __ge__(self, other):
        """Compare two Square objects for greater than or equal to.

         Args:
           other (Square): The other Square object to compare to.

         Returns:
           bool: True if the size of the current Square is greater than or
                 equal to the other Square, False otherwise.
           NotImplemented: If the comparison is not applicable with
                           the given object.
        """
        if isinstance(other, Square):
            return (self.area() >= other.area())
        return NotImplemented
