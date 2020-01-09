#!/usr/bin/python3
class Square:
    def __init__(self, size=0, value=(0, 0)):
        self.__size = size
        self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, size=0, value=(0, 0)):
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

        def area(self):
            return self.__size*self.__size

    def my_print(self):
        if self.__size == 0:
            print ("")
        else:
            if self.position[1] > 0:
                print ("" * self.__position[0])
            for i in range(self.__size):
                print (' ' * self.__position[0], end='')
                print ('#' * self.__size)
