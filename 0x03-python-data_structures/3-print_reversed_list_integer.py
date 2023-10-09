#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list."""
    if my_list:
        for i in range(0, len(my_list)):
            print('{:d}'.format(my_list[(-i) - 1]))
