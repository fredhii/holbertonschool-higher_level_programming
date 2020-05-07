#!/usr/bin/python3
def uniq_add(my_list=[]):
    clean_list = list(set(my_list))
    sum = 0
    for i in clean_list:
        sum += i
    return sum
