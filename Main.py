import math
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Buttons():

    def __init__(self, text, results):
        self.btn_class = QPushButton(str(text))
        self.text = text
        self.result = results
        self.btn_class.clicked.connect(lambda: self.btn_handle(self.text))
        self.btn_class.setStyleSheet('QPushButton {background-color: #808080}')

    def btn_handle(self, par):
        if par == '=':
            res = eval(self.result.text())
            self.result.setText(str(res))
        elif par == 'AC':
            self.result.setText('')
        elif par == 'SQ':
            value = float(self.result.text())
            self.result.setText(str(math.sqrt(value)))
        elif par == 'C':
            current_val = self.result.text()
            self.result.setText(current_val[:-1])
        else:
            current_value = self.result.text()
            new_value = current_value + str(par)
            self.result.setText(new_value)


class Application(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.createCalc()

    def createCalc(self):

        grid_layout = QGridLayout()
        result_label = QLineEdit()
        buttons = ['AC', 'C', 'SQ', '/',
                   7, 8, 9, '*',
                   4, 5, 6, '-',
                   1, 2, 3, '+',
                   0, '.', '=']
        rows = 1
        cols = 0
        grid_layout.addWidget(result_label, 0, 0, 1, 4)
        for button in buttons:
            if cols > 3:
                cols = 0
                rows += 1
            btn_object = Buttons(button, result_label)
            if button == 0:
                grid_layout.addWidget(btn_object.btn_class, rows, cols, 1, 2)
                cols += 1
            else:
                grid_layout.addWidget(btn_object.btn_class, rows, cols, 1, 1)
            cols += 1
        self.setLayout(grid_layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec())
