import json
import lib.general as general

configDir = "config"
locationDir= configDir + "/locations.json"

##
# @brief    Class to handle the configurations
class configManager():

    ## 
    # @public
    # @brief    Get Cities
    # @details  This interface reads the json with the available countries & cities and returns
    #           a dictionary with all cities in this country.
    #
    # @retunrs  Returns a dictionary of all available cities in the wanted country
    def getCities(self, cnt):
        with open(locationDir) as f:
            data = json.load(f)
        return data[cnt]


    def updateLocations(self):
        cnties = self.__getDict(self, "nordvpn countries")

        for cnt in cnties:
            cities = self.__getArr(self, "nordvpn cities " + str(cnt))
            cnties[cnt].append(cities)
        print(cnties)
        with open(locationDir, "w") as jsonFile:
            json.dump(cnties, jsonFile, indent=4, sort_keys=True)




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
        return arr