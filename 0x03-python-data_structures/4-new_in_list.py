#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_l = my_list.copy()
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list
    new_l[idx] = element
    return new_l
