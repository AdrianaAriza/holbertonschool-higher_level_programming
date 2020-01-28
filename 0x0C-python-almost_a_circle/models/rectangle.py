#!/usr/bin/python3
"""
models
"""


from models.base import Base


class Rectangle(Base):
    """
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init
        """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        height
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        x
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        y
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        area
        """
        return self.__width * self.__height

    def display(self):
        """
        display
        """
        for i in range(self.__height):
            print("#" * self.__width)

    def __str__(self):
        """
        str
        """
        s = "[Rectangle] " + '(' + str(self.id) + ") " + str(self.__x) + "/"
        s = s + str(self.__y) + ' - ' + str(self.__width) + "/"
        s = s + str(self.__height)
        return s

    def display(self):
        """
        display
        """
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """
        update
        """
        att_list = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, att_list[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """
        to_dictionary
        """
        my_k = ["x", "y", "width", "height", "id"]
        my_v = [self.x, self.y, self.width, self.height, self.id]
        return dict(zip(my_k, my_v))
