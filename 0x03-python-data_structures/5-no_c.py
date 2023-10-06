#!/usr/bin/python3
def no_c(my_string):
    strng_list = []
    for i in my_string:
        strng_list.append(i)
    result = ""
    for x in strng_list:
        if x not in ['c', 'C']:
            result += x
    return result
