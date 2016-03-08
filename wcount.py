infile = "test1.txt"

def countWord(infile):
	all_words = []
	with open(infile) as file:
		for line in file:
			words = line.split()
			#print words
			all_words += words	

		for word in all_words:
			word = word.rstrip('\'\"-,.:;!?')

				#stripped_words = words

	#stripped_words = [el.rstrip('\'\"-,.:;!?') for el in words] #shorter way to do for loop

	return all_words, len(all_words)
d = countWord(infile)
print d

# def numberOfWords(infile):
# 	num_words = 0
# 	with open(infile) as file:
# 		for line in file:
# 			words = line.split()
# 			num_words += len(words)
# 	return num_words

# a = numberOfWords(infile)
# print a