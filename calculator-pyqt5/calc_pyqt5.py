#!/usr/bin/python3
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore
import sys
import qdarkstyle

from main5 import Ui_MainWindow


class MyApp(QMainWindow):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.button_0.clicked.connect(self.put0)
        self.ui.button_1.clicked.connect(self.put1)
        self.ui.button_2.clicked.connect(self.put2)
        self.ui.button_3.clicked.connect(self.put3)
        self.ui.button_4.clicked.connect(self.put4)
        self.ui.button_5.clicked.connect(self.put5)
        self.ui.button_6.clicked.connect(self.put6)
        self.ui.button_7.clicked.connect(self.put7)
        self.ui.button_8.clicked.connect(self.put8)
        self.ui.button_9.clicked.connect(self.put9)
        self.ui.decimal.clicked.connect(self.put_dot)
        self.ui.clear_button.clicked.connect(self.clear)
        self.ui.reset_button.clicked.connect(self.reset)
        self.ui.add.clicked.connect(self.put_add)
        self.ui.minus.clicked.connect(self.put_sub)
        self.ui.divide.clicked.connect(self.put_divide)
        self.ui.multiply.clicked.connect(self.put_mul)
        self.ui.remainder.clicked.connect(self.put_mod)
        self.ui.square_root.clicked.connect(self.put_root)
        self.ui.parenthesis_close.clicked.connect(self.parenthesis_close)
        self.ui.parenthesis_open.clicked.connect(self.parenthesis_open)
        self.ui.equals.clicked.connect(self.render_answer)

    def put_add(self):
        self.put_text('+')

    def put_sub(self):
        self.put_text('-')

    def put_mul(self):
        self.put_text('*')

    def put_divide(self):
        self.put_text('/')

    def put_mod(self):
        self.put_text('%')

    def put_root(self):
        self.put_text('√')

    def parenthesis_open(self):
        self.put_text('(')

    def parenthesis_close(self):
        self.put_text(')')

    def reset(self):
        self.ui.lineEdit.clear()
        self.ui.output_window.clear()

    def clear(self):
        self.ui.lineEdit.clear()

    def put0(self):
        self.put_text('0')

    def put1(self):
        self.put_text('1')

    def put2(self):
        self.put_text('2')

    def put3(self):
        self.put_text('3')

    def put4(self):
        self.put_text('4')

    def put5(self):
        self.put_text('5')

    def put6(self):
        self.put_text('6')

    def put7(self):
        self.put_text('7')

    def put8(self):
        self.put_text('8')

    def put9(self):
        self.put_text('9')

    def put_dot(self):
        self.put_text('.')

    def put_text(self, txt):
        original = self.ui.lineEdit.text()
        new = original+txt
        self.ui.lineEdit.setText(new)

    def clicked(self):
        self.statusBar().showMessage('Hello there !')

    def keyPressEvent(self, e):
        key = e.key()
        if key in range(37, 62):
            original = self.ui.lineEdit.text()
            self.ui.lineEdit.setText(str(original+chr(key)))
        elif key == QtCore.Qt.Key_Return or key == QtCore.Qt.Key_Enter:
            self.render_answer()
        elif key == QtCore.Qt.Key_Escape:
            self.reset()
        elif key == QtCore.Qt.Key_Backspace:
            self.backspace_line_edit()

    def backspace_line_edit(self):
        init = self.ui.lineEdit.text()
        self.ui.lineEdit.setText(init[:-1])

    def render_answer(self):
        input_equation = self.ui.lineEdit.text()
        init_output = self.ui.output_window.toPlainText()

        try:
            answer = eval(input_equation)
            self.ui.output_window.setText(input_equation+" = "+str(answer)+"\n"+init_output)

        except Exception:
            self.ui.statusbar.showMessage("Math Error!")

        self.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MyApp()
    dark_style = qdarkstyle.load_stylesheet_pyqt5()
    myapp.setStyleSheet(dark_style)
    myapp.show()
    sys.exit(app.exec_())
