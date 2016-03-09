# number of words divided by number of lines

infile = "para.txt"
wordfind = 'the'

# counts the number of total words in a file
def CountWords(infile):
    num_words = 0
    num_linesall = 0
    empty_lines = 0

    with open(infile) as file:
        for line in file:
            num_linesall += 1
            words = line.split()
            num_words += len(words)
            if line == '\n':
                empty_lines += 1

    non_emptylines = num_linesall - empty_lines
    # print non_emptylines
    # print num_linesall, num_words
    return "Average including empty lines is {}, non-empty line average is: {} "\
    .format(float(num_words)/ float(num_linesall), float(num_words)/float(non_emptylines))

a = CountWords(infile)
print a

def CountOccurences(infile):
    wordlength = 0
    num_words = 0
    with open(infile) as file:
        for line in file:
            words = line.split()
            num_words += len(words)
            stripped_words = [el.rstrip('\'\"-,.:;!?') for el in words]
            #print stripped_words
            for el in stripped_words:
                length = len(el)
                wordlength += length
                # if el == wordfind:
                #       total += 1

    print "Average chars per word is: {}".format(float(wordlength) / float(num_words))


CountOccurences(infile)



