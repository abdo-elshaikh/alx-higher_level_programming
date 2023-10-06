#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replace an element in a list."""
    result = []
    if idx < 0 or idx >= len(my_list):
        for i in range(len(my_list)):
            result.append(my_list[i])
    else:
        for i in range(len(my_list)):
            if i == idx:
                result.append(element)
            else:
                result.append(my_list[i])
    return result
