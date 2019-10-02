import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
widget = QWidget()
label = QLabel("Result:",widget)

AddButton = QPushButton("+", widget)
SubtractButton = QPushButton("-", widget)
MultiplyButton = QPushButton("*", widget)
DivideButton = QPushButton("/", widget)
PercentButton = QPushButton("%", widget)

txtArea1 = QLineEdit("", widget)
txtArea2 = QLineEdit("", widget)

def init():
    widget.resize(250, 300)
    widget.move(250, 300)
    widget.setWindowTitle('Calculator')
    widget.show()
 
    txtArea1.move(20, 30)
    txtArea2.move(20, 80)
    
 
    label.setText("")
    label.move(20, 110)
    
 
    AddButton.setToolTip("Addition")
    AddButton.move(20, 160)
    AddButton.clicked.connect(addition)
    
 
    SubtractButton.setToolTip("Subtraction")
    SubtractButton.move(110, 160)
    SubtractButton.clicked.connect(subtraction)
    
 
    DivideButton.setToolTip("Division")
    DivideButton.move(20, 200)
    DivideButton.clicked.connect(division)
    
 
    MultiplyButton.setToolTip("Multiplication")
    MultiplyButton.move(110, 200)
    MultiplyButton.clicked.connect(multiplication)
   

    PercentButton.setToolTip("Percentage")
    PercentButton.move(70,235)
    PercentButton.clicked.connect(percent)

 
 
def addition():
    num1 = int(txtArea1.text())
    num2 = int(txtArea2.text())
    label.setText(str(num1) + "+" + str(num2) + "=" + str(num1 + num2))
 
 
def subtraction():
    num1 = int(txtArea1.text())
    num2 = int(txtArea2.text())
    label.setText(str(num1) + "-" + str(num2) + "=" + str(num1 - num2))
 
 
def multiplication():
    num1 = int(txtArea1.text())
    num2 = int(txtArea2.text())
    label.setText(str(num1) + "*" + str(num2) + "=" + str(num1 * num2))
 
 
def division():
    num1 = int(txtArea1.text())
    num2 = int(txtArea2.text())
    label.setText(str(num1) + "/" + str(num2) + "=" + str(num1 / num2))

def percent():
    num1 = int(txtArea1.text())
    label.setText(str(num1/100))

 
 
if __name__ == "__main__":
    init()
 
app.exec_()

