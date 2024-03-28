#!/usr/bin/python3
"""Module that finds a peak in a list of integers"""


def find_peak(list_of_integers):
    """function that search for peak in list of unsorted integers

    Args: list of integers

    Returns: peak
    """
    int_list = list_of_integers
    # if no list of int return None
    if ilist == []:
        return None
    length = len(ilist)

    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start) // 2
        if ilist[mid] > ilist[mid - 1] and ilist[mid] > ilist[mid + 1]:
            return ilist[mid]
        if ilist[mid - 1] > ilist[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return ilist[start]
