# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 19:17:44 2016

@author: JimmyHome
"""

#reasons for reusable components: simplicity, productivity, 
#reliability, performance

a = "week 4 class\n"

print a

# functions vs subroutines (void functions in book)
# subroutines provide early form of encapsulation (internals not available)
# procedural abstraction th performs a taslk on share memory - subroutine
# funtion procedural abstraction that enforces referenctial transparency and 
# returns a value
# functions provide greater reliabiliy and can be used in an expression
# call parameters to a function samplefunction(param1, param2) when defining

# when calling the parameters are called arguments!!!

# void function (subroutine) does not alter any value outside its scope, still does stuff
def dummy(x, y):
    z = x + y
    print z
    
# function that returns a value
def addthese(x, y):
    z = x + y
    return z
    
i  = addthese(4, 5)

j = dummy(4, 5)

print type(j)

print type(i)

#------------------------------------------------------------------------------
# does a factorial
def fact(n):
        r = 1
        while n > 0:
            r = r * n
            n = n - 1
        return r
            
print fact(4)

#------------------------------------------------------------------------------
#another example
def factorial (n):
	if (n <= 1):
		return 1

	i = 1
	product = 1
	while (i <= n):
		product = product * i
		i = i + 1

	return product
 
print factorial(4)
#------------------------------------------------------------------------------

#scoping rules

# Global variables that can be caleld anywhere in program
# Local scope are used within a function
# weird stuff below

cat = "global string"

def printcat(a):
 #   print cat
    cat = "local string"
    print cat
    print a
    
printcat(cat)


# functions are standalone, methods are functions associated with a class
#str.lower  in str.lower("ABCD") is a method because str is an object
glob = "global variable"

def cglob():
    glob = "xxxx"
    print glob

cglob()

print glob

#------------------------------------------------------------------------------



