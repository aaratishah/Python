import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
widget = QWidget()
label = QLabel("Result:",widget)

btnAdd = QPushButton("+", widget)
btnSubtract = QPushButton("-", widget)
btnMultiply = QPushButton("*", widget)
btnDivide = QPushButton("/", widget)
btnPercent = QPushButton("%", widget)

txtArea1 = QLineEdit("", widget)
txtArea2 = QLineEdit("", widget)

def init():
    widget.resize(300, 300)
    widget.move(300, 300)
    widget.setWindowTitle('Calculator')
    widget.show()
 
    txtArea1.move(20, 30)
    txtArea1.show()
    txtArea2.move(20, 80)
    txtArea2.show()
 
    label.setText("")
    label.move(20, 110)
    label.show()
 
    btnAdd.setToolTip("Addition")
    btnAdd.move(20, 160)
    btnAdd.clicked.connect(addition)
    btnAdd.show()
 
    btnSubtract.setToolTip("Subtraction")
    btnSubtract.move(110, 160)
    btnSubtract.clicked.connect(subtraction)
    btnSubtract.show()
 
    btnDivide.setToolTip("Division")
    btnDivide.move(20, 210)
    btnDivide.clicked.connect(division)
    btnDivide.show()
 
    btnMultiply.setToolTip("Multiplication")
    btnMultiply.move(110, 210)
    btnMultiply.clicked.connect(multiplication)
    btnMultiply.show()

    btnPercent.setToolTip("Percentage")
    btnPercent.move(75,190)
    btnPercent.clicked.connect(percent)

 
 
def addition():
    num1 = int(txtArea1.text())
    num2 = int(txtArea2.text())
    label.setFixedWidth(200)
    label.setText(str(num1 + num2))
 
 
def subtraction():
    num1 = int(txtArea1.text())
    num2 = int(txtArea2.text())
    label.setFixedWidth(200)
    label.setText(str(num1 - num2))
 
 
def multiplication():
    num1 = int(txtArea1.text())
    num2 = int(txtArea2.text())
    label.setFixedWidth(200)
    label.setText(str(num1 * num2))
 
 
def division():
    num1 = int(txtArea1.text())
    num2 = int(txtArea2.text())
    label.setFixedWidth(200)
    label.setText(str(num1 / num2))

def percent():
    num1 = int(txtArea1.text())
    
    label.setFixedWidth(200)
    label.setText(str(num1/100))

 
 
if __name__ == "__main__":
    init()
 
app.exec_()

