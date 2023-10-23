#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print x and only integers elements of a list."""
    i = 0
    len = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            len += 1
        except (TypeError, ValueError):
            pass
        i += 1
    print()
    return len
