#!/usr/bin/python3
""" Class that inherit from list """


class MyList(list):
    """ Class that inherit from list """
    def print_sorted(self):
        """ Prints sorted list """
        print(sorted(self))
