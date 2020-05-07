#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = 0
    person = None
    if a_dictionary:
        for key in a_dictionary:
            if a_dictionary[key] > max_score:
                max_score = a_dictionary[key]
                person = key
    return person
