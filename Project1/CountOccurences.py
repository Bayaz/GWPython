infile = "test1.txt"
wordfind = 'at'

def CountOccurences(infile, wordfind):
    total = 0
    with open(infile) as file:
        for line in file:
            words = line.split()
            stripped_words = [el.rstrip('\'\"-,.:;!?') for el in words]
            print stripped_words
            for el in stripped_words:
                if el == wordfind:
                      total += 1

    return total

CountOccurences(infile, wordfind)
