#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, 'r') as file:
        i = 0
        while file.readline() != "":
            i += 1
    return i
