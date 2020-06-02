#!/usr/bin/python3
""" Class MyInit that inherits from Int """


class MyInt(int):

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value != other

    def __ne__(self, other):
        return self.value == other
