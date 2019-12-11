#!/usr/bin/python3
n = 1
m = 0
for i in range(m, 8):
    for j in range(n, 10):
        print("{:d}{:d}".format(i, j), end=", ")
    n = n + 1
    m = m + 1
i = i + 1
print("{:d}{:d}".format(i, j))
