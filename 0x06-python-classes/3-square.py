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
    def __init__(self, size=0):
        """
        Initializes the square with a private size attribute.

        Args:
            size: The size of the square (no type/value verification).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size