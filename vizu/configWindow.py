import os
import sys
import logging
from PyQt5.QtWidgets import QLabel, QMessageBox, QVBoxLayout, QWidget, QCheckBox
from PyQt5 import QtCore, uic, QtGui

sys.path.append("..")
from lib.conf import configManager


# import ui
from vizu.configUI import Ui_Configuration

##
# @brief Class for the Configuration Window
class configWindow(QWidget):

    ##
    # @public
    # @brief    Init
    # @details  Class gets initialized
    def __init__(self):

        super(configWindow, self).__init__()
        self.ui = Ui_Configuration()
        self.ui.setupUi(self)

        # inernal flags and vars
        self.isDisabled = True

        # simulate toggleSwitch like handling
        self.ui.slid_firewall.sliderPressed.connect(lambda: self.__toggleSlider(slid=self.ui.slid_firewall))
        self.ui.slid_killSwitch.sliderPressed.connect(lambda: self.__toggleSlider(slid=self.uislid_killSwitch))
        self.ui.slid_cyberSec.sliderPressed.connect(lambda: self.__toggleSlider(slid=self.ui.slid_cyberSec))
        self.ui.slid_obfuscate.sliderPressed.connect(lambda: self.__toggleSlider(slid=self.ui.slid_obfuscate))
        self.ui.slid_notify.sliderPressed.connect(lambda: self.__toggleSlider(slid=self.ui.slid_notify))
        self.ui.slid_autoConnect.sliderPressed.connect(lambda: self.__toggleSlider(slid=self.ui.slid_autoConnect))
        self.ui.slid_ipv6.sliderPressed.connect(lambda: self.__toggleSlider(slid=self.ui.slid_ipv6))
        self.ui.slid_dns.sliderPressed.connect(lambda: self.__toggleSlider(slid=self.ui.slid_dns))
        # button setup
        self.ui.btn_close.clicked.connect(self.__closeBtn)
        self.ui.btn_save.clicked.connect(self.saveConfig)
        # combobox setup
        self.ui.cb_protocol.addItems(["TCP", "UDP"])
        self.ui.cb_technology.addItems(["OpenVPN", "NordLynx"])
        # dns setup
        self.ui.line_dns.returnPressed.connect(self.__enterDNS)
        self.ui.dns_delete.clicked.connect(self.__removeDNS)

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

    def __loadDNS(self):
        dnsIsActive = configManager.getConfig(configManager, "dns")
        # disable line edit and list view if custom dns is disabled
        self.ui.line_dns.setDisabled(not dnsIsActive)
        self.ui.list_dns.setDisabled(not dnsIsActive)
        self.ui.dns_delete.setDisabled(not dnsIsActive)

        # set the server list
        servers = configManager.getDNSServer(configManager)
        self.ui.list_dns.clear() # clear whole list before updating it
        self.ui.list_dns.addItems(servers)
        return

    def __loadWhitelist(self):
        return


    ##
    # @public 
    # @brief    Load Configuration
    # @details  This interface is ued to load the configuration
    #           from the config file and show it to the user
    #           (configFile -> UI)
    def loadConfig(self):
        logging.info("Load Config")
        self.ui.slid_firewall.setValue(configManager.getConfig(configManager, "firewall"))
        self.ui.slid_killSwitch.setValue(configManager.getConfig(configManager, "killswitch"))
        self.ui.slid_cyberSec.setValue(configManager.getConfig(configManager, "cybersec"))
        self.ui.slid_obfuscate.setValue(configManager.getConfig(configManager, "obfuscate"))
        self.ui.slid_notify.setValue(configManager.getConfig(configManager, "notify"))
        self.ui.slid_autoConnect.setValue(configManager.getConfig(configManager, "autoconnect"))
        self.ui.slid_ipv6.setValue(configManager.getConfig(configManager, "ipv6"))
        self.ui.slid_dns.setValue(configManager.getConfig(configManager, "dns"))
        # set the selected item in the comboboxes
        index_protocol = self.ui.cb_protocol.findText(configManager.getConfig(configManager, "protocol"), QtCore.Qt.MatchFixedString)
        if index_protocol >= 0:
            self.ui.cb_protocol.setCurrentIndex(index_protocol)
        index_tech = self.ui.cb_protocol.findText(configManager.getConfig(configManager, "technology"), QtCore.Qt.MatchFixedString)
        if index_tech >= 0:
            self.ui.cb_protocol.setCurrentIndex(index_tech)

        # load the dns configuration & whitelist
        self.__loadDNS()
        self.__loadWhitelist()

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
                                 self.__getSetting(self.ui.slid_firewall.value()) )
        configManager.setConfig( configManager,
                                 "killswitch",
                                 self.__getSetting(self.ui.slid_killSwitch.value()) )
        configManager.setConfig( configManager,
                                 "cybersec",
                                 self.__getSetting(self.ui.slid_cyberSec.value()) )
        configManager.setConfig( configManager,
                                 "obfuscate",
                                 self.__getSetting(self.ui.slid_obfuscate.value()) )
        configManager.setConfig( configManager,
                                 "notify",
                                 self.__getSetting(self.ui.slid_notify.value()) )
        configManager.setConfig( configManager,
                                 "autoconnect",
                                 self.__getSetting(self.ui.slid_autoConnect.value()) )
        configManager.setConfig( configManager,
                                 "ipv6",
                                 self.__getSetting(self.ui.slid_ipv6.value()) )
        configManager.setConfig( configManager,
                                 "dns",
                                 self.__getSetting(self.ui.slid_dns.value()) )
        configManager.setConfig( configManager,
                                 "protocol",
                                 self.ui.cb_protocol.currentText())
        configManager.setConfig( configManager,
                                 "technology",
                                 self.ui.cb_technology.currentText())

        # reload the dns and whitelist configurations
        self.__loadDNS()
        self.__loadWhitelist()

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
        self.ui.slid_firewall.setDisabled(disabled)
        self.ui.slid_killSwitch.setDisabled(disabled)
        self.ui.slid_cyberSec.setDisabled(disabled)
        self.ui.slid_obfuscate.setDisabled(disabled)
        self.ui.slid_notify.setDisabled(disabled)
        self.ui.slid_autoConnect.setDisabled(disabled)
        self.ui.slid_ipv6.setDisabled(disabled)
        self.ui.slid_dns.setDisabled(disabled)

        self.ui.cb_protocol.setDisabled(disabled)
        self.ui.cb_technology.setDisabled(disabled)

        self.ui.btn_save.setDisabled(disabled)


    def __enterDNS(self):
        # set the text to the config manager
        configManager.addDNSServer(configManager, self.ui.line_dns.text())
        # load dns again to show the new server in the list
        self.__loadDNS()
        return

    def __removeDNS(self):
        # get the text of the selected item and remove it from the list
        item = self.ui.list_dns.currentItem()
        if item is not None:
            configManager.removeDNSServer(configManager, item.text())
        # load dns again to show the server list
        self.__loadDNS()
        return