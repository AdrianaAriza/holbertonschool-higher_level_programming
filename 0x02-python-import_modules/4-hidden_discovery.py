#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    p = dir(hidden_4)
    for i in p:
        if i[:2] != '__':
            print(i)
