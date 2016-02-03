# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 18:55:38 2016

@author: JimmyHome
"""

a = range(0,16)

print a


def print_is_even(a):
    for num in a:
        if num % 2 == 0:
            print num


c = []

for num in a:
    if num % 2 == 0:
        c.append(num)
print(type(a))
print("The even numbers in the list are {}".format(c))

print_is_even(a)
    

    


    




    

