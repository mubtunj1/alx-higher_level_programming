#!/usr/bin/python3
"""Finds the peak in a list of unsorted integers"""
def find_peak(list_of_integers):
    """Finds the peak in a list of unsorted integers"""
    if len(list_of_integers) == 0:
        return None
    return find_peak_helper(list_of_integers, 0, len(list_of_integers) - 1)
    