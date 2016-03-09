infile = "para.txt"
word1 = 'This'
word2 = 'year'

def SwitchPairs(infile, word1, word2):
    f2 = open('SwitchedWordsFile.txt', 'w')
    joinedWords = ''
    with open(infile) as file:
        for line in file:
            words = line.split()
            stripped_words = [el.rstrip('\'\"-,.:;!?') for el in words]
            joinedWords += ' '.join(stripped_words) + '\n'

    f2.write(joinedWords.replace(word1 + ' ' + word2, word2 + ' ' + word1))
    f2.close()
    return joinedWords.count(word1 + ' ' + word2)
    
print SwitchPairs(infile, word1, word2)