# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 19:16:00 2016

@author: JimmyHome
"""
#----------------------------------------------------------------------
s = "a\tb\tc\nd"

print s
#----------------------------------------------------------------------
d = "\\n is a newline character"

print d
#----------------------------------------------------------------------
e = "\\\\n what will happen"

print e
#----------------------------------------------------------------------
g = "abce"

print g
print g[0:3]
#--- while loop ---
index = 0
while index < len(g):
    letter = g[index]
    print letter
    index = index + 1
print  "\nbreak \n"
#--- for loop ---
for letter in g:
    print letter
print  "\nbreak \n"
#---------------------------------------------------------------------
ls = [1,'a', 3, 'b']
for thing in ls:
    print thing
print  "\nbreak \n"
#---------------------------------------------------------------------
#strip only works on beginning and end
v = 'xxxabcxxxx'
print v.strip('x')
c = 'xxxabcxxxabc'
print c.strip('x')
#---------------------------------------------------------------------
f = open("testfile.txt", "w")

f.write("First Line\r\n")
f.write("Second Line\r\n")
f.close()
#---------------------------------------------------------------------
f = open("testfile.txt", "r")
count = 0
line = f.readline()
while line != "":
    count = count +1
    line = f.readline()
f.close()
print "count = " , count
#---------------------------------------------------------------------
f = open("testfile.txt", "r")
linecount = 0
charcount = 0

line = f.readline()
while line != "":
    linecount = linecount + 1
    charcount = charcount + len(line)
    line = f.readline()
f.close()
print "linecount = " , linecount
print "charcount = ", charcount






    
    



