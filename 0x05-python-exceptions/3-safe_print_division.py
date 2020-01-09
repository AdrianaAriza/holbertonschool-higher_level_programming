#!/usr/bin/python3
def safe_print_division(a, b):
    r = 0.0
    f = 0
    try:
        r = a / b
    except ZeroDivisionError:
        f = 1
    finally:
        if f is 0:
            print("Inside result: {:.1f}".format(r))
            return r
        else:
            print("Inside result: None")
            return None
