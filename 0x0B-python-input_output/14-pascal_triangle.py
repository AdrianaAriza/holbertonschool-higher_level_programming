#!/usr/bin/pythpn3
def pascal_triangle(n):
    pl = []
    if n == 1:
        pl = [1]
    else:
        pl = [[1], [1, 1]]
        if n > 2:
            for i in range(2, n):
                pl.append([])
                for j in range(i + 1):
                    if j == 0 or j == i:
                        pl[i].append(1)
                    else:
                        x = pl[i-1][j-1] + pl[i-1][j]
                        pl[i].append(x)
    return pl
