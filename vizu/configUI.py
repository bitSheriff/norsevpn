# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vizu/config.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Configuration(object):
    def setupUi(self, Configuration):
        Configuration.setObjectName("Configuration")
        Configuration.resize(400, 300)
        Configuration.setMinimumSize(QtCore.QSize(400, 300))
        Configuration.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("vizu/../doc/img/logo/NorseVPN.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Configuration.setWindowIcon(icon)
        self.btn_close = QtWidgets.QPushButton(Configuration)
        self.btn_close.setGeometry(QtCore.QRect(310, 270, 83, 25))
        self.btn_close.setObjectName("btn_close")
        self.btn_save = QtWidgets.QPushButton(Configuration)
        self.btn_save.setGeometry(QtCore.QRect(10, 270, 83, 25))
        self.btn_save.setObjectName("btn_save")
        self.tabWidget = QtWidgets.QTabWidget(Configuration)
        self.tabWidget.setGeometry(QtCore.QRect(6, 9, 391, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.config = QtWidgets.QWidget()
        self.config.setObjectName("config")
        self.label_cyberSec = QtWidgets.QLabel(self.config)
        self.label_cyberSec.setGeometry(QtCore.QRect(70, 70, 81, 17))
        self.label_cyberSec.setObjectName("label_cyberSec")
        self.slid_cyberSec = QtWidgets.QSlider(self.config)
        self.slid_cyberSec.setGeometry(QtCore.QRect(30, 70, 31, 16))
        self.slid_cyberSec.setMaximum(1)
        self.slid_cyberSec.setPageStep(1)
        self.slid_cyberSec.setOrientation(QtCore.Qt.Horizontal)
        self.slid_cyberSec.setObjectName("slid_cyberSec")
        self.slid_autoConnect = QtWidgets.QSlider(self.config)
        self.slid_autoConnect.setGeometry(QtCore.QRect(30, 160, 31, 16))
        self.slid_autoConnect.setMaximum(1)
        self.slid_autoConnect.setPageStep(1)
        self.slid_autoConnect.setOrientation(QtCore.Qt.Horizontal)
        self.slid_autoConnect.setObjectName("slid_autoConnect")
        self.label_firewall = QtWidgets.QLabel(self.config)
        self.label_firewall.setGeometry(QtCore.QRect(70, 10, 62, 17))
        self.label_firewall.setObjectName("label_firewall")
        self.slid_ipv6 = QtWidgets.QSlider(self.config)
        self.slid_ipv6.setGeometry(QtCore.QRect(30, 190, 31, 16))
        self.slid_ipv6.setMaximum(1)
        self.slid_ipv6.setPageStep(1)
        self.slid_ipv6.setOrientation(QtCore.Qt.Horizontal)
        self.slid_ipv6.setObjectName("slid_ipv6")
        self.slid_notify = QtWidgets.QSlider(self.config)
        self.slid_notify.setGeometry(QtCore.QRect(30, 130, 31, 16))
        self.slid_notify.setMaximum(1)
        self.slid_notify.setPageStep(1)
        self.slid_notify.setOrientation(QtCore.Qt.Horizontal)
        self.slid_notify.setObjectName("slid_notify")
        self.slid_firewall = QtWidgets.QSlider(self.config)
        self.slid_firewall.setGeometry(QtCore.QRect(30, 10, 31, 16))
        self.slid_firewall.setMaximum(1)
        self.slid_firewall.setPageStep(1)
        self.slid_firewall.setTracking(True)
        self.slid_firewall.setOrientation(QtCore.Qt.Horizontal)
        self.slid_firewall.setObjectName("slid_firewall")
        self.label_killSwitch = QtWidgets.QLabel(self.config)
        self.label_killSwitch.setGeometry(QtCore.QRect(70, 40, 81, 17))
        self.label_killSwitch.setObjectName("label_killSwitch")
        self.label_obfuscate = QtWidgets.QLabel(self.config)
        self.label_obfuscate.setGeometry(QtCore.QRect(70, 100, 91, 17))
        self.label_obfuscate.setObjectName("label_obfuscate")
        self.label_notify = QtWidgets.QLabel(self.config)
        self.label_notify.setGeometry(QtCore.QRect(70, 130, 51, 17))
        self.label_notify.setObjectName("label_notify")
        self.label_autoconnect = QtWidgets.QLabel(self.config)
        self.label_autoconnect.setGeometry(QtCore.QRect(70, 160, 111, 17))
        self.label_autoconnect.setObjectName("label_autoconnect")
        self.slid_obfuscate = QtWidgets.QSlider(self.config)
        self.slid_obfuscate.setGeometry(QtCore.QRect(30, 100, 31, 16))
        self.slid_obfuscate.setMaximum(1)
        self.slid_obfuscate.setPageStep(1)
        self.slid_obfuscate.setOrientation(QtCore.Qt.Horizontal)
        self.slid_obfuscate.setObjectName("slid_obfuscate")
        self.label_ipv6 = QtWidgets.QLabel(self.config)
        self.label_ipv6.setGeometry(QtCore.QRect(70, 190, 51, 17))
        self.label_ipv6.setObjectName("label_ipv6")
        self.slid_killSwitch = QtWidgets.QSlider(self.config)
        self.slid_killSwitch.setGeometry(QtCore.QRect(30, 40, 31, 16))
        self.slid_killSwitch.setMaximum(1)
        self.slid_killSwitch.setPageStep(1)
        self.slid_killSwitch.setOrientation(QtCore.Qt.Horizontal)
        self.slid_killSwitch.setObjectName("slid_killSwitch")
        self.cb_protocol = QtWidgets.QComboBox(self.config)
        self.cb_protocol.setGeometry(QtCore.QRect(287, 8, 86, 25))
        self.cb_protocol.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.cb_protocol.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cb_protocol.setFrame(True)
        self.cb_protocol.setModelColumn(0)
        self.cb_protocol.setObjectName("cb_protocol")
        self.cb_technology = QtWidgets.QComboBox(self.config)
        self.cb_technology.setGeometry(QtCore.QRect(287, 48, 86, 25))
        self.cb_technology.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.cb_technology.setFrame(True)
        self.cb_technology.setModelColumn(0)
        self.cb_technology.setObjectName("cb_technology")
        self.label_technology = QtWidgets.QLabel(self.config)
        self.label_technology.setGeometry(QtCore.QRect(188, 50, 81, 20))
        self.label_technology.setObjectName("label_technology")
        self.label_protocol = QtWidgets.QLabel(self.config)
        self.label_protocol.setGeometry(QtCore.QRect(210, 13, 62, 17))
        self.label_protocol.setObjectName("label_protocol")
        self.tabWidget.addTab(self.config, "")
        self.dns = QtWidgets.QWidget()
        self.dns.setObjectName("dns")
        self.label_dns = QtWidgets.QLabel(self.dns)
        self.label_dns.setGeometry(QtCore.QRect(50, 10, 101, 17))
        self.label_dns.setObjectName("label_dns")
        self.slid_dns = QtWidgets.QSlider(self.dns)
        self.slid_dns.setGeometry(QtCore.QRect(10, 10, 31, 16))
        self.slid_dns.setMaximum(1)
        self.slid_dns.setPageStep(1)
        self.slid_dns.setOrientation(QtCore.Qt.Horizontal)
        self.slid_dns.setObjectName("slid_dns")
        self.line_dns = QtWidgets.QLineEdit(self.dns)
        self.line_dns.setGeometry(QtCore.QRect(10, 180, 131, 25))
        self.line_dns.setMaxLength(15)
        self.line_dns.setObjectName("line_dns")
        self.dns_delete = QtWidgets.QPushButton(self.dns)
        self.dns_delete.setGeometry(QtCore.QRect(290, 180, 83, 25))
        self.dns_delete.setObjectName("dns_delete")
        self.list_dns = QtWidgets.QListWidget(self.dns)
        self.list_dns.setGeometry(QtCore.QRect(15, 31, 351, 141))
        self.list_dns.setObjectName("list_dns")
        self.tabWidget.addTab(self.dns, "")
        self.whitelist = QtWidgets.QWidget()
        self.whitelist.setObjectName("whitelist")
        self.tabWidget.addTab(self.whitelist, "")

        self.retranslateUi(Configuration)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Configuration)

    def retranslateUi(self, Configuration):
        _translate = QtCore.QCoreApplication.translate
        Configuration.setWindowTitle(_translate("Configuration", "Configuration"))
        self.btn_close.setText(_translate("Configuration", "Close"))
        self.btn_save.setText(_translate("Configuration", "Save"))
        self.label_cyberSec.setToolTip(_translate("Configuration", "When enabled, the CyberSec feature will automatically block suspicious websites so that no malware or other cyber threats can infect your device. Additionally, no flashy ads will come into your sight."))
        self.label_cyberSec.setText(_translate("Configuration", "Cyber-Sec"))
        self.label_firewall.setToolTip(_translate("Configuration", "blub"))
        self.label_firewall.setText(_translate("Configuration", "Firewall"))
        self.label_killSwitch.setToolTip(_translate("Configuration", "This security feature blocks your device from accessing the Internet outside the secure VPN tunnel, in case connection with a VPN server is lost."))
        self.label_killSwitch.setText(_translate("Configuration", "Kill Switch"))
        self.label_obfuscate.setText(_translate("Configuration", "Obfuscate"))
        self.label_notify.setText(_translate("Configuration", "Notify"))
        self.label_autoconnect.setToolTip(_translate("Configuration", "When enabled, this feature will automatically try to connect to VPN on operating system startup. "))
        self.label_autoconnect.setText(_translate("Configuration", "Auto Connect"))
        self.label_ipv6.setText(_translate("Configuration", "IPv6"))
        self.label_technology.setText(_translate("Configuration", "Technology"))
        self.label_protocol.setText(_translate("Configuration", "Protocol"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.config), _translate("Configuration", "Configuration"))
        self.label_dns.setText(_translate("Configuration", "Custom DNS"))
        self.line_dns.setText(_translate("Configuration", "8.8.8.8"))
        self.dns_delete.setText(_translate("Configuration", "Del"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dns), _translate("Configuration", "DNS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.whitelist), _translate("Configuration", "Whitelist"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Configuration = QtWidgets.QWidget()
    ui = Ui_Configuration()
    ui.setupUi(Configuration)
    Configuration.show()
    sys.exit(app.exec_())
