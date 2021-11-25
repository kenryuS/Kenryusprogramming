# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from random import random
import decimal

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QCloseEvent

class calculations():
    def montecalro(self):
        a = i = y = x = 1
        progress = 0
        output = ""
        while i < self:
            x = random()
            y = random()
            z = (x**2) + (y**2)
            if z <= 1:
                a += 1
            else:
                pass
            i += 1
            progress += 1
        output = decimal.Decimal(a) / decimal.Decimal(self)
        print(output)
    
    def riemmanzeta(self):
        i = 1
        a = 0
        progress = 0
        output = ""
        while i < self:
            a += (i**2)**-1
            i += 1
            progress += 1
        output = a
        print(output)
    
    def wallis(self):
        i = 1
        progress = 0
        output = 1
        while i <= self:
            output *= (((2*i)/((2*i)-1)))*((2*i)/((2*i)+1))
            i += 1
            progress += 1
        output = 2 * output
        print(output)
    
    def Gregory1(self):
        i = 1
        output = progress = 0
        while i <= self:
            output += ((-1)**(i-1)) * 4/((2*i)-1)
            i += 1
            progress += 1
        print(output)
    
    def Gregory2(self):
        i = 1
        output = progress = 0
        while i <= self:
            output += (-1)**(i-1) * (4/((2*i)*((2*i)+1)*((2*i)+2)))
            i += 1
            progress += 1
        output += 3
        print(output)


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        self.load_ui()
        self.setWindowTitle('Python PI')

    def load_ui(self):
        loader = QUiLoader()
        path = os.fspath(Path(__file__).resolve().parent / "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

        def closeEvent(self, event: QCloseEvent):
            reply = QMessageBox.question(
            self, 
            'Message', 
            'Are you sure you want to quit?',
            QMessageBox.Yes | QMessageBox.No, 
            QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()


if __name__ == "__main__":
    app = QApplication([])
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
