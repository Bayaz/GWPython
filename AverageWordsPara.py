infile = "para.txt"
wordfind = 'the'

# # counts the number of total words in a file
# def CountWords(infile):
#     num_words = 0
#     with open(infile) as file:
#         for line in file:
#             words = line.split('/t')
#             num_words += len(words)
#     print words
#     return num_words

# a = CountWords(infile)
# print a

# def numberOfWords(infile):
#     num_words = 0
#     allwords = []
#     with open(infile) as file:
#         for line in file:
#             words = line.split()
#             allwords += words
#             num_words += len(words)
#     print allwords
#     return num_words

# print numberOfWords(infile)



# def numberOfWords(infile):
#     l = []
#     for line in infile:
#         l.append(line.split(','))

def AverageWordsPara(infile):
    tabcounter = 0
    num_words = 0
    with open(infile) as file:
        for line in file:
            words = line.split()
            num_words += len(words)
            if '\t' in line:
                tabcounter += 1

    print tabcounter
    print num_words
    return "The average number of words per para is {}".format(num_words/tabcounter)

print AverageWordsPara(infile)
