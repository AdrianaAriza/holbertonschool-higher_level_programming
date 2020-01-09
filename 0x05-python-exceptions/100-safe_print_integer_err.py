#!/usr/bin/pyhton3
def safe_print_integer_err(value):
    import sys
    s = "Exception: Unknown format code 'd' for object of type 'str'"
    try:
        print("{:d}".format(value))
        return True
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        return False
