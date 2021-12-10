# main file of the norsevpn - nordvpn gui client

# imports
import logging
import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import qdarkstyle

from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

# own modules and libs
#import vizu.norseVPNGUIWindow as norseVPNGUIWindow
import vizu.mainWindow as mainWindow
import lib.nordvpn as nordvpn
import vizu.trayWindow as trayWindow


##
# @brief    Main Call
# @details  TODO
if __name__ == "__main__":

    logging.basicConfig(filename='norsevpn.log', filemode='w', encoding='utf-8', level=logging.DEBUG)

    """! Initializes the program."""
    app = QtWidgets.QApplication(sys.argv)
    window = mainWindow.mainWindow()

    # set the window style
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))

    tray = trayWindow.trayWindow(QtGui.QIcon("doc/img/logo/NorseVPN_app.svg"), app)
    tray.show()

    window.show()
    sys.exit(app.exec_())