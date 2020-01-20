#!/usr/bin/python3
class MyInt(int):
    """"""
    def __ne__(self, other):
        return self.real == other

    def __eq__(self, other):
        return self.real != other
