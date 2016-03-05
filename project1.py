# -*- coding: utf-8 -*-
infile = "test1.txt"

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


