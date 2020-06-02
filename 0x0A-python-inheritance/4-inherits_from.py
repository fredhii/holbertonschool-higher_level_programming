#!/usr/bin/python3
""" Check if is instance """


def inherits_from(obj, a_class):
    """ Check if is instance """
    if (type(obj) != a_class):
        return isinstance(obj, a_class)
    return False
