import os
import random

import sys
from PySide6 import QtCore, QtWidgets, QtGui
from window import MainWidget

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWidget()
    widget.resize(800, 600)
    widget.setStyleSheet("""
           background-color: #262626;
           color: #FFFFFF;
           font-size: 18px;
           """)
    widget.show()

    sys.exit(app.exec())