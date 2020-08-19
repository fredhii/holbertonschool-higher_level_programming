#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Return a peak """
    if list_of_integers:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
