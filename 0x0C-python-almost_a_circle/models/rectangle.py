#!/usr/bin/python3
""" models package """
from models.base import Base


class Rectangle(Base):
    """ Reqtangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
    
    @property
    def width(self):
        """ Getter """
        return self.__width
    
    @width.setter
    def width(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def height(self):
        """ Getter """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
    
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def x(self):
        """ Getter """
        return self.__x
    
    @x.setter
    def x(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    @property
    def y(self):
        """ Getter """
        return self.__y
    
    @y.setter
    def y(self, value):
        """ Setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Area """
        return self.__width * self.__height
    
    def display(self):
        """ Display """
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ String representation """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def update(self, *args, **kwargs):
        """ Update """
        if args and len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.__width = arg
                if i == 2:
                    self.__height = arg
                if i == 3:
                    self.__x = arg
                if i == 4:
                    self.__y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
            return self
    
    def to_dictionary(self):
        """ Dictionary representation """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
        }