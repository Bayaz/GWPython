print("add and concatenate i = 5 and s = '5' ")

i = 5
s = '5'

print("i is this type:")
print(type(i))

print("s is this type:")
print(type(s))

print("To add, change s to and int using int(s) function\n \
	now s is:")
s = int(s)
print(type(s))

print("i equals {} and s = {}, i + s = : {}".format(i, s, s + i))

print("To concatenate i and s change them both to strings \
using the str() function")
 
i = str(i)
s = str(s)

print("i is this type:")
print(type(i))

print("s is this type:")
print(type(s))

print("i concatenated with s is : {}".format(i + s))

print("Now concatenate i with \"4\"")
print("{} concatenated with {} is: {}".format(i, '4', i + '4'))
newnum = str(i + '4')
print("Now changing '54' to an integer and dividing by 2")

print int(newnum) / 2

print("How many operators are in: (5 + 7)/4 + 2 ?")
print("3 operators.... +, /, and +")

print("Using / and // for division results in the same value \n\
when the integers or floats have have no remainder, they are \n \
both integers, the only time they are different is when divinding \n\
floats with remainders in which case // will return floor division ")

print (""" Here are some examples:\n\n\
print 5 / 3 \n
print 5 // 3 \n
print 5.0 / 3.0 \n
print 5.0 // 3.0 
""")
print 5 / 3 
print 5 // 3 
print 5.0 / 3.0 
print 5.0 // 3.0 

i = 1
print("i = 1")
print(i)

i = i = i
print("i = i = i")
print(i)

i == i == i
print("i == i == i")
print i

i = 1
j = 2
print("i = 1 and j = 2 and z =3")
print(i, j)

i = i = j
print("i = i = j")
print(i, j)

i = 1
j = 2

i = j = i
print("i = j = i")
print(i, j)

i = 1
j = 2
z = 3

j = i = i = z
print("j = i = i = z")
print(i, j, z)

print("Notice how they evalute beginning from the right feeding back to the left")
