#!/usr/bin/python3

def inherits_from(obj, a_class):
    """returns True if the object is an
    instance of, or if the object is an
    instance of a class that inherited
    from, the specified class ; otherwise False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
