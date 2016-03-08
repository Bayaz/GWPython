#wordcounta.py

infile = "wordcount.txt"
inword = 'the.'
def wordCounta(infile, inword):
	try:
		count_file = open(infile)
	except:
		print "File cannot be opened or doesn't exist in directory", infile
		exit()

	word_counts = dict()
	for line in count_file:
		words = line.split()

		print words

		for word in words:
			if word not in word_counts:
				word_counts[word] = 1
			else:
				word_counts[word] += 1

	print word_counts #used for testing to see if dictionary is populating
	try:
		if word_counts[inword] == 1:
			print "'{}' shows up {} time." .format(inword, word_counts[inword])
		else:
			print "'{}' shows up {} times." .format(inword, word_counts[inword])
	except:
		print "The word you chose is not in the file."

wordCounta(infile, inword)

