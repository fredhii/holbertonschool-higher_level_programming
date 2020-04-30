#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    length = len(argv) - 1
    sum = 0
    for i in range(0, length):
        sum += int(argv[i])
    print("{}".format(sum))
