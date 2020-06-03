#!/usr/bin/python3
""" Prints a file """


def read_lines(filename="", nb_lines=0):
    """ Prints a file """
    with open(filename, encoding='utf8') as file:
        if nb_lines <= 0:
            for line in file:
                print(line, end="")
        else:
            for line in range(nb_lines):
                print(file.readline(), end="")
