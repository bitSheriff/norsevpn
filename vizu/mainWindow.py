
# imports
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QCheckBox

sys.path.append("..")
from lib.nordvpn import nordvpn as nordvpn


# UI file
uiFile = "vizu/norsevpn.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)

##
# @brief mainWindow class
# 
# @param QtWidgets.QMainWindow
# @param Ui_MainWindow
class mainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    ##
    # @brief    Init
    # @details  TODO
    #
    # @param    self    Object itself
    def __init__(self):
        # create the instance of the Qt window
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.cb_connected.setChecked(nordvpn.isConnected(nordvpn))

        print("Installed: " + str(nordvpn.checkInstall(nordvpn)))
        print("Connected: " + str(nordvpn.isConnected(nordvpn)))


