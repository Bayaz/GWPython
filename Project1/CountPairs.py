infile = "para.txt"
word1 = 'CSE'
word2 = 'is'


def CountPairs(infile, word1, word2):
    joinedWords = ''
    with open(infile) as file:
        for line in file:
            words = line.split()
            stripped_words = [el.rstrip('\'\"-,.:;!?') for el in words]
            joinedWords += ' '.join(stripped_words) + '\n'

                
    return joinedWords.count(word1 + ' ' + word2)

print CountPairs(infile, word1, word2)


