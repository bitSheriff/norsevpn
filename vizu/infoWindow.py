import os
import sys
import logging
import webbrowser
from PyQt5.QtWidgets import QLabel, QMessageBox, QVBoxLayout, QWidget, QCheckBox
from PyQt5 import QtCore, uic

sys.path.append("..")
from lib.conf import configManager
from lib.nordvpn import nordvpn as nordvpn
import lib.general as general

# UI file
ui_path = os.path.dirname(os.path.abspath(__file__))
uiFile = os.path.join(ui_path,"info.ui")

htmlFile = os.path.join(ui_path,"info.html")

##
# @brief Class for the information window
class infoWindow(QWidget):

    ##
    # @public
    # @brief    Init
    # @details  Class gets initialized
    def __init__(self):
        super(infoWindow, self).__init__()
        uic.loadUi(uiFile, self)

        self.btn_close.clicked.connect(self.close)
        self.btn_showLog.clicked.connect(self.__showLog)
        self.textBrowser.clearHistory()

    ## 
    # @public
    # @brief    On Show
    # @details  Interface to show the widget. This is needed
    #           to update the UI/UX depending on the information
    #           before the user sees the window.
    def onShow(self):
        logging.info("Show Info window")
        # clear textbrowser
        self.textBrowser.clearHistory()
        with open(htmlFile, 'r') as file:
            htmlText = file.read()
        # parse the versions and more data into html file
        htmlText = htmlText.replace("{%NORSEVPN_VERSION%}", general.getGitLatestTag() )
        htmlText = htmlText.replace("{%NORSEVPN_GITHASH%}", general.getGitHashShort() )
        htmlText = htmlText.replace("{%NORDVPN_VERSION%}", nordvpn.getVersion(nordvpn) )
        self.textBrowser.setHtml(htmlText)
        self.show()

    ## 
    # @private
    # @brief    Method to open the log file
    def __showLog(self):
        # open the log file
        webbrowser.open("norsevpn.log")