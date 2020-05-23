#!/usr/bin/python3
""" Multiply two matrix  """
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    @m_a: Matrix one
    @m_b: Matrix two
    Return: New matrix wit multiplied data
    """
    return np.matmul(m_a, m_b)
