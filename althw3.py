## -*- coding: utf-8 -*-
#"""
#Created on Wed Feb  3 15:38:21 2016
#
#@author: JimmyHome
#"""
##---------------------------------------------------------------------- 
#num_one = int(raw_input("Type in starting number of range >>>"))
#num_two = int(raw_input("Type in ending number of range >>>")) + 1
#
#num_range = range(num_one, num_two)
#num_sum = sum(num_range)
#
#print("Here is a list of the numbers in the range\n{}".format(num_range))
#print("The sum of all the numbers in the range is {}".format(num_sum))
#
#def only_evens(ls):
#    even_nums = []
#    for num in ls:
#        if num % 2 == 0:
#            even_nums.append(num)
#    return even_nums
#    
#num_range_evens = only_evens(num_range)
#
#print num_range_evens
#
##---------------------------------------------------------------------- 
#
#fact = int(raw_input("Enter a number to get the factorial: "))
#factorial = 1
#
## check if the number is negative, positive or zero
#if fact < 0:
#   print("Factorials do not exist for negative numbers")
#elif fact == 0:
#   print("The factorial of 0 is 1")
#else:
#   for i in range(1,fact + 1):
#       factorial = factorial*i
#   print("The factorial of {} is {}".format(fact,factorial))
#
##---------------------------------------------------------------------- 
#
#fib = int(raw_input("Enter a number to generate fibonacci to that index: "))
#
#def make_fibonacci(n):
#    fib = []
#    a, b = 0, 1
#    for i in range(n):
#        a, b = b, a+b
#        fib.append(a)
#    return tuple(fib)
#
#print make_fibonacci(fib)
#
##---------------------------------------------------------------------- 

name_string = raw_input("Write a string with your name in it >>>")

print("There are {} characters in your string".format(len(name_string)))
ns_to_list = name_string.split()

print ns_to_list


for word in ns_to_list:
    strlength = len(word)
    print("\"{}\" is {} characters long".format(word, strlength))