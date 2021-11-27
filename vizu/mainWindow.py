
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

        # QTimer for the GUI updater
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(100) # time in ms
        self.timer.timeout.connect(self.__update)
        self.timer.start()


        print("Installed: " + str(nordvpn.checkInstall(nordvpn)))
        print("Connected: " + str(nordvpn.isConnected(nordvpn)))

    ##
    # @private
    # @brief    Updater
    # @details  This private method is called periodically by the QTimer
    @QtCore.pyqtSlot()
    def __update(self):
        # update the status of the vpn connection
        self.cb_connected.setChecked(nordvpn.isConnected(nordvpn))





