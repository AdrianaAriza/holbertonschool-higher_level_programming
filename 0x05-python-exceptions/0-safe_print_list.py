#!/bin/usr/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    for i in my_list:
        try:
            if c < x:
                c += 1
                print("{:d}".format(i), end='')
        except ValueError:
            print('')
            return c
    print('')
    return c
