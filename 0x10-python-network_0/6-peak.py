#!/usr/bin/python3
def find_peak(list_of_integers):
    """"""
    if list_of_integers:
        max = list_of_integers[0]
        for integer in list_of_integers:
            if integer > max:
                max = integer
        return max
    else:
        return None
