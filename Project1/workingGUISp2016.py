# Import Needed Libraries
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#----------------------------------------------------------------------
#============== Functions =============================================
def CountCharacters(infile):
    num_chars = 0
    num_lines = -1
    tabs = 0
    with open(infile) as file:
        for line in file:
            num_lines += 1
            num_chars += len(line)
            if '\t' in line:
                tabs += 1

    return num_chars - num_lines - tabs
#----------------------------------------------------------------------
def CountLines(infile):
    num_lines = 0
    empty_lines = 0
    with open(infile) as file:
        for line in file:
            num_lines += 1
            if line == '\n':
                empty_lines += 1
    return "There are {} non-blank and {} total lines."\
    .format(num_lines - empty_lines,num_lines)
#----------------------------------------------------------------------
def CountWords(infile):
    num_words = 0
    with open(infile) as file:
        for line in file:
            words = line.split()
            num_words += len(words)
    return num_words
#----------------------------------------------------------------------
def CountOccurences(infile, wordfind):
    total = 0
    with open(infile) as file:
        for line in file:
            words = line.split()
            stripped_words = [el.rstrip('\'\"-,.:;!?') for el in words]
            for el in stripped_words:
                if el == wordfind:
                      total += 1

    return total
#----------------------------------------------------------------------
# counts the number of total words in a file
def AverageWordsPerline(infile):
    num_words = 0
    num_linesall = 0
    empty_lines = 0
    with open(infile) as file:
        for line in file:
            num_linesall += 1
            words = line.split()
            num_words += len(words)
            if line == '\n':
                empty_lines += 1
    non_emptylines = num_linesall - empty_lines
    if num_linesall != non_emptylines:
        return "Average including empty lines is: {0:.2f}, non-empty line average is: {1:.2f} "\
        .format(float(num_words)/ float(num_linesall), float(num_words)/float(non_emptylines))
    elif num_linesall > 0 and num_linesall == non_emptylines:
        return "Average words per line is {}".format(float(num_words)/ float(num_linesall))
    else:
        return "The file is empty."
#---------------------

# counts average characters per word
def AverageCharsPerWord(infile):
    wordlength = 0
    num_words = 0
    with open(infile) as file:
        for line in file:
            words = line.split()
            num_words += len(words)
            stripped_words = [el.rstrip('\'\"-,.:;!?') for el in words]
            for el in stripped_words:
                length = len(el)
                wordlength += length
    if num_words != 0:
        return "Average chars per word is: {0:.2f}".format(float(wordlength) / float(num_words))
    else:
        return "There are no words in the file."
#---------------------

# counts average words per paragragh using tab as paragraph delimiter
def AverageWordsPara(infile):
    tabcounter = 0
    fulllinecounter = 0
    num_words = 0
    with open(infile) as file:
        for line in file:
            words = line.split()
            num_words += len(words)
            if '\t' in line:
                tabcounter += 1
            elif line != '\n':
                fulllinecounter += 1
    if tabcounter != 0:
        return "The average number of words per para is: {0:.2f}"\
        .format(num_words/tabcounter)
    elif fulllinecounter != 0:
        return "The average number of words per para is: {0:.2f}"\
        .format(num_words/fulllinecounter)
    else:
        return "The file does not have paragraphs."



#---------------------

#consolidates all average functions
def Averages(infile):
    a = AverageWordsPerline(infile)
    b = AverageCharsPerWord(infile)
    c = AverageWordsPara(infile)

    return a, b, c 

#----------------------------------------------------------------------
def CountPairs(infile, word1, word2):
    joinedWords = ''
    with open(infile) as file:
        for line in file:
            words = line.split()
            stripped_words = [el.rstrip('\'\"-,.:;!?') for el in words]
            joinedWords += ' '.join(stripped_words) + '\n'

                
    return joinedWords.count(word1 + ' ' + word2)
#----------------------------------------------------------------------
def SwitchPairs(infile, word1, word2):
    f2 = open('Switched.txt', 'w')
    joinedWords = ''
    with open(infile) as file:
        for line in file:
            words = line.split()
            stripped_words = [el.rstrip('\'\"-,.:;!?') for el in words]
            joinedWords += ' '.join(stripped_words) + '\n'

    f2.write(joinedWords.replace(word1 + ' ' + word2, word2 + ' ' + word1))
    f2.close()
    if joinedWords.count(word1 + ' ' + word2) == 1:
        return "{} instance switched, check current directory for Switched.txt file."\
                .format(joinedWords.count(word1 + ' ' + word2))
    elif joinedWords.count(word1 + ' ' + word2) > 1:
        return "{} instances switched, check current directory for Switched.txt file."\
                .format(joinedWords.count(word1 + ' ' + word2))
    else:
        return "No instance of substring found."

#============== End Functions =========================================

# Define Form as a Class
class Form( QDialog):
    # Form Constructor
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.label0 = QLabel("Enter Filename Below:")
        self.lineedit0 = QLineEdit("para.txt")
        self.label1 = QLabel("Select a Function")
        self.pbutton1 = QPushButton("Character Count")
        self.lineedit1 = QLineEdit("")
        self.pbutton2 = QPushButton("Line Count")
        self.lineedit2 = QLineEdit("")
        self.pbutton3 = QPushButton("Word Count")
        self.lineedit3 = QLineEdit("")
        self.pbutton4 = QPushButton("Count Occurences")
        self.lineedit4 = QLineEdit("Replace this text with word to be counted.")
        self.pbutton5 = QPushButton("Averages")
        self.lineedit5a = QLineEdit("Average Characters per Word")
        self.lineedit5b = QLineEdit("Average Words per Line")
        self.lineedit5c = QLineEdit("Average Words per Paragraph")
        self.pbutton6 = QPushButton("Count Pairs")
        self.lineedit6a = QLineEdit("Enter the First Word")
        self.lineedit6b = QLineEdit("Enter the Second Word")
        self.lineedit6c = QLineEdit("Number of Pairs")
        self.pbutton7 = QPushButton("Switch Pairs")
        self.lineedit7a = QLineEdit("Enter the First Word")
        self.lineedit7b = QLineEdit("Enter the Second Word")
        self.lineedit7c = QLineEdit("Pairs Switched")
        self.pbuttonQuit = QPushButton("Quit")
        layout = QVBoxLayout()
        layout.addWidget(self.label0)
        layout.addWidget(self.lineedit0)
        layout.addWidget(self.label1)
        layout.addWidget(self.pbutton1)
        layout.addWidget(self.lineedit1)
        layout.addWidget(self.pbutton2)
        layout.addWidget(self.lineedit2)
        layout.addWidget(self.pbutton3)
        layout.addWidget(self.lineedit3)
        layout.addWidget(self.pbutton4)
        layout.addWidget(self.lineedit4)
        layout.addWidget(self.pbutton5)
        layout.addWidget(self.lineedit5a)
        layout.addWidget(self.lineedit5b)
        layout.addWidget(self.lineedit5c)
        layout.addWidget(self.pbutton6)
        layout.addWidget(self.lineedit6a)
        layout.addWidget(self.lineedit6b)
        layout.addWidget(self.lineedit6c)
        layout.addWidget(self.pbutton7)
        layout.addWidget(self.lineedit7a)
        layout.addWidget(self.lineedit7b)
        layout.addWidget(self.lineedit7c)
        layout.addWidget(self.pbuttonQuit)
        self.setLayout(layout)
        self.lineedit0.setFocus()
        self.connect(self.pbutton1, SIGNAL("clicked()"),self.button1Pressed)
        self.connect(self.pbutton2, SIGNAL("clicked()"),self.button2Pressed)
        self.connect(self.pbutton3, SIGNAL("clicked()"),self.button3Pressed)
        self.connect(self.pbutton4, SIGNAL("clicked()"),self.button4Pressed)
        self.connect(self.pbutton5, SIGNAL("clicked()"),self.button5Pressed)
        self.connect(self.pbutton6, SIGNAL("clicked()"),self.button6Pressed)
        self.connect(self.pbutton7, SIGNAL("clicked()"),self.button7Pressed)       
        self.connect(self.pbuttonQuit, SIGNAL("clicked()"),self.buttonQuitPressed)
        self.setWindowTitle("File Processor")
    # Form Methods
    def button1Pressed(self):
        self.pbutton1.setFocus()
        infile = str(self.lineedit0.text())
        func1 = CountCharacters(infile)
        b1outtext = str(func1)
        self.lineedit1.setText(b1outtext)
    def button2Pressed(self):
        self.pbutton2.setFocus()
        infile = str(self.lineedit0.text())
        func2 = CountLines(infile)
        b2outtext = str(func2)
        self.lineedit2.setText(b2outtext)
    def button3Pressed(self):
        self.pbutton3.setFocus()
        infile = str(self.lineedit0.text())
        func3 = CountWords(infile)
        b3outtext = str(func3)
        self.lineedit3.setText(b3outtext)
    def button4Pressed(self):
        self.pbutton4.setFocus()
        infile = str(self.lineedit0.text())
        wordfind = str(self.lineedit4.text())
        func4 = CountOccurences(infile, wordfind)
        b4outtext = str(func4)
        self.lineedit4.setText(b4outtext)
    def button5Pressed(self):
        self.pbutton5.setFocus()
        infile = str(self.lineedit0.text())
        func5 = Averages(infile)
        b5aouttext = str(func5[0])
        b5bouttext = str(func5[1])
        b5couttext = str(func5[2])
        self.lineedit5a.setText(b5aouttext)
        self.lineedit5b.setText(b5bouttext)
        self.lineedit5c.setText(b5couttext)
        
    def button6Pressed(self):
        self.pbutton6.setFocus()
        infile = str(self.lineedit0.text())
        word1 = str(self.lineedit6a.text())
        word2 = str(self.lineedit6b.text())
        func6 = CountPairs(infile, word1, word2)
        b6couttext = str(func6)
        self.lineedit6c.setText(b6couttext)

    def button7Pressed(self):
        self.pbutton7.setFocus()
        infile = str(self.lineedit0.text())
        word1 = str(self.lineedit7a.text())
        word2 = str(self.lineedit7b.text())
        func7 = SwitchPairs(infile, word1, word2)
        b7couttext = str(func7)
        self.lineedit7c.setText(b7couttext)


    def buttonQuitPressed(self):
        self.done(1)
        app.quit()

# End of Form Class Definition

app = QApplication(sys.argv)
form = Form()
form.setGeometry(50, 50, 500, 800)
form.show()
app.exec_()

        

