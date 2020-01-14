#!/usr/bin/python3
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ multiplies two matrix with numpy module
    """
    A = np.array(m_a)
    B = np.array(m_b)
    return(A.dot(B))
