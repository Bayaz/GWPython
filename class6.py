# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 19:47:31 2016

@author: JimmyHome
"""

mylist = ['first', 'second', 'third', 'fourth']

print mylist[1:3]

print mylist[1]

print mylist[1:]

print len(mylist)

# notice that len is a function because it stands alone

mylist.append('fifth')

# append is a method because it is preceded by a period

print mylist

print mylist.count('fifth')
#count counts the number of instances ofthe value fifth in list myslist

a =  'sample string'.join(mylist)
print a 

#how it realy works
b = ' '.join(mylist)

print b

print b.split()

#below you can use third or a spae or comma (anything really) as  delimiter
#split() assumes it splits on a blank..can even delimit letters in a word 'ir'
print b.split('third')


d = ' '.join(['this', 'is', 'separated', 'by', 'spaces'])
print d
e = '\t'.join(['this', 'is', 'separated', 'by', 'tabs'])
print e

li = 'asc'

x = li

print x

print li is x

print dir(x)


print id(x)

print id(li)

f = open('home6.txt')
linecount = 0
wordcount = 0
charcount = 0
line = f.readline()
#do while stuff  from slides
tup = (1, 2, 3)
print tup

anotherTup = (1, 2, tup, 3)

#nested tuple example

print anotherTup

#how is a set different than a list???
mysetlist = [1,1,2,2,3,3,4,4]
myset =  set(mysetlist)
#notice that the set gets rid of non unique values
print myset

#dictionary is a mutable set of ordered pairs can acces by element or pair
#midterm is next week

s = 4 + 4.0

print s



#while not [] is an infinite loop because it [] is false, ['anyvlaue'] is True

