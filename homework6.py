lst = ['1', '2', '3', '4', '5', '6', '7', '8']

print("The list lst is {}".format(lst))

print("The zero position is {}".format(lst[0]))

print("The indexes 0:3 are {}".format(lst[0:3]))

print("The negative one position is {}".format(lst[-1]))

print("The indexes [-3:-2] are {}".format(lst[-3:-2]))

print("The indexes [-10:9] are {}".format(lst[-10:9]))

def movethisto(someList, anItem, aPosition):
	lst = someList
	lst.insert(aPosition, anItem)
	r
	return lst

print movethisto(lst,'2',5)
