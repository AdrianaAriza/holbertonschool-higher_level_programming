#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    x = len(sys.argv)
    if x != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    op = sys.argv[2]
    if op != "+" and op != "-" and op != "*" and op != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{:d} {} {:d} = {:d}".format(a, op, b, add(a, b) if op is "+"
                                       else sub(a, b) if op is "-"
                                       else mul(a, b) if op is "*"
                                       else div(a, b)))
    # else sub(a, b) if op == "-"
    # else mul(a, b) if op == "*"
    # else div(a, b) if op == "/"))
    sys.exit(0)
