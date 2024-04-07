from ApiDataRetriever.Census.CensusApiDataRetriever import CensusApiDataRetriever
from ApiDataRetriever.Census.CensusApiRouteHandler import CensusApiRouteHandler
from DataProcessor.CityZoriDataProcessor import CityZoriDataProcessor
from DataProcessor.MetroZoriDataProcessor import MetroZoriDataProcessor
from OutputHandler.FileOutputHandler import FileOutputHandler


def zoriMetroDriver():
    dataProcessor = MetroZoriDataProcessor()
    yearStart = 2022
    yearEnd = 2024
    metroNames = ["rochester", "baltimore", "madison", "st. louis", "chicago", "buffalo", "minneapolis", "philadelphia",
                  "pittsburgh", "new york", "salt lake city", "boston", "portland", "san francisco", "seattle", "los angeles", "austin, tx"]
    for metroName in metroNames:
        row = dataProcessor.getRowByLocationName(metroName)
        print(metroName, "-", dataProcessor.getAverageZORIOfRowOverRange(
            row, yearStart, yearEnd))
    print("results from zori_metro.csv")


def zoriCityDriver():
    dataProcessor = CityZoriDataProcessor()
    yearStart = 2022
    yearEnd = 2024
    dataProcessor.listAverageZORIOfLocationsInMetroOverRange(
        "los angeles", yearStart, yearEnd)
    print("results from zori_city.csv")


def censusDriver():
    dataRetriever = CensusApiDataRetriever()
    apiRouteHandler = CensusApiRouteHandler()
    listData = dataRetriever.getDataFromAPIRequestToPath(
        apiRouteHandler.getListPlacesInCalifornia())
    outputHandler = FileOutputHandler("data/places_in_california.tsv")
    outputHandler.outputListData(listData)


def main():
    # uncomment the driver function to be run
    # zoriMetroDriver()
    # zoriCityDriver()
    censusDriver()


main()
