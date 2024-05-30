#!/usr/bin/python3
""" Pascal's Triangle """

def pascal_triangle(n):
    """ Returns a lists of integers representing Pascal's triangle of n """
    if n <= 0:
        return []

    pastri = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(pastri[i-1][j-1] + pastri[i-1][j])
        row.append(1)
        pastri.append(row)
    return pastri

