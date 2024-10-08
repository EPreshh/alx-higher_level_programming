#!/usr/bin/python3
"""
This module defines a function that adds 2 integers.
Function:
- add_integer(a, b=98): Return the sum of a and b.
"""


def add_integer(a, b=98):
    """ Add two numbers and return the result.
    Args:a, b.
    Returns: The result of a + b """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
