#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Returns a tuple with 2 integers."""
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = (0, 0)
        else:
            tuple_a = (tuple_a[0], 0)
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = (0, 0)
        else:
            tuple_b = (tuple_b[0], 0)
    if len(tuple_a) > 2 or len(tuple_b) > 2:
        tuple_a = tuple_a[:2]
        tuple_b = tuple_b[:2]
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
