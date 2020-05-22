#!/usr/bin/python3
""" ================================ """
""" Adds two integers """
""" ================================ """


def add_integer(a, b=98):
    """
    @a: Number one
    @b: Number two
    Description: If there's not second argument 98 is set
    Return: Adition from two integers
    """
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
