#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, 'r', encoding='utf-8') as file:
        if nb_lines <= 0:
            print("{}".format(file.read()), end="")
        else:
            s = file.readline()
            i = 0
            while i < nb_lines and s != "":
                print("{}".format(s), end="")
                s = file.readline()
                i += 1
