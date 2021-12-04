
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

class trayWindow(QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QSystemTrayIcon.__init__(self, icon, parent)
        self.action_connect = QAction("Connect", self)
        self.action_disconnect = QAction("Disconnect", self)
        self.action_exit = QAction("Exit", self)

        self.action_connect.triggered.connect(self.__actionConnect)
        self.action_disconnect.triggered.connect(self.__actionDisonnect)
        self.action_exit.triggered.connect(self.__actionExit)

        menu = QMenu()
        menu.addAction(self.action_connect)
        menu.addAction(self.action_disconnect)
        menu.addAction(self.action_exit)

        self.setContextMenu(menu)

    def __actionConnect(self):
        print("Connect")
        nordvpn.connect( nordvpn, 
                             configManager.getConfig(configManager, "selected_country"),
                             configManager.getConfig(configManager, "selected_city"))
        

    def __actionDisonnect(self):
        print("Disconnect")
        nordvpn.disconnect(nordvpn)

    def __actionExit(self):
        print("Exit")

    def exit(self):
        QCoreApplication.exit()