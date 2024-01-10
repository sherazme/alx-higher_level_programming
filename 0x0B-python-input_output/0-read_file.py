#!/usr/bin/python3
""" Read File """


def read_file(filename=""):
    """ Read from file and print it content

    Args:
       filename (string): name of File  to read from
    """
    with open(filename, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
