import os
import sys
import logging
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

        # inernal flags and vars
        self.isDisabled = True

        # simulate toggleSwitch like handling
        self.slid_firewall.sliderPressed.connect(lambda: self.__toggleSlider(slid=self.slid_firewall))
        self.slid_killSwitch.sliderPressed.connect(lambda: self.__toggleSlider(slid=self.slid_killSwitch))
        self.slid_cyberSec.sliderPressed.connect(lambda: self.__toggleSlider(slid=self.slid_cyberSec))
        self.slid_obfuscate.sliderPressed.connect(lambda: self.__toggleSlider(slid=self.slid_obfuscate))
        self.slid_notify.sliderPressed.connect(lambda: self.__toggleSlider(slid=self.slid_notify))
        self.slid_autoConnect.sliderPressed.connect(lambda: self.__toggleSlider(slid=self.slid_autoConnect))
        self.slid_ipv6.sliderPressed.connect(lambda: self.__toggleSlider(slid=self.slid_ipv6))
        self.slid_dns.sliderPressed.connect(lambda: self.__toggleSlider(slid=self.slid_dns))
        # button setup
        self.btn_close.clicked.connect(self.__closeBtn)
        self.btn_save.clicked.connect(self.saveConfig)
        # combobox setup
        self.cb_protocol.addItems(["TCP", "UDP"])
        self.cb_technology.addItems(["OpenVPN", "NordLynx"])

    ## 
    # @public
    # @brief    On Show
    # @details  Interface to show the widget. This is needed
    #           to update the UI/UX depending on the configuration
    #           before the user sees the window.
    def onShow(self):
        logging.info("Show Config window")
        self.loadConfig()
        self.show()

    ##
    # @public 
    # @brief    Load Configuration
    # @details  This interface is ued to load the configuration
    #           from the config file and show it to the user
    #           (configFile -> UI)
    def loadConfig(self):
        logging.info("Load Config")
        self.slid_firewall.setValue(configManager.getConfig(configManager, "firewall"))
        self.slid_killSwitch.setValue(configManager.getConfig(configManager, "killswitch"))
        self.slid_cyberSec.setValue(configManager.getConfig(configManager, "cybersec"))
        self.slid_obfuscate.setValue(configManager.getConfig(configManager, "obfuscate"))
        self.slid_notify.setValue(configManager.getConfig(configManager, "notify"))
        self.slid_autoConnect.setValue(configManager.getConfig(configManager, "autoconnect"))
        self.slid_ipv6.setValue(configManager.getConfig(configManager, "ipv6"))
        self.slid_dns.setValue(configManager.getConfig(configManager, "dns"))
        # set the selected item in the comboboxes
        index_protocol = self.cb_protocol.findText(configManager.getConfig(configManager, "protocol"), QtCore.Qt.MatchFixedString)
        if index_protocol >= 0:
            self.cb_protocol.setCurrentIndex(index_protocol)
        index_tech = self.cb_protocol.findText(configManager.getConfig(configManager, "technology"), QtCore.Qt.MatchFixedString)
        if index_tech >= 0:
            self.cb_protocol.setCurrentIndex(index_tech)


        return

    ##
    # @public 
    # @brief    Save Configuration
    # @details  This interface is ued to save the configuration
    #           from the UI to the config file
    #           (UI -> configFile)
    def saveConfig(self):
        logging.info("Save Config")
        configManager.setConfig( configManager,
                                 "firewall",
                                 self.__getSetting(self.slid_firewall.value()) )
        configManager.setConfig( configManager,
                                 "killswitch",
                                 self.__getSetting(self.slid_killSwitch.value()) )
        configManager.setConfig( configManager,
                                 "cybersec",
                                 self.__getSetting(self.slid_cyberSec.value()) )
        configManager.setConfig( configManager,
                                 "obfuscate",
                                 self.__getSetting(self.slid_obfuscate.value()) )
        configManager.setConfig( configManager,
                                 "notify",
                                 self.__getSetting(self.slid_notify.value()) )
        configManager.setConfig( configManager,
                                 "autoconnect",
                                 self.__getSetting(self.slid_autoConnect.value()) )
        configManager.setConfig( configManager,
                                 "ipv6",
                                 self.__getSetting(self.slid_ipv6.value()) )
        configManager.setConfig( configManager,
                                 "dns",
                                 self.__getSetting(self.slid_dns.value()) )
        configManager.setConfig( configManager,
                                 "protocol",
                                 self.cb_protocol.currentText())
        configManager.setConfig( configManager,
                                 "technology",
                                 self.cb_technology.currentText())
        return

    ##
    # @private
    # @overload closeEvent
    # @brief    Close Window
    # @details  Internal method to close the widget.
    #           The user can decide if the configuration should be saved, just closed
    #           or return to the config window.
    def closeEvent(self, event):
        # if settings are nor allowed because vpn is connected, exit window without qmessagebox
        if self.isDisabled:
            self.close
            return

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
            event.ignore()
            pass

    def __closeBtn(self):
        self.close()

    ##
    # @private
    # @brief    Get Value from string
    def __getSetting(self, sliderVal):
        if sliderVal > 0:
            return True
        else:
            return False

    ##
    # @private
    # @brief    Toggle Slider
    # @details  This private function is used to simulate a toggeling action.
    #           So it switches between 0 and 1.
    def __toggleSlider(self, slid):
        if slid.value() == 0:
            slid.setValue(1)
        else:
            slid.setValue(0)
    ##
    # @public
    # @brief    Set Disable Changes
    # @details  This interface disables and enables changes on the settings page.
    #           It is needed to avoid changes setting during a vpn connection 
    #           because they would not take affect until a new connection.
    #
    # @param    self    Object itself
    # @param    disabled    Boolish value if changes should be disabled
    def setDisableChanges(self, disabled):
        self.isDisabled  = disabled
        self.slid_firewall.setDisabled(disabled)
        self.slid_killSwitch.setDisabled(disabled)
        self.slid_cyberSec.setDisabled(disabled)
        self.slid_obfuscate.setDisabled(disabled)
        self.slid_notify.setDisabled(disabled)
        self.slid_autoConnect.setDisabled(disabled)
        self.slid_ipv6.setDisabled(disabled)
        self.slid_dns.setDisabled(disabled)

        self.cb_protocol.setDisabled(disabled)
        self.cb_technology.setDisabled(disabled)

        self.btn_save.setDisabled(disabled)
