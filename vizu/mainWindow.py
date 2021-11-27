
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

    # private vars
    __isConnected = False

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
        self.timer.setInterval(1000) # time in ms
        self.timer.timeout.connect(self.update)
        self.timer.start()

        # button initalization
        self.btn_connect.clicked.connect(self.__btnConnect)

        print("Installed: " + str(nordvpn.checkInstall(nordvpn)))
        print("Connected: " + str(nordvpn.isConnected(nordvpn)))

    ##
    # @private
    # @brief    Updater
    # @details  This private method is called periodically by the QTimer
    @QtCore.pyqtSlot()
    def update(self):
        # update the private variable
        self.__isConnected = nordvpn.isConnected(nordvpn)

        # update the checkbox
        self.cb_connected.setChecked(self.__isConnected)
        # update the text on the button depending on the connection state
        if self.__isConnected:
            self.btn_connect.setText("Disconnect")
        else:
            self.btn_connect.setText("Connect")

    ##
    # @private
    # @brief    Connect button click event
    # @details  This private method is called if the user clicks on the connect/disconnect buttin
    #           depending on the vpn state the nordvpn module is called to connect or disconnect
    def __btnConnect(self):
        # call interface depending on the vpn status
        if self.__isConnected:
            nordvpn.disconnect(nordvpn)
        else:
            nordvpn.connect(nordvpn)


