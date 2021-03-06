#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size*self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            if self.__position[1] > 0:
                print('\n' * (self.__position[1] - 1))
            for i in range(self.__size):
                if self.__position[0] > 0:
                    print(' ' * self.__position[0], end='')
                print('#' * self.__size)

    def __str__(self):
        r = ""
        if self.__size == 0:
            r = r + "\n"
        else:
            if self.__position[1] > 0:
                r = r + ("\n" * (self.__position[1]))
            for i in range(self.__size):
                if self.__position[0] > 0:
                    r = r + (" " * self.__position[0])
                r = r + ("#" * self.__size) + "\n"
        return(r[:-1])
