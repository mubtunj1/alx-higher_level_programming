#!/usr/bin/python3
""" Write a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    size = len(list_of_integers)
    middle = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        middle = middle // 2
        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if middle // 2 == 0:
                middle = 2
            mid = mid + middle // 2
        elif middle > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if middle // 2 == 0:
                middle = 2
            mid = mid - middle // 2
        else:
            return list_of_integers[mid]
