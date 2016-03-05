# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 19:49:06 2016

@author: JimmyHome
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


#definitions for gui

def twotimes(x):
   return 2*x

#define form as a class
#setFocus() means that if you hit RETURN it will execute whatever iti s set to
class Form( QGialog):
   @Form Constructor
   def __init__(self, parent=None):
       super(Form, self).__init__(parent)
       self.setWindowTitle("TwoTimes GUI") #set window title
       self.pbutton1 = QPushButton("Press Button") #create pushbutton
       self.lineedit1 = QLineEdit("Put Number Here") #create line edit
       self.pbuttonQuit = QPushButton("Quit")
       layout = QVBoxLayout()
       layout.addwidget(self.pbutton1)
#_______ more stuff needed__________________
       
       
       #form methods
   def button1Pressed(self):
       x1 = int(self.lineedit1.text())
       x2 = twotimes(x1)
        

