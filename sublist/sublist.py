"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one, list_two):
    if list_one == list_two:
        return 2

    if to_string(list_one) in to_string(list_two):
        if check_list(list_one, list_two):
            return 0
    elif to_string(list_two) in to_string(list_one):
        return 1
    return 3

def to_string(list):
    return_str = []
    for item in list:
        return_str.append(str(item))
    return "".join(return_str)

def check_list(list_one, list_two):
    for item in list_one:
        if item not in list_two:
            return False
    return True
