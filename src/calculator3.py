import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
import re

from_class = uic.loadUiType("calculator3.ui")[0]
#QMainWindow
class WindowClass(QDialog, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("calculator")
        self.result = ['0']
        self.last_state = 0
        self.number = []
        self.operator = []
        self.token = []
        self.lineEdit.setText(''.join(self.result))

        self.zero.clicked.connect(lambda: self.numClicked('0'))
        self.one.clicked.connect(lambda: self.numClicked('1'))
        self.two.clicked.connect(lambda: self.numClicked('2'))
        self.three.clicked.connect(lambda: self.numClicked('3'))
        self.four.clicked.connect(lambda: self.numClicked('4'))
        self.five.clicked.connect(lambda: self.numClicked('5'))
        self.six.clicked.connect(lambda: self.numClicked('6'))
        self.seven.clicked.connect(lambda: self.numClicked('7'))
        self.eight.clicked.connect(lambda: self.numClicked('8'))
        self.nine.clicked.connect(lambda: self.numClicked('9'))
        self.addition.clicked.connect(lambda: self.operatorClicked('+'))
        self.substraction.clicked.connect(lambda: self.operatorClicked('-'))
        self.multiplication.clicked.connect(lambda: self.operatorClicked('*'))
        self.division.clicked.connect(lambda: self.operatorClicked('/'))
        self.equal.clicked.connect(self.equalClicked)
        self.decimal.clicked.connect(self.decimalClicked)
        self.sign.clicked.connect(self.signClicked)
        self.clear.clicked.connect(self.clearClicked)
        self.allclear.clicked.connect(self.allclearClicked)
 #           if len(self.result)== 1 and self.result[0] == '0':
  #              if num == '0':
   #                 pass
    #            else:
     #               self.result[0] = num
      #              self.last_state = 0

#                 if '.' in ''.join(self.result[len(''.join(self.token)):]):
#                    self.result.append(num)
#                    self.last_state = 0
#                else:
#                    pass     

    def numClicked(self, num):
        if self.last_state == 0:
            if len(self.result) == 1 and self.result[0] == '0':
                if num == '0':
                    pass
                else:
                    self.result[-1] = num
                    self.last_state = 0
            elif self.operator and len(self.result[len(''.join(self.token)):])==1 and self.result[len(''.join(self.token))]=='0':
                if num == '0':
                    pass
                else:
                    self.result[-1] = num
                    self.last_state = 0
            else:
                self.result.append(num)
                self.last_state = 0 
        else:
            self.result.append(num)
            self.last_state = 0
        self.lineEdit.setText(''.join(self.result))


    def operatorClicked(self, op):
        if self.last_state == 0:
            if self.operator:
                pass
            else:
                self.operator.append(op)
                self.number.append(''.join(self.result))
                self.token.append(self.number[-1])
                self.token.append(self.operator[-1])
                self.result.append(op)
                self.last_state = 1
        elif self.last_state == 1:
            self.operator[-1] = op
            self.token[-1] = self.operator[-1]
            self.result[-1] = op
            self.last_state = 1
        elif self.last_state == 2:
            pass
        elif self.last_state == 3:
            pass
        elif self.last_state == 4:
            self.operator.append(op)
            self.number.append(''.join(self.result))
            self.token.append(self.number[-1])
            self.token.append(self.operator[-1])
            self.result.append(op)
            self.last_state = 1
        self.lineEdit.setText(''.join(self.result))


    def signClicked(self):
        if self.last_state == 0:
            if len(self.result) == 1 and self.result[0] == '0':
                self.result[0] = '-'
                self.last_state = 2
        elif self.last_state == 1:
            self.result.append('-')
            self.last_state = 2
        elif self.last_state == 2:
            if self.result[-1] == '-':
                del self.result[-1]
                if len(self.result):
                    self.last_state = 1
                else:
                    self.result.append('0')
                    self.last_state = 0
                
            else:
                self.result.append('-')
                self.last_state = 2
        elif self.last_state == 3 :
            pass
        elif self.last_state == 4 :
            pass
        self.lineEdit.setText(''.join(self.result))


    def decimalClicked(self):
        if self.last_state == 0:
            if len(self.number):
                if '.' in self.result[len(self.number[0]):]:
                    pass
                else:
                    self.result.append('.')
                    self.last_state = 3
            else:
                if '.' in self.result:
                    pass
                else:
                    self.result.append('.')
                    self.last_state = 3
        elif self.last_state == 1:
            pass
        elif self.last_state == 2:
            pass
        elif self.last_state == 3:
            pass
        elif self.last_state == 4:
            pass
        self.lineEdit.setText(''.join(self.result))


    def equalClicked(self):
        if self.last_state == 0:
            if self.operator:
                second_start = len(''.join(self.token))
                self.number.append(''.join(self.result[second_start:]))
                self.token.append(self.number[-1])
                if self.operator[0] == '*':
                    self.result = list(str(float(self.number[0])*float(self.number[1])))
                elif self.operator[0] == '/':
                    if float(self.number[1]) == 0.0:
                        self.result = ['0']
                    else:
                        self.result = list(str(float(self.number[0]) / float(self.number[1])))
                elif self.operator[0] == '+':
                    self.result = list(str(float(self.number[0])+float(self.number[1])))
                elif self.operator[0] == '-':
                    self.result = list(str(float(self.number[0])-float(self.number[1])))
                self.number = []
                self.token = []
                self.operator = []
                self.last_state = 4
            else:
                pass
        elif self.last_state == 1:
            pass
        elif self.last_state == 2:
            pass
        elif self.last_state == 3:
            pass
        elif self.last_state ==4:
            pass
        self.lineEdit.setText(''.join(self.result))
#                if self.token:
#                    if self.token[-1] in '*/+-':
#                        self.last_state =1
#                    else:
#                        self.last_state =0
#                else:
#                   self.last_state = 0
    def clearClicked(self):
        if len(self.result)>0:
            if len(self.result) > len(''.join(self.token)):
                self.result = self.result[:len(''.join(self.token))]
                if self.token:
                    self.last_state = 1
                else:
                    self.last_state = 0
            elif len(self.result) == len(''.join(self.token)):
                element = self.token.pop()
                self.result = self.result[:len(''.join(self.token))]
                if element == self.number[-1]:
                    self.number.pop()
                    self.last_state = 1
                elif element == self.operator[-1]:
                    self.operator.pop()
                    self.number.pop()
                    self.token.pop()
                    self.last_state = 0
            
            if len(self.result) == 0:
                self.result.append('0')
                self.last_state = 0
            else:
                pass
        self.lineEdit.setText(''.join(self.result))
   

    def allclearClicked(self):
        self.result = ['0']
        self.last_state = 0
        self.number = []
        self.operator = []
        self.token = []    

        self.lineEdit.setText(''.join(self.result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = WindowClass()
    myWindows.show()
    sys.exit(app.exec())