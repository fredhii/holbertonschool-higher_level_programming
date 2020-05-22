#!/usr/bin/python3
""" ================================ """
""" Indent text """
""" ================================ """


def text_indentation(text):
    """
    @text: String to indent
    Return: None
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    delim = ['.', '?', ':']
    aux = 0
    for i in text:
        if aux == 0:
            if i == ' ':
                continue
            else:
                print("{}".format(i), end="")
                aux = 1
        else:
            if i in delim:
                print("{}".format(i), end="\n\n")
                aux = 0
            else:
                print("{}".format(i), end="")
