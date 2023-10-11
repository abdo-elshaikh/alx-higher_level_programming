#!/usr/bin/python3
def common_elements(set_1, set_2):
    """ set of common elements in two sets"""
    new_list = []
    for i in set_1:
        if i in set_2:
            new_list.append(i)
    return set(new_list)
