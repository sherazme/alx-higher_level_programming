#!/usr/bin/python3
""" Prints square with the character # """


def print_square(size):
    """Prints square where size is
    the hight and width of the square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
