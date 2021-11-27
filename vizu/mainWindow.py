
# imports
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QCheckBox

sys.path.append("..")
from lib.nordvpn import nordvpn as nordvpn
from lib.conf import configManager

# UI file
uiFile = "vizu/norsevpn.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(uiFile)


##
# @brief mainWindow class
class mainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    # private vars
    __isConnected = False




    ##
    # @public
    # @brief    Init
    # @details  Initialization of the class
    #
    # @param    self    Object itself
    def __init__(self):
        # create the instance of the Qt window
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # init timer for periodical calls
        self.__init_timer()

        # button initalization
        self.btn_connect.clicked.connect(self.__btnConnect)
        self.btn_debug.clicked.connect(self.__debug)

        print("Installed: " + str(nordvpn.checkInstall(nordvpn)))
        print("Connected: " + str(nordvpn.isConnected(nordvpn)))

    ##
    # @private
    # @brief    Init Timer
    # @details  This private method is used to initialize the timers for the periodical calls
    def __init_timer(self):
        # QTimer for the GUI updater
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000) # time in ms
        self.timer.timeout.connect(self.__update)
        self.timer.start()


    ##
    # @private
    # @brief    Updater
    # @details  This private method is called periodically by the QTimer
    @QtCore.pyqtSlot()
    def __update(self):
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

    def __debug(self):
        print("Debug")
        print(configManager.updateLocations(configManager))
        print("Debug 2")
        print(configManager.getCities(configManager, "United_States"))
