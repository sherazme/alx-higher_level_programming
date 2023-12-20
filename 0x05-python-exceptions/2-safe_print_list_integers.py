#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x elements of a list and only integers.

    :param my_list: List to print.
    :param x: Number of elements to print.
    :return: Number of elements printed.
    """
    num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1

        except (ValueError, TypeError):
            continue

    print("")
    return (num)
