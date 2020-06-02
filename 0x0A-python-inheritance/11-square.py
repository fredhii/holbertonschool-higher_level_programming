#!/usr/bin/python3
""" Class Square that inherits from rectangle class """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square that inherits from rectangle class """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    """ Class Square that inherits from rectangle class """
    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
