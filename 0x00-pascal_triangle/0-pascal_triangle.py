"""Contains function that returns a list of lists of integers
reprsenting the Pascal's triangle"""


def pascal_triangle(n):
    """Returns list of lists of pascal's triangle integers"""

    if n <= 0:
        return []
    else:
        # The coefficeint of any value of n is given by
        # coeff = nCr = n! / (r! * (n-r)!)
        list_of_list = []

        def factorial(n):
            """Helper function for calculating factorial"""
            if n == 0:
                return 1
            elif n == 1:
                return 1
            return n * factorial(n-1)

        for _ in range(n):
            pascal_list = []

            # counter variable
            r = 0
            # to accommodate index 0
            n = n - 1
            for _ in range(n + 1):
                num = factorial(n) / (factorial(r) * factorial(n - r))
                r += 1
                pascal_list.append(int(num))
            list_of_list.append(pascal_list)

    # Return a reversed version of list of list to ensure to ensure
    # increasing other as required
    return list_of_list[::-1]
