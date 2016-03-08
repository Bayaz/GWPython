infile = "test1.txt"
wordfind = 'the'

# counts the number of total words in a file
def CountWords(infile):
    num_words = 0
    with open(infile) as file:
        for line in file:
            words = line.split()
            num_words += len(words)
    return num_words

a = CountWords(infile)
print a