infile = "proj1.txt"
wordfind = 'the'

def CountCharacters(infile):
    num_chars = 0
    num_lines = 0
    tabs = 0
    with open(infile) as file:
        for line in file:
            num_lines += 1
            num_chars += len(line)
            if "\t" in line:
                tabs += 1
    return num_chars - num_lines - tabs

c = CountCharacters(infile)
print c