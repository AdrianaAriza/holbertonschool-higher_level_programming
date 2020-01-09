#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return fct(args[0], args[1])
    except Exception as i:
        sys.stderr.write("Exception:{}\n".format(i))
        return None
