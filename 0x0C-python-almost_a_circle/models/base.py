#!/usr/bin/python3
""" Defines a Base class """
import json
import csv
import turtle


class Base():
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class Constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns a json string """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save information into a file """
        file = cls.__name__ + ".json"
        with open(file, 'w') as jfile:
            if list_objs is None:
                jfile.write("[]")
            else:
                dictionary = [object.to_dictionary() for object in list_objs]
                jfile.write(Base.to_json_string(dictionary))

    @staticmethod
    def from_json_string(json_string):
        """ Returns a string """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            doom = cls(7, 7)
        else:
            doom = cls(7)
        doom.update(**dictionary)
        return doom

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        file = cls.__name__ + ".json"
        try:
            with open(file, 'r') as ifile:
                string_list = Base.from_json_string(ifile.read())
                return [cls.create(**strings) for strings in string_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save information into a csv file """
        file_name = cls.__name__ + ".csv"
        with open(file_name, 'w', newline='') as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    headers = ["id", "width", "height", "x", "y"]
                else:
                    headers = ["id", "size", "x", "y"]
                new_csv = csv.DictWriter(file, fieldnames=headers)
                for object in list_objs:
                    new_csv.writerow(object.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ Load csv data """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, 'r', newline='') as file:
                if cls.__name__ == "Rectangle":
                    headers = ["id", "width", "height", "x", "y"]
                else:
                    headers = ["id", "size", "x", "y"]
                dict_list = csv.DictReader(file, fieldnames=headers)
                dict_list = [dict([key, int(value)] for key,
                                  value in f.items())
                             for f in dict_list]
                return [cls.create(**argument) for argument in dict_list]
        except IOError:
            return []

    def draw(list_rectangles, list_squares):
        """ Draw figures """
        t = turtle.Turtle()
        t.screen.bgcolor("#000000")
        t.color("#FFFFFF")
        for rectangle in list_rectangles:
            t.showturtle()
            t.up()
            if rectangle.x == 0 or rectangle.y == 0:
                t.goto(-200, 0)
            else:
                t.goto(rectangle.x * 2 - 150, rectangle.y * 2 - 180)
            t.down()
            for i in range(2):
                t.forward(rectangle.width)
                t.left(90)
                t.forward(rectangle.height)
                t.left(90)
            t.hideturtle()

        for square in list_squares:
            t.showturtle()
            t.up()
            t.goto(square.x - 50, square.y)
            t.down()
            for i in range(2):
                t.forward(square.width)
                t.left(90)
                t.forward(square.height)
                t.left(90)
            t.hideturtle()

        turtle.mainloop()
