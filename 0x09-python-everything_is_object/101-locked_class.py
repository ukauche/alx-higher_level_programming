#!/usr/bin/python3
"""A defined locked class."""


class LockedClass:
    """
    Stops user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
