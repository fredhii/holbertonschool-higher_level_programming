#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda lis: list(map(lambda item: item ** 2, lis)), matrix))
