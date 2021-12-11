import os
import sys
import logging
from PyQt5.QtWidgets import QLabel, QMessageBox, QVBoxLayout, QWidget, QCheckBox
from PyQt5 import QtCore, uic

sys.path.append("..")
from lib.conf import configManager
from lib.nordvpn import nordvpn as nordvpn

# UI file
ui_path = os.path.dirname(os.path.abspath(__file__))
uiFile = os.path.join(ui_path,"info.ui")

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
