#!/usr/bin/python3
def safe_print_division(a, b):
    r = 0.0
    try:
        r = a / b
    except ZeroDivisionError:
        print("Inside result: None")
        return None
    finally:
        print("Inside result: {:.1f}".format(r))
    return r
