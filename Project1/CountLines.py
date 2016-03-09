infile = "test1.txt"
wordfind = 'the'


def CountLines(infile):
    num_lines = 0
    empty_lines = 0
    with open(infile) as file:
        for line in file:
            num_lines += 1
            if line == '\n':
                empty_lines += 1
    return num_lines - empty_lines

b = CountLines(infile)
print b