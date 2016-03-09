infile = "testfile.txt"
wordfind = 'Line'

def CountOccurences(infile, wordfind):
    wordlength = 0
    num_words = 0
    with open(infile) as file:
        for line in file:
            words = line.split()
            num_words += len(words)
            stripped_words = [el.rstrip('\'\"-,.:;!?') for el in words]
            print stripped_words
            for el in stripped_words:
                length = len(el)
                wordlength += length
                # if el == wordfind:
                #       total += 1

    print wordlength, num_words, "Average chars per word is: {}".format(float(wordlength) / float(num_words))


CountOccurences(infile, wordfind)