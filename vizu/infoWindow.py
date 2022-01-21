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

# import ui
from vizu.infoUI import Ui_Info
import vizu.vizu_resources

ui_path = os.path.dirname(os.path.abspath(__file__))
##
# @brief Class for the information window
class infoWindow(QWidget):

    ##
    # @public
    # @brief    Init
    # @details  Class gets initialized
    def __init__(self):

        super(infoWindow, self).__init__()
        self.ui = Ui_Info()
        self.ui.setupUi(self)

        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_showLog.clicked.connect(self.__showLog)
        self.ui.textBrowser.clearHistory()

    ## 
    # @public
    # @brief    On Show
    # @details  Interface to show the widget. This is needed
    #           to update the UI/UX depending on the information
    #           before the user sees the window.
    def onShow(self):
        logging.info("Show Info window")
        # clear textbrowser
        self.ui.textBrowser.clearHistory()
        
        htmlFile = QtCore.QFile(":/info.html")
        if htmlFile.open(QtCore.QFile.ReadOnly):
            data = htmlFile.readAll()
            codec = QtCore.QTextCodec.codecForHtml(data)
        htmlText = codec.toUnicode(data)

        # parse the versions and more data into html file
        htmlText = htmlText.replace("{%NORSEVPN_VERSION%}", general.getGitLatestTag() )
        htmlText = htmlText.replace("{%NORSEVPN_GITHASH%}", general.getGitHashShort() )
        htmlText = htmlText.replace("{%NORDVPN_VERSION%}", nordvpn.getVersion(nordvpn) )
        self.ui.textBrowser.setHtml(htmlText)
        self.show()

    ## 
    # @private
    # @brief    Method to open the log file
    def __showLog(self):
        # open the log file
        webbrowser.open("norsevpn.log")