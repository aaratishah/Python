from math import *
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
TangentButton = QPushButton("tan", widget)
SineButton = QPushButton("sin", widget)
CosineButton = QPushButton("cos", widget)
FactButton = QPushButton("!", widget)
ClearButton = QPushButton("C", widget)

txtArea1 = QLineEdit("", widget)
txtArea2 = QLineEdit("", widget)

def init():
    widget.resize(250, 350)
    widget.move(250, 350)
    widget.setWindowTitle('Calculator')
    widget.show()
 
    txtArea1.move(20, 30)
    txtArea2.move(20, 80)
     
    label.setText("")
    label.move(20, 110)
    label.show()
     
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
    PercentButton.move(20, 240)
    PercentButton.clicked.connect(percent)

    TangentButton.setToolTip("Tangent")
    TangentButton.move(110, 240)
    TangentButton.clicked.connect(tangent)

    SineButton.setToolTip("Sine")
    SineButton.move(20, 280)
    SineButton.clicked.connect(sine)

    CosineButton.setToolTip("Cosine")
    CosineButton.move(110, 280)
    CosineButton.clicked.connect(cosine)

    FactButton.setToolTip("Factorial")
    FactButton.move(20, 320)
    FactButton.clicked.connect(factorials)

    ClearButton.setToolTip("Clear")
    ClearButton.move(110,120)
    ClearButton.clicked.connect(clear)

 
def addition():
    num1 = int(txtArea1.text())
    num2 = int(txtArea2.text())
    label.setFixedWidth(200)
    label.setText(str(num1) + "+" + str(num2) + "=" + str(num1 + num2))
 
 
def subtraction():
    num1 = int(txtArea1.text())
    num2 = int(txtArea2.text())
    label.setFixedWidth(200)
    label.setText(str(num1) + "-" + str(num2) + "=" + str(num1 - num2))
 
 
def multiplication():
    num1 = int(txtArea1.text())
    num2 = int(txtArea2.text())
    label.setFixedWidth(200)
    label.setText(str(num1) + "*" + str(num2) + "=" + str(num1 * num2))
 
 
def division():
    num1 = int(txtArea1.text())
    num2 = int(txtArea2.text())
    label.setFixedWidth(200)
    label.setText(str(num1) + "/" + str(num2) + "=" + str(num1 / num2))

def percent():
    num1 = int(txtArea1.text())
    label.setFixedWidth(200)
    label.setText(str(num1/100))

def tangent():
    num1 = int(txtArea1.text())
    #num2 = int(txtArea2.text())
    label.setFixedWidth(200)
    label.setText("tan" + str(num1) + "=" + str(tan(num1)))

def sine():
    num1 = int(txtArea1.text())
    #num2 = int(txtArea2.text())
    label.setFixedWidth(200)
    label.setText("sin" + str(num1) + "=" + str(sin(num1)))

def cosine():
    num1 = int(txtArea1.text())
    #num2 = int(txtArea2.text())
    label.setFixedWidth(200)
    label.setText("cos" + str(num1) + "=" + str(cos(num1)))

def factorials():
    num1 = int(txtArea1.text())
    label.setFixedWidth(200)
    label.setText(str(num1) + " !" + " = " + str(factorial(num1))) 

def clear():
    txtArea1.setText("")
    txtArea2.setText("")
    label.setText("")

if __name__ == "__main__":
    init()
 
app.exec_()

