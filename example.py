

import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import uic




class ExampleApp(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('example.ui', self)
        self.pushButton.clicked.connect(self.on_button_click)
    
    def on_button_click(self):
        self.label.setText("Button Clicked!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    sys.exit(app.exec_())


