#!/usr/bin/python3
def uniq_add(my_list=[]):
    newlist = set(my_list)
    total = 0
    for i in newlist:
        total += i
    return (total)
