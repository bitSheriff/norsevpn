import os, sys, string

import lib.general as general

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
        general.getOSString("nordvpn c " + cnt + "" + cty)
        return

    ## 
    # @public
    # @brief    Disconnect from the vpn
    # @details  This interface is used to disconnect the nordvpn server. 
    def disconnect(self):
        general.getOSString("nordvpn d")
        return
