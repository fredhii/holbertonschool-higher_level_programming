#!/usr/bin/python3
def multiple_returns(sentence):
    x = None
    size = len(sentence)
    if size > 0:
        x = sentence[0]
    return size, x
