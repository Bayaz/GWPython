#words_alt.py
#code from CSEV (original author) in Python3 
#uses slightly different syntax ln15 list function
#uses '=='' as opposed to 'is' line 16

name = input('Enter file:')
handle = open(name, 'r')
text = handle.read()
words = text.split()
counts = dict()
for word in words: 
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in list(counts.items()):
    if bigcount == None or count > bigcount:
        bigword = word 
        bigcount = count 

print(bigword, bigcount)