import os, sys, string

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
        res = self.__getOSString("nordvpn -v")
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
        res = self.__getOSString("nordvpn status")
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
        return


    ## 
    # @private
    # @brief    Get string from a OS command
    #
    # @returns  Returns the string wich the OS returned on the stdout
    def __getOSString(cmnd):
        call = os.popen(cmnd, 'r')
        return call.read()
