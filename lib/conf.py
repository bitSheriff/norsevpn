import json
from json.decoder import JSONDecodeError
import logging
import random
import os, sys

sys.path.append("..")
import lib.general as general

configDir = "~/.config/norsevpn"
locationDir= os.path.abspath(os.path.expanduser(os.path.expandvars(configDir + "/locations.json"))) 
settingDir = os.path.abspath(os.path.expanduser(os.path.expandvars(configDir + "/settings.json"))) 


##
# @brief    Class to handle the configurations
class configManager():

    defaultSetting = {
            "autoconnect": False,
            "cybersec": False,
            "dns": False,
            "firewall": False,
            "ipv6": False,
            "killswitch": False,
            "notify": False,
            "obfuscate": False,
            "protocol": "UDP",
            "selected_city": "Vienna",
            "selected_country": "Austria",
            "technology": "OpenVPN",
            "dns_list": [""],
            "whitelist": [""]
            }

    def initializeConfig(self):
        print("Init config")
        # check if the config is not initalized yest on system
        if(not os.path.isfile(locationDir)):
            # create folder
            os.popen("mkdir " + configDir, 'r')
            os.popen("touch " + settingDir, 'r')
            os.popen("touch " + locationDir, 'r')
            with open(settingDir, "w+") as f: 
                f.seek(0)
                json.dump(self.defaultSetting, f,  indent=4, sort_keys=True)
                f.close()

        return

    ## 
    # @public
    # @brief    Get Cities
    # @details  This interface reads the json with the available countries & cities and returns
    #           a dictionary with all cities in this country.
    #
    # @returns  Returns a dictionary of all available cities in the wanted country
    def getCities(self, cnt):
        with open(locationDir) as f:
            data = json.load(f)
        return data[cnt]

    def getLocationDict(self):
        with open(locationDir) as f:
            data = json.load(f)
        return data

    ##
    # @public
    # @brief    Update Locations
    # @details  This interface is used to read the available countries
    #           and cities from the nordvpn-cli application. 
    #           These cities are stored in a json file where the
    #           user can select a destination.
    # @note     This interface has not to be called every application start-up
    def updateLocations(self):
        cnties = self.__getDict(self, "nordvpn countries")

        for cnt in cnties:
            cities = self.__getArr(self, "nordvpn cities " + str(cnt))
            cnties[cnt].append(cities)
        with open(locationDir, "w+") as jsonFile:
            json.dump(cnties, jsonFile, indent=4, sort_keys=True)

    ##
    # @public
    # @brief    Set Config
    # @details  This interface sets the wanted configuration to the wanted value.
    #           At first the json is loaded and then the wanted value is repaced.
    #           At last the new json dictionary is written to the file.
    #
    # @param strVal Config which should be set
    # @param value  Value which the config should be set
    def setConfig(self, strVal, value):
        with open(settingDir, "r") as f:
            data = json.load(f)
            f.close()
        data[strVal] = value
        with open(settingDir, "w+") as f: 
            f.seek(0)
            json.dump(data, f,  indent=4, sort_keys=True)
            f.close()
    ##
    # @public
    # @brief    Get Config
    # @details  This interface gets the wanted configuration of the 
    #           settings file.
    #
    # @param strVal
    # @returns  string  Value of the wanted configuration
    def getConfig(self, strVal):
        retVal = ""
        with open(settingDir, "r") as f:
            data = json.load(f)
            f.close()
        try:
            retVal = data[strVal]
        except KeyError as err:
            logging.error("Config Key " + strVal + " not found")
            retVal = ""
        return retVal

    ## 
    # @public
    # @brief    Get Dictionary from OS command
    # @details  This private interfaces turns the result from the stdout
    #           which the wanted command returned into a dictionary.
    #
    # @param    cmnd    OS command which is executed
    # @returns  dict    Returns a dictionary of the results
    def __getDict(self, cmnd):
        str = general.getOSString(cmnd)
        dict = {}
        temp = str.replace("\t"," ")
        temp = temp.replace("\n"," ")
        temp = temp.split(" ")
        for x in temp:
            if(x != "-" and x != "" and x != " "):
                dict[x] = []
        return dict

    ## 
    # @public
    # @brief    Get Array from OS command
    # @details  This private interfaces turns the result from the stdout
    #           which the wanted command returned into an array.
    #
    # @param    cmnd    OS command which is executed
    # @returns  array   Returns an array of the results
    def __getArr(self, cmnd):
        str = general.getOSString(cmnd)
        arr = []
        i=0
        temp = str.replace("\t"," ")
        temp = temp.replace("\n"," ")
        temp = temp.split(" ")
        for x in temp:
            if(x != "-" and x != "" and x != " "):
                arr.append(x)
        return arr#

    def __getConfigStream(self):
        with open(settingDir, "r") as f:
            data = json.load(f)
            f.close()
        return data

    def __setConfigStream(self, stream):
        with open(settingDir, "w+") as f: 
            f.seek(0)
            json.dump(stream, f,  indent=4, sort_keys=True)
            f.close()
        return


    def getRandomLocation(self):
        locations = self.getLocationDict(self)
        country, city = random.choice(list(locations.items()))
        return country, city


    def addDNSServer(self, server):
        # load the whole configuration
        config = self.__getConfigStream(self)
        # add the server to the list
        config["dns_list"].append(server)
        # store the whole configuration again
        self.__setConfigStream(self, config)
        return
    
    def getDNSServer(self):
        # load the whole configuration
        config = self.__getConfigStream(self)
        # return the dns server list
        return config["dns_list"]

    def removeDNSServer(self, server):
        # load the whole configuration
        config = self.__getConfigStream(self)
        # remove the wanted server
        config["dns_list"].remove(server)
        # store the whole configuration again
        self.__setConfigStream(self, config)
        return


