#!/usr/bin/python3
def text_indentation(text):
    """ indet a text(.:?)
    """
    f = 0
    s = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if i is ":" or i is "." or i is "?":
            s = s + i + "\n\n"
            f = 1
        else:
            if f is 1 and i is " ":
                f = 0
            else:
                s = s + i
    print(s, end="")
