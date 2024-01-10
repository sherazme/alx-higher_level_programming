#!/usr/bin/python3
""" Write into file """


def write_file(filename="", text=""):
    """ Write string into file
    Create file if it doesnt exist and overide old data
    if the file exist

    Args:
      filename (string): name of file to write into
      text (string): string to write to file

    Return: number of characters writen
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return (f.write(text))
