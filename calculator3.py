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
squareBotton = QPushButton(" a²", widget)
squarerootBotton = QPushButton("√", widget)
cubeButton = QPushButton("a³", widget)
cuberootButton = QPushButton("∛", widget)

txtArea1 = QLineEdit("", widget)
txtArea2 = QLineEdit("", widget)

def init():
    widget.resize(350, 350)
    widget.move(350, 350)
    widget.setWindowTitle('Calculator')
    widget.show()
 
    txtArea1.move(20, 30)
    txtArea2.move(20, 70)
     
    label.setText("")
    label.move(20, 110)
    label.show()
     
    AddButton.setToolTip("Addition")
    AddButton.move(20, 170)
    AddButton.clicked.connect(addition)
     
    SubtractButton.setToolTip("Subtraction")
    SubtractButton.move(110, 170)
    SubtractButton.clicked.connect(subtraction)
     
    DivideButton.setToolTip("Division")
    DivideButton.move(20, 210)
    DivideButton.clicked.connect(division)
     
    MultiplyButton.setToolTip("Multiplication")
    MultiplyButton.move(200, 170)
    MultiplyButton.clicked.connect(multiplication)
   
    PercentButton.setToolTip("Percentage")
    PercentButton.move(200, 130)
    PercentButton.clicked.connect(percent)

    TangentButton.setToolTip("Tangent")
    TangentButton.move(200, 210)
    TangentButton.clicked.connect(tangent)

    squarerootBotton.setToolTip("SquareRoot")
    squarerootBotton.move(200, 250)
    squarerootBotton.clicked.connect(squareroot)

    SineButton.setToolTip("Sine")
    SineButton.move(110, 210)
    SineButton.clicked.connect(sine)

    CosineButton.setToolTip("Cosine")
    CosineButton.move(20, 250)
    CosineButton.clicked.connect(cosine)

    squareBotton.setToolTip("Square")
    squareBotton.move(20, 290)
    squareBotton.clicked.connect(square)

    cubeButton.setToolTip("cube")
    cubeButton.move(200, 290)
    cubeButton.clicked.connect(cube)

    FactButton.setToolTip("Factorial")
    FactButton.move(110, 250)
    FactButton.clicked.connect(factorials)

    cuberootButton.setToolTip("cuberoot")
    cuberootButton.move(110, 290)
    cuberootButton.clicked.connect(cuberoot)

    ClearButton.setToolTip("Clear")
    ClearButton.move(110,130)
    ClearButton.clicked.connect(clear)

 
def addition():
    num1 = float(txtArea1.text())
    num2 = float(txtArea2.text())
    label.setFixedWidth(200)
    label.setText(str(num1) + "+" + str(num2) + "=" + str(num1 + num2))
 
 
def subtraction():
    num1 = float(txtArea1.text())
    num2 = float(txtArea2.text())
    label.setFixedWidth(200)
    label.setText(str(num1) + "-" + str(num2) + "=" + str(num1 - num2))
 
 
def multiplication():
    num1 = float(txtArea1.text())
    num2 = float(txtArea2.text())
    label.setFixedWidth(200)
    label.setText(str(num1) + "*" + str(num2) + "=" + str(num1 * num2))
 
 
def division():
    num1 = float(txtArea1.text())
    num2 = float(txtArea2.text())
    label.setFixedWidth(200)
    label.setText(str(num1) + "/" + str(num2) + "=" + str(num1 / num2))

def percent():
    num1 = float(txtArea1.text())
    label.setFixedWidth(200)
    label.setText(str(num1/100))

def tangent():
    num1 = float(txtArea1.text())
    label.setFixedWidth(200)
    label.setText("tan" + str(num1) + "=" + str(tan(num1)))

def sine():
    num1 = float(txtArea1.text())
    label.setFixedWidth(200)
    label.setText("sin" + str(num1) + "=" + str(sin(num1)))

def cosine():
    num1 = float(txtArea1.text())
    label.setFixedWidth(200)
    label.setText("cos" + str(num1) + "=" + str(cos(num1)))

def factorials():
    num1 = float(txtArea1.text())
    label.setFixedWidth(200)
    label.setText(str(num1) + " !" + " = " + str(factorial(num1))) 

def cuberoot():
    num1 = float(txtArea1.text())
    label.setFixedWidth(200)
    label.setText("∛" + str(num1) + " = " + str(pow(num1, 1/3)))

def square():
    num1 = float(txtArea1.text())
    label.setFixedWidth(200)
    label.setText(str(num1) + "²" + " = " + str(pow(num1,2)))

def squareroot():
    num1 = float(txtArea1.text())
    label.setFixedWidth(200)
    label.setText("√" + str(num1) + " = " + str(sqrt(num1)))

def cube():
    num1 = float(txtArea1.text())
    label.setFixedWidth(200)
    label.setText(str(num1) + "³" + " = " + str(pow(num1,3)))

def clear():
    txtArea1.setText("")
    txtArea2.setText("")
    label.setText("")

if __name__ == "__main__":
    init()
 
app.exec_()

