#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """ multiplies two matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if all(not isinstance(i, list) for i in m_a):
        raise TypeError("m_a must be a list of lists")
    if all(not isinstance(i, list) for i in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for i in m_a:
        if not all(isinstance(j, (int, float)) for j in i):
            raise TypeError("m_a should contain only integers or floats")
    for i in m_b:
        if not all(isinstance(j, (int, float)) for j in i):
            raise TypeError("m_b should contain only integers or floats")
    if not all(len(i) == len(m_a[0]) for i in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(i) == len(m_b[0]) for i in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    n_m = []
    for i in range(len(m_a)):
        f = []
        for k in range(len(m_b[0])):
            n = 0
            for j in range(len(m_b)):
                n = n + m_a[i][j] * m_b[j][k]
            f.append(n)
        n_m.append(f)
    return (n_m)
