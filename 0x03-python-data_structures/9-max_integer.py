#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    for i in my_list:
        max_element = my_list[i]
        if i > max_element:
            max_element = i
        return max_element
