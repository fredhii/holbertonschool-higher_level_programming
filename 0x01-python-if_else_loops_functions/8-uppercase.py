#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        xd = ord(str[i])
        if xd >= 97 and xd <= 123:
            xd -= 32
        print("{}".format(chr(xd)), end="")
    print()
