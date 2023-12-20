#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represent a square"""

    def __init__(self, size):
        """Initialize  new square.
        Args:
            size(int): The size of the new square.
        """
        self.__size = size

    def get_size(self):
        return self.__size
