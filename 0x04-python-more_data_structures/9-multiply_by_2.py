#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dictionary2 = {}
    for key, value in a_dictionary.items():
        dictionary2[key] = value * 2

    return (dictionary2)
