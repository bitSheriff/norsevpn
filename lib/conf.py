import json
import random
import lib.general as general

configDir = "config"
locationDir= configDir + "/locations.json"
settingDir = configDir + "/settings.json"

##
# @brief    Class to handle the configurations
class configManager():

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
        with open(locationDir, "w") as jsonFile:
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
        with open(settingDir, "r") as f:
            data = json.load(f)
            f.close()
        return data[strVal]

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

    def getRandomLocation(self):
        locations = self.getLocationDict(self)
        country, city = random.choice(list(locations.items()))
        return country, city