#!/usr/bin/python3
'''The minimum operations coding challenge.
'''

def minOperations(n):
    """
    Function minOperations
    Returns an integer
    """
    result = 0
    x = 2
    while n > 1:
        while n % x == 0:
            result += x
            n /= x
        x += 1
    return result