#!/usr/bin/python3
"""MyList module.

Contains a class MyList that inherits from list
and a method that prints the sorted list.
"""


class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """Methot that sorted a list"""

        print(sorted(list(self)))
