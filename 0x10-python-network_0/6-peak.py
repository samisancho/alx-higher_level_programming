#!/usr/bin/python3
"""
    Finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):

    if list_of_integers is None:
        return None
    pivot = len(list_of_integers) - 1
    index = 0

    for i in range(pivot):
        i = index
        if list_of_integers[index] > list_of_integers[pivot]:
            pivot -= 1
        else:
            index += 1
        if index == pivot:
            return list_of_integers[pivot]
