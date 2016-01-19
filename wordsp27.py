#words.py python 2.7
#returns the word that occurs the most in a file

name = raw_input('Enter File Name: ')
handle = open(name, 'r')
text = handle.read()
words = text.split()
counts = dict()

for word in words:
    counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
        
print("The word that show up the most is '{}', which shows up {} \
times".format(bigword, bigcount))