# Import Needed Libraries
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Define Form as a Class
class Form( QDialog):
    # Form Constructor
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.lineedit0 = QLineEdit("File Name")
        self.label1 = QLabel("Select a Function")
        self.pbutton1 = QPushButton("Character Count")
        self.lineedit1 = QLineEdit("")
        self.pbutton2 = QPushButton("Line Count")
        self.lineedit2 = QLineEdit("")
        self.pbutton3 = QPushButton("Word Count")
        self.lineedit3 = QLineEdit("")
        self.pbutton4 = QPushButton("Count Occurences")
        self.lineedit4 = QLineEdit("Enter Word to be Counted")
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
        self.lineedit1.setFocus()
        self.connect(self.pbutton1, SIGNAL("clicked()"),self.button1Pressed)
        self.connect(self.pbutton2, SIGNAL("clicked()"),self.button2Pressed)
        self.connect(self.pbutton3, SIGNAL("clicked()"),self.button3Pressed)
        self.connect(self.pbutton4, SIGNAL("clicked()"),self.button4Pressed)
        self.connect(self.pbutton5, SIGNAL("clicked()"),self.button5Pressed)
        self.connect(self.pbutton6, SIGNAL("clicked()"),self.button6Pressed)      
 #       self.connect(self.lineedit4, SIGNAL("returnPressed()"),self.countaword)
        self.connect(self.pbuttonQuit, SIGNAL("clicked()"),self.buttonQuitPressed)
        self.setWindowTitle("File Processor")
    # Form Methods
    def button1Pressed(self):
        self.lineedit1.setText("xxxx characters counted")
    def button2Pressed(self):
        self.lineedit2.setText("xxxx lines counted")
    def button3Pressed(self):
        self.lineedit3.setText("xxxx words counted")
    def button4Pressed(self):
        self.lineedit4.setText("xxxx occurrences count of aaaaaa")
    def button5Pressed(self):
        self.lineedit5a.setText("Average of xxxxxxxx characters per word")
        self.lineedit5b.setText("Average of xxxxxxxx words per line")
    def button6Pressed(self):
        self.lineedit6a.setText("aaaaa occurrs most frequently")
        self.lineedit6b.setText("aaaaa occurs before bbbbb xxxxxx times")
        self.lineedit6c.setText("bbbbbb occurs before aaaaaa xxxxxx times")

    def buttonQuitPressed(self):
        self.done(1)
        app.quit()
    def countaword(self):
        self.lineedit4.setText("xxxx occurences found")
# End of Form Class Definition

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()

        

