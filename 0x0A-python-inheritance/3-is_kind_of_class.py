#!/usr/bin/python3
"""is_kind_of_class module.

Contains function that compares an object with an instance.
"""


def is_kind_of_class(obj, a_class):
    """Method that return True if an object is an instance of a class
    that inherited from"""

    return isinstance(obj, a_class)
