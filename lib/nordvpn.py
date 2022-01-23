import logging
import os, sys, string

import lib.general as general
from lib.conf import configManager

##
# @brief Class for the NordVPN Cli functions
class nordvpn():


    ##
    # @brief    Check Nordvpn installation
    # @details  This interface is used to get if nordvpn-cli is installed on this system
    #
    # @returns  Returns boolish value if nordvpn-cli is installed
    # @retval   False   nordvpn is not installed
    # @retval   True    nordvpn is installed
    def checkInstall(self):
        installed = False
        res = general.getOSString("nordvpn -v")
        if "NordVPN Version" in res:
            installed = True
        return installed

    ##
    # @brief    Check Nordvpn connection
    # @details  This interface is used to get if the user is currently connected to the nordvpn servers
    #
    # @returns  Returns boolish value if nordvpn-cli is connected
    # @retval   False   nordvpn is not connected
    # @retval   True    nordvpn is connected
    def isConnected(self):
        connected = False
        res = general.getOSString("nordvpn status")
        if "Connected" in res:
            connected = True
        return connected

    ## 
    # @public
    # @brief    Connect to the vpn
    # @details  This interface is used to connect to a nordvpn server. 
    #           With the given parameter it can be defined which country and city is used.
    # @note     If country and city are not given then the nordvpn-cli will use the default one.
    #
    # @param    cnt    Wanted country
    # @param    cty    Wanted city
    def connect(self, cnt="", cty=""):
        self.__setSettings(self)        # set the user wanted settings
        connect = "nordvpn c " + cnt + " " + cty
        logging.info(repr(connect))
        logging.info(general.getOSString(connect))
        return
        

    ## 
    # @public
    # @brief    Disconnect from the vpn
    # @details  This interface is used to disconnect the nordvpn server. 
    def disconnect(self):
        self.__setDefaultSettings(self)         # return to default settings
        logging.info(general.getOSString("nordvpn d"))
        return

    ## 
    # @public
    # @brief    Status from the vpn
    # @details  This interface is used to disconnect the nordvpn server. 
    def getStatus(self):
        return general.getOSString("nordvpn status")

    def __setSettings(self):
        self.__setSetting(self, "firewall", configManager.getConfig(configManager, "firewall"))
        self.__setSetting(self, "killswitch", configManager.getConfig(configManager, "killswitch"))
        self.__setSetting(self, "cybersec", configManager.getConfig(configManager, "cybersec"))
        self.__setSetting(self, "autoconnect", configManager.getConfig(configManager, "autoconnect"))
        self.__setSetting(self, "obfuscate", configManager.getConfig(configManager, "obfuscate"))
        self.__setSetting(self, "notify", configManager.getConfig(configManager, "notify"))
        self.__setSetting(self, "ipv6", configManager.getConfig(configManager, "ipv6"))
        self.__setSetting(self, "dns", configManager.getConfig(configManager, "dns"))
        self.__setSetting(self, "protocol", configManager.getConfig(configManager, "protocol"))
        self.__setSetting(self, "technology", configManager.getConfig(configManager, "technology"))

    def __setDefaultSettings(self):
        self.__setSetting(self, "firewall", True)
        self.__setSetting(self, "killswitch", False)
        self.__setSetting(self, "cybersec", False)
        self.__setSetting(self, "obfuscate", False)
        self.__setSetting(self, "notify", False)
        self.__setSetting(self, "ipv6", False)
        self.__setSetting(self, "dns", False)
        self.__setSetting(self, "protocol", "UDP")
        self.__setSetting(self, "technology", "OpenVPN")

    def __setSetting(self, setting, val):
        general.getOSString("nordvpn set " + setting + " "+ str(val))

    def getVersion(self):
        return general.getOSString("nordvpn --version")