#!/usr/bin/python3
"""Contains function that returns a list of lists of integers
reprsenting the Pascal's triangle
"""


def pascal_triangle(n):
    """Returns list of lists of pascal's triangle integers
    """

    list_of_list = []
    if n > 0:
        for _ in range(n):
            pascal_list = []

            # Pascal coeff = nCr = n! / (r! * (n-r)!)
            # to accommodate index 0
            n = n - 1
            for r in range(n + 1):
                num = factorial(n) / (factorial(r) * factorial(n - r))
                pascal_list.append(round(num))
            list_of_list.append(pascal_list)

    return list_of_list[::-1]


def factorial(n):
    """Helper function for calculating factorial"""
    if n == 0:
        return 1
    elif n == 1:
        return 1
    return n * factorial(n-1)
