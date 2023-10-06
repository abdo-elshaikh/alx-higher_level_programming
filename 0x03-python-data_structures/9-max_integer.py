#!/usr/bin/python3
def max_integer(my_list=[]):
    """Return the biggest integer in a list."""
    if len(my_list) == 0:
        return (None)
    max = my_list[0]
    for i in my_list:
        if i > max:
            max = i
    return (max)
