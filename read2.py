# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:54:22 2016
@author: James
d"""

print "Type the name of the file you want to analyze:"
txt_file = raw_input("> ")

num_chars = 0
num_lines = 0
num_words = 0


with open(txt_file) as file:
    for line in file:
        words = line.split()
        num_chars += len(line)
        num_lines += 1
        num_words += len(words)
        
stripped_words = [el.rstrip('\'\"-,.:;!?') for el in words]

print stripped_words  

print("Type the name of the word before the one you are looking for: ")

word_to_find = raw_input("> ")
base_word =  stripped_words.index(word_to_find)


words_after = []
for i,w in enumerate(stripped_words):
    if w == word_to_find:
        # next word
        words_after.append(stripped_words[i+1])

print words_after
       
output = ("""
The number of characters in the file is {}
The number of words in the file is {}
The number or lines in the file is {}
"""
.format(num_chars,num_words,num_lines))

print output

dest_file = 'output.txt'
open(dest_file, 'w').write(output)



