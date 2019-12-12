#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print(len(sys.argv) - 1, "arguments.")
    elif len(sys.argv) == 2:
        print(len(sys.argv) - 1, "argument:")
    else:
        print(len(sys.argv) - 1, "arguments:")
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
