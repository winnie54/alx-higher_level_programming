#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list:
        for n in reversed(range(1, 6)):
            print("{:d}".format(n))
