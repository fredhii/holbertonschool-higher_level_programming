#!/usr/bin/python3
""" Class Square that inherits from rectangle class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square that inherits from rectangle class """
    def __init__(self, size):
        """ Define a new rectangle """
        super().__init__(size, size)
