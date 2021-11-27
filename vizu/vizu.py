
# imports
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog

# UI file
Ui_MainWindow, QtBaseClass = uic.loadUiType("norsevpn.ui")

##
# @brief norseVPNGUIWindow class
# 
# @param QtWidgets.QMainWindow
# @param Ui_MainWindow
class norseVPNGUIWindow(QtWidgets.QMainWindow, Ui_MainWindow):


        def __init__(self):
            QtWidgets.QMainWindow.__init__(self)
            Ui_MainWindow.__init__(self)