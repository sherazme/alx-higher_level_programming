#!/usr/bin/python3
""" Append to file """


def append_write(filename="", text=""):
    """ Append text to file """
    with open(filename, mode='a', encoding='utf-8') as f:
        return (f.write(text))
