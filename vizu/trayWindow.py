
import sys
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QCoreApplication, QObject
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 

sys.path.append("..")
from vizu.mainWindow import mainWindow
from lib.nordvpn import nordvpn as nordvpn
from lib.conf import configManager

##
# @brief Class for the tray application
class trayWindow(QSystemTrayIcon):

    ## 
    # @brief    Init
    # @details  The init is used to build up the 
    #           system tray window and define its content.
    def __init__(self, icon, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)

        # add items for the action
        self.action_connect = QAction("Connect", self)
        self.action_disconnect = QAction("Disconnect", self)
        self.action_exit = QAction("Exit", self)

        # connect the functions to the items
        self.action_connect.triggered.connect(self.__actionConnect)
        self.action_disconnect.triggered.connect(self.__actionDisonnect)
        self.action_exit.triggered.connect(self.__actionExit)

        # create the menu itself and add the items
        menu = QMenu()
        menu.addAction(self.action_connect)
        menu.addAction(self.action_disconnect)
        menu.addAction(self.action_exit)

        self.setContextMenu(menu)

    ##
    # @brief    Action Connect
    # @details  This internal method is executed if the user 
    #           clicks on the connect menu item.
    #           It will connect the vpn to the selected country and city.
    def __actionConnect(self):
        nordvpn.connect( nordvpn, 
                             configManager.getConfig(configManager, "selected_country"),
                             configManager.getConfig(configManager, "selected_city"))
        
    ##
    # @brief    Action Disconnect
    # @details  This internal function is used to handle actions
    #           which are executed if the user chooses "Disconnect" in the tray.
    #           It will disconnect the vpn connection.
    def __actionDisonnect(self):
        nordvpn.disconnect(nordvpn)

    ##
    # @brief    Action Exit
    # @details  This internal function is triggered 
    #           at the menu item "Exit". This will exit the whole application.
    def __actionExit(self):
        nordvpn.disconnect(nordvpn)
        QCoreApplication.exit()

