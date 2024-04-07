from ApiDataRetriever.Census.CensusApiDataRetriever import CensusApiDataRetriever
from ApiDataRetriever.Census.CensusApiRouteHandler import CensusApiRouteHandler
from DataProcessor.CityZoriDataProcessor import CityZoriDataProcessor
from DataProcessor.MetroZoriDataProcessor import MetroZoriDataProcessor
from FileReader.ZoriFileReader.ZoriFileReader import ZoriFileReader
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


def zoriFileReaderDriver():
    fileReader = ZoriFileReader("")
    print(fileReader.splitLineIntoTokens(
        "102001,0,United States,country,,1222.8126117105548"))
    print(fileReader.splitLineIntoTokens(
        "394913,1,\"New York, NY\",msa,NY,2286.9183201876376"))
    print(fileReader.splitLineIntoTokens(
        "753899,2,\"Los Angeles, CA\",msa,CA,1833.2128308607282"))


def main():
    # uncomment the driver function to be run
    # zoriMetroDriver()
    # zoriCityDriver()
    # censusDriver()
    zoriFileReaderDriver()


main()
