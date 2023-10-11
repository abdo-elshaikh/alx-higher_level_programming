#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all 
    
    integers tuple (<score>, <weight>)"""
    if len(my_list) == 0:
        return 0
    total = 0
    weight_total = 0
    for score, weight in my_list:
        total += score * weight
        weight_total += weight
    return total / weight_total
