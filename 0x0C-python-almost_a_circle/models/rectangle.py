#!/usr/bin/python3
""""""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        Base.__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.__width * self.__height

    def display(self):
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        s = "[Rectangle] " + '(' + str(self.id) + ") " + str(self.__x) + "/"
        s = s + str(self.__y) + ' - ' + str(self.__width) + "/" + str(self.__height)
        return s

    def display(self):
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        att_list = ["id", "width", "height", "x", "y"]
        if args != None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, att_list[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        my_k = ["x", "y", "width", "height", "id"]
        my_v = [self.x, self.y, self.width, self.height, self.id]
        return dict(zip(my_k, my_v))
