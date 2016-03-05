#wordcounta.py

infile = "wordcount.txt"

def wordCounta(infile):
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

	print word_counts['the']

wordCounta(infile)

