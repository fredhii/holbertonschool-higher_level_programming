#!/usr/bin/python3
""" Defines a Rectangle class """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Class Constructor """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ Getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ Getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Returns rectangle area """
        return self.__width * self.height

    def display(self):
        """ Prints rectangle """
        for y in range(self.y):
            print()
        for height in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for width in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        """ Defines print attribute """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x,
                                                       self.y,
                                                       self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """ Update rectangle class """
        if len(args):
            i = 0
            key = ['id', 'width', 'height', 'x', 'y']
            for value in args:
                if i < 5:
                    setattr(self, key[i], value)
                    i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns a rectangle dictionary """
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}
