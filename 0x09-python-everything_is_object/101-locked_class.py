#!/usr/bin/python3
"""blocked class module"""


class LockedClass:
    """objest prevents dynamic attribute"""

    __slots__ = ['first_name']
