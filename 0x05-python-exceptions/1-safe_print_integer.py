#!/usr/bin/python3
def safe_print_integer(value):
    """
    Print SAFTLEY number
    :param value: number to print

    """
    try:
        print("{:d}".format(value))

    except (ValueError, TypeError):
        return (False)
