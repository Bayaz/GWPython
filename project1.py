# -*- coding: utf-8 -*-
infile = "test1.txt"
wordfind = 'the'

def numberOfWords(infile):
	num_words = 0
	with open(infile) as file:
		for line in file:
			words = line.split()
			num_words += len(words)
	return num_words

a = numberOfWords(infile)
print a

def numberOfLines(infile):
	num_lines = 0
	with open(infile) as file:
		for line in file:
			num_lines += 1
	return num_lines

b = numberOfLines(infile)
print b

def numberOfChars(infile):
	num_chars = 0
	num_lines = 0
	with open(infile) as file:
		for line in file:
			num_lines += 1
			num_chars += len(line)
	return num_chars - num_lines

c = numberOfChars(infile)
print c

def countWord(infile):
	with open(infile) as file:
		for line in file:
			words = line.split()

	stripped_words = [el.rstrip('\'\"-,.:;!?') for el in words]

	return stripped_words, len(stripped_words)
d = countWord(infile)
print d

def wordCounta(infile, wordfind):
	try:
		count_file = open(infile)
	except:
		print "File cannot be opened or doesn't exist in directory", infile
		exit()

	word_counts = dict()
	for line in count_file:
		words = line.split()
		for word in words:
			if word not in word_counts:
				word_counts[word] = 1
			else:
				word_counts[word] += 1

	print word_counts
	try:
		wordfind = word_counts[wordfind]
		print wordfind
	except:
		print "That word does not exist in the file"
		exit()

wordCounta(infile, wordfind)


