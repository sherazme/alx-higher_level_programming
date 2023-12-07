#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list:
        k = j = 0
        for i in my_list:
            k += i[0] * i[1]
            j += i[1]
        return (k / j)
    return (0)
