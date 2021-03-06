# imports
import logging
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMessageBox, QTreeWidgetItem, QWidget, QInputDialog, QLineEdit, QFileDialog, QCheckBox

sys.path.append("..")
from lib.nordvpn import nordvpn as nordvpn
from lib.conf import configManager
from vizu.configWindow import configWindow
from vizu.infoWindow import infoWindow
import lib.general as general
import vizu.vizu_resources


# import ui
from vizu.mainUI import Ui_NorseVPN

##
# @brief mainWindow class
class mainWindow(QtWidgets.QMainWindow):

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
        #QtWidgets.QMainWindow.__init__(self)
        #Ui_MainWindow.__init__(self)
        self.configWidget = configWindow()
        self.infoWidget = infoWindow()

        super(mainWindow, self).__init__()
        self.ui = Ui_NorseVPN()
        self.ui.setupUi(self)

        # init timer for periodical calls
        self.__init_timer()
        self.__init_textBrowser()

        # button initialization
        self.ui.btn_debug.clicked.connect(self.__debug)
        self.ui.btn_config.clicked.connect(self.__btnConfig)
        self.ui.btn_connect.clicked.connect(self.__btnConnect)
        self.ui.btn_shuffle.clicked.connect(self.__randomLocation)
        self.ui.btn_info.clicked.connect(self.__showInfoWindow)
        self.ui.tree_location.itemClicked.connect(self.__locationSelection)

        # initialize system config directory if it does not exist
        configManager.initializeConfig(configManager)

        # load tree view
        configManager.updateLocations(configManager)    # update the locations inside the json
        self.__fillLocationTree()

        # set the version to the label
        self.ui.label_version.setText("Version " + general.getGitLatestTag())

        logging.info("Installed: " + str(nordvpn.checkInstall(nordvpn)))
        logging.info("Connected: " + str(nordvpn.isConnected(nordvpn)))

        # show an error window if nordvpn is not installed on the system
        if(not nordvpn.checkInstall(nordvpn)):
            self.__showErrorBox()

        # deactivate debugging functions
        self.ui.btn_debug.setVisible(False)

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

        self.cooldownTimer = QtCore.QTimer(self)
        self.cooldownTimer.timeout.connect(self.__cooldownEnd)
        self.cooldownTimer.setInterval(3000) # time in ms
        self.cooldownTimer.setSingleShot(True)  # timer runs only once if startet

    def __init_textBrowser(self):
        self.ui.textBrowser.setAcceptRichText(True)

    ##
    # @private
    # @brief    Updater
    # @details  This private method is called periodically by the QTimer
    @QtCore.pyqtSlot()
    def __update(self):
        # update the private variable
        self.__isConnected = nordvpn.isConnected(nordvpn)

        # update the checkbox
        self.ui.cb_connected.setChecked(self.__isConnected)
        # update the text on the button depending on the connection state
        if self.__isConnected:
            self.ui.btn_connect.setText("Disconnect")
        else:
            self.ui.btn_connect.setText("Connect")

        # disable the main window if the config window is currently open
        if self.configWidget.isVisible():
            self.setDisabled(True)
        else:
            self.setDisabled(False)

        # disable changes in the settings if currently connected
        self.configWidget.setDisableChanges(self.__isConnected)

        # update the vpn status from console
        self.__updateTextBrowser()

    ##
    # @private
    # @overload closeEvent
    # @brief    Close Window
    # @details  Internal method to close the widget.
    #           If the window should close, the vpn connection gets disconnected.
    def closeEvent(self, event):
        # show message to get if the user wants to save
        reply = QMessageBox.question(
            self, "Message",
            "Are you sure you want to quit? VPN will disconnect.",
            QMessageBox.Close | QMessageBox.Cancel,
            QMessageBox.Cancel)

        # get the user input
        if reply == QMessageBox.Close:
            nordvpn.disconnect(nordvpn)     # disconnect the vpn
            # close all sub windows and this window
            if self.configWidget.isVisible():
                self.configWidget.close()
            if self.infoWidget.isVisible():
                self.infoWidget.close()
            self.close()
        else:
            event.ignore()
            pass

    ##
    # @private
    # @brief    Connect button click event
    # @details  This private method is called if the user clicks on the connect/disconnect buttin
    #           depending on the vpn state the nordvpn module is called to connect or disconnect
    def __btnConnect(self):
        logging.info("Btn: Connect")
        # call interface depending on the vpn status
        if self.__isConnected:
            nordvpn.disconnect(nordvpn)
        else:
            nordvpn.connect( nordvpn, 
                             configManager.getConfig(configManager, "selected_country"),
                             configManager.getConfig(configManager, "selected_city"))
            self.__cooldownStart()

    ##
    # @private
    # @brief    Method to open the config window
    def __btnConfig(self):
        # disable the main window and show the config window
        self.setDisabled(True)
        self.configWidget.onShow()

    def __debug(self):
        logging.info("Debug")
        logging.info(configManager.updateLocations(configManager))
    
    ##
    # @private
    # @brief    Method to update the live status window
    # @details  This internal method is periodically called to
    #           to update the status of the vpn connection.
    #           It replaces some chars in the string to display it properly.
    def __updateTextBrowser(self):
        if(nordvpn.checkInstall(nordvpn)):
            htmlText = nordvpn.getStatus(nordvpn)
            htmlText = htmlText.replace("\t", "")
            htmlText = htmlText.replace("-", "")
            htmlText = htmlText.replace("\n", "<br>")
        else:
            htmlText = "nordVPN is not installed"
        self.ui.textBrowser.clearHistory()
        self.ui.textBrowser.setHtml(htmlText)

    def __fillLocationTree(self):
        data = configManager.getLocationDict(configManager)
        items = []
        for key, values in data.items():
            item = QTreeWidgetItem([key])
            for value in values:
                # create for every city a iterateable to add it as a child (needed by Qt)
                for city in value:
                    cityEntry = []
                    cityEntry.append(city)
                    child = QTreeWidgetItem(cityEntry)
                    item.addChild(child)
            items.append(item)
        self.ui.tree_location.insertTopLevelItems(0, items)

    def __locationSelection(self):
        item = self.ui.tree_location.currentItem()
        par = item.parent()

        if type(par) is not QTreeWidgetItem:
            cnt = item.text(0)
            cty = ""
        else:
            cnt = par.text(0)
            cty = item.text(0)
        configManager.setConfig(configManager, "selected_country",cnt)
        configManager.setConfig(configManager, "selected_city",cty)
        if self.__isConnected:
            self.__cooldownStart()
            # vpn is currently connected, change location of the fly
            nordvpn.connect( nordvpn, 
                             cnt,
                             cty)


    def __cooldownStart(self):
        self.cooldownTimer.start()

        # disable interactions
        self.ui.tree_location.setDisabled(True)
        self.ui.btn_connect.setDisabled(True)
        self.ui.btn_shuffle.setDisabled(True)

    def __cooldownEnd(self):
        # Enable all interactions again
        self.ui.tree_location.setDisabled(False)
        self.ui.btn_connect.setDisabled(False)
        self.ui.btn_shuffle.setDisabled(False)

    def __randomLocation(self):
        logging.info("Btn: Random Location")
        cnt, cty = configManager.getRandomLocation(configManager)
        nordvpn.connect( nordvpn, 
                         str(cnt),
                         str((cty[0])[0]))

    def __showInfoWindow(self):
        self.infoWidget.onShow()

    def __showErrorBox(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("nordvpn is not installed")
        msg.setInformativeText("Please visit the official github repository for further informations")
        msg.setWindowTitle("norseVPN Error")
        msg.setStandardButtons(QMessageBox.Ignore)
        msg.exec_()
