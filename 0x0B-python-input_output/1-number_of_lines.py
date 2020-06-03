#!/usr/bin/python3
""" Open a file from UTF-8 """


def number_of_lines(filename=""):
    """ Prints a file """
    with open(filename, encoding='utf8') as file:
        i = 0
        for line in file:
            i += 1
        return i
