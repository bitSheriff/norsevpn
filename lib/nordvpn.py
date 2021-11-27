import os, sys, string

##
# @brief Class for the NordVPN Cli functions
class nordvpn():


    ##
    # @brief    Check Nordvpn installation
    # @details  this interface is used to get if nordvpn-cli is installed on this system
    # @returns  Returns boolish value if nordvpn-cli is installed
    # @retval   False   nordvpn is not installed
    # @retval   True    nordvpn is installed
    def checkInstall(self):
        installed = False
        res = self.__getOSString("nordvpn -v")
        if "NordVPN Version" in res:
            installed = True
        return installed

    def isConnected(self):
        connected = False
        res = self.__getOSString("nordvpn status")
        if "Connected" in res:
            connected = True
        return connected



 # # # # # PRIVATE FUNCTIONS # # # # # 
    def __getOSString(cmnd):
        call = os.popen(cmnd, 'r')
        return call.read()
