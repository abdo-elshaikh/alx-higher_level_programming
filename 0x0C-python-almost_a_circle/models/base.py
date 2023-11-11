#!/usr/bin/python3
""" models package """
import json, csv, turtle, os

class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))


    @staticmethod
    def from_json_string(json_string):
        """ from json string """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """ create """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """ load from file """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = Base.from_json_string(file.read())
                list_objs = [cls.create(**dict) for dict in list_dicts]
                return list_objs
        except FileNotFoundError:
            return []
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to file csv """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())
    
    @staticmethod
    def load_from_file_csv():
        """ load from file csv """
        filename = type.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as file:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                reader = csv.DictReader(file, fieldnames=fieldnames)
                list_dicts = [dict([key, int(value)] for key, value in dict.items())
                              for dict in reader]
                return [cls.create(**dict) for dict in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ draw """
        t = turtle.Turtle()
        t.pensize(3)
        t.shape("square")
        t.color("blue")
        t.penup()
        t.goto(-200, 200)
        t.pendown()
        for rect in list_rectangles:
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
        t.penup()
        t.goto(-200, -200)
        t.pendown()
        t.pensize(3)
        t.shape("square")
        t.color("red")
        for square in list_squares:
            t.forward(square.size)
            t.left(90)
            t.forward(square.size)
            t.left(90)
            t.forward(square.size)
            t.left(90)
            t.forward(square.size)
            t.left(90)
        turtle.exitonclick()
