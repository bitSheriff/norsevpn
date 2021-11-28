
import os
import sys
from PyQt5.QtWidgets import QLabel, QMessageBox, QVBoxLayout, QWidget, QCheckBox
from PyQt5 import QtCore, uic

sys.path.append("..")
from lib.conf import configManager


# UI file
ui_path = os.path.dirname(os.path.abspath(__file__))
uiFile = os.path.join(ui_path,"config.ui")

##
# @brief Class for the Configuration Window
class configWindow(QWidget):

    ##
    # @public
    # @brief    Init
    # @details  Class gets initialized
    def __init__(self):
        super(configWindow, self).__init__()
        uic.loadUi(uiFile, self)

        self.btn_close.clicked.connect(self.__btn_close)
        self.btn_save.clicked.connect(self.saveConfig)

    ## 
    # @public
    # @brief    On Show
    # @details  Interface to show the widget. This is needed
    #           to update the UI/UX depending on the configuration
    #           before the user sees the window.
    def onShow(self):
        print("Show")
        self.loadConfig()
        self.show()

    ##
    # @public 
    # @brief    Load Configuration
    # @details  This interface is ued to load the configuration
    #           from the config file and show it to the user
    #           (configFile -> UI)
    def loadConfig(self):
        print("Load Config")
        return

    ##
    # @public 
    # @brief    Save Configuration
    # @details  This interface is ued to save the configuration
    #           from the UI to the config file
    #           (UI -> configFile)
    def saveConfig(self):
        print("Save Config")
        return

    ##
    # @private
    # @brief    Close Window
    # @details  Internal method to close the widget.
    #           The user can decide if the configuration should be saved, just closed
    #           or return to the config window.
    def __btn_close(self, event):
        # show message to get if the user wants to save
        reply = QMessageBox.question(
            self, "Message",
            "Are you sure you want to quit? Any unsaved work will be lost.",
            QMessageBox.Save | QMessageBox.Close | QMessageBox.Cancel,
            QMessageBox.Save)

        # get the user input
        if reply == QMessageBox.Close:
            self.close()
        elif reply == QMessageBox.Save:
            self.saveConfig()
            self.close
        else:
            pass
