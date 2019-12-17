#!/usr/bin/python
def new_in_list(my_list, idx, element):
    a = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return (a if idx < 0 else my_list)
    a[idx] = element
    return a
