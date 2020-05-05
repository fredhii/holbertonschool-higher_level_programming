#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_l = my_list.copy()
    if idx < 0:
        return new_l
    if idx > len(my_list):
        return new_l
    new_l[idx] = element
    return new_l
