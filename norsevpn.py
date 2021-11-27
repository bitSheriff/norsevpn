# main file of the norsevpn - nordvpn gui client

# imports
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog

# own modules and libs
#import vizu.norseVPNGUIWindow as norseVPNGUIWindow
import vizu.mainWindow as mainWindow
import lib.nordvpn as nordvpn


##
# @brief    Main Call
# @details  TODO
if __name__ == "__main__":
    """! Initializes the program."""
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow.mainWindow()
    window.show()
    sys.exit(app.exec_())