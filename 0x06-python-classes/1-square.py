#!/usr/bin/python3
"""
This module defines a Square class used to represent a square shape.

The Square class includes methods for initializing a square with a given
size, which is stored as a private instance attribute.
"""


class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square,a private instance attribute.

    Methods:
        __init__(self, size): Initializes the square with the specified size.
    """
    def __init__(self, size):
        """
        Initializes the square with a private size attribute.

        Args:
            size: The size of the square (no type/value verification).
        """
        self.__size = size
