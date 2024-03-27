#!/usr/bin/python3
"""Module that finds a peak in a list of integers"""


def find_peak(list_of_integers):
    """function that search for peak in list of unsorted integers

    Args: list of integers

    Returns: peak
    """
    int_list = list_of_integers
    # if no list of int return None
    if int_list == []:
        return None
    l= len(int_list)

    start, end = 0, l- 1
    while start < end:
        mid = start + (end - start) // 2
        if list_[mid] > int_list[mid - 1] and int_list[mid] > int_list[mid + 1]:
            return int_list[mid]
        if int_list[mid - 1] > int_list[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return int_list[start]
