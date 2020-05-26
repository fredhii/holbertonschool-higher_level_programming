#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    """ Rectangle class """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initialize rectangle """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @classmethod
    def square(cls, size=0):
        """ Returns a new rectangle/square """
        return cls(size, size)

    @property
    def width(self):
        """ Getter """
        return self.__width

    @property
    def height(self):
        """ Getter """
        return self.__height

    @width.setter
    def width(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """ Setter """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Return rectangle area """
        return self.width * self.height

    def perimeter(self):
        """ Return rectangle perimeter """
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        """ Prints square """
        if self.width == 0 or self.height == 0:
            return ''
        rect = ''
        for col in range(self.height):
            for row in range(self.width):
                rect += str(self.print_symbol)
            if col != self.height - 1:
                rect += '\n'
        return rect

    def __repr__(self):
        """ Return rectangle size """
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        """ Deletes a rectangle """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compare two rectangles """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)
