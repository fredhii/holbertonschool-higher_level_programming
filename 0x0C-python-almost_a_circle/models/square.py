#!/usr/bin/python3
""" Defines a Square class """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Class Constructor """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Defines print attribute """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        """ Getter """
        return self.width

    @size.setter
    def size(self, size):
        """ Setter """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Update square class """
        if len(args):
            i = 0
            key = ['id', 'size', 'x', 'y']
            for value in args:
                if i < 4:
                    setattr(self, key[i], value)
                    i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a square dictionary """
        return {'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y}
