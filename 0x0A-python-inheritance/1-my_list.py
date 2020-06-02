#!/usr/bin/python3
""" Class that inherit from list """


class MyList(list):

    def print_sorted(self):
        print(sorted(self))
