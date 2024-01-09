#!/usr/bin/python3
""" Lookup """


def lookup(obj):
    """ returns list of available attributes and methods of object

    Args:
      obj (object): object to return it attributes and methodes
    """
    return (dir(obj))
