# Import Needed Libraries
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
# Define twotimes function
def twotimes(x):
    return 2*x
# Define Form as a Class
class Form( QDialog):
    # Form Constructor
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setWindowTitle("TwoTimes GUI") # Set Window Title
        self.pbutton1 = QPushButton("Press Button")     # Create Push Button
        self.lineedit1 = QLineEdit("Put Number Here")   # Creade Line Edit
        self.pbuttonQuit = QPushButton("Quit")              # Create Another Push Button
        layout = QVBoxLayout()                                      # Create a Layout for Widgets
        layout.addWidget(self.pbutton1)                         # Add pbutton1 to layout
        layout.addWidget(self.lineedit1)                        # Add lineedit1 to layout
        layout.addWidget(self.pbuttonQuit)                  # Add Quit button to layout
        self.setLayout(layout)                                          # Apply the Layout to the Form
        self.pbutton1.setFocus()                                    # This is probably not necessary but it actives pbutton1
        self.connect(self.pbutton1, SIGNAL("clicked()"),self.button1Pressed)    # Connects pbutton1 to a method
        self.connect(self.pbuttonQuit, SIGNAL("clicked()"),self.buttonQuitPressed)  # Connect Quit button to a method

    # Form Methods
    def button1Pressed(self):           # Method to be involved when pbutton1 is pressed
        x1 = int(self.lineedit1.text()) # this is the input
        x2 = twotimes(x1)
        outtext =  str(x1) + " times 2 is " + str(x2)
        self.lineedit1.setText(outtext)
    def buttonQuitPressed(self):        #Method to be involved when Quitbutton is pressed
        self.done(1)
        app.quit()
   
# End of Form Class Definition

app = QApplication(sys.argv)    # Create Application
form = Form()                           # Create Instance of Form
form.show()                             # Show the Form
app.exec_()                             # Start Event Handler Loop

        

