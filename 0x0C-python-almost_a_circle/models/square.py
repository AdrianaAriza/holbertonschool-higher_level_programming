#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        s = "[Square] " + "(" + str(self.id) + ") " + str(self.x) + "/"
        s = s + str(self.y) + " - " + str(self.size)
        return s

    def update(self, *args, **kwargs):
        arg_l = ["id", "size", "x", "y"]
        if args != None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, arg_l[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        l_att = ["id", "size", "x", "y"]
        l_val = [self.id, self.size, self.x, self.y]
        return dict(zip(l_att, l_val))
