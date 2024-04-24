from src.ApiDataRetriever.ApiDataRetriever import ApiDataRetriever
from src.ApiDataRetriever.Census.CensusApiDataType import CensusApiData
from src.ApiDataRetriever.Census.CensusApiRouteHandler import CensusApiRouteHandler
from src.DataExplorer.CensusStateMappingsDataExplorer import CensusStateMappingsDataExplorer


def zoriMetroDriver():
    yearStart = 2022
    yearEnd = 2024
    metroNames = ["rochester", "baltimore", "madison", "st. louis", "chicago", "buffalo", "minneapolis", "philadelphia",
                  "pittsburgh", "new york", "salt lake city", "boston", "portland", "san francisco", "seattle", "los angeles", "austin, tx"]
    # for metroName in metroNames:
    #     row = dataProcessor.getRowByLocationName(metroName)
    #     print(metroName, "-", dataProcessor.getAverageZORIOfRowOverRange(
    #         row, yearStart, yearEnd))
    print("results from zori_metro.csv")


def zoriCityDriver():
    yearStart = 2022
    yearEnd = 2024
    # dataProcessor.listAverageZORIOfLocationsInMetroOverRange(
    #     "los angeles", yearStart, yearEnd)
    print("results from zori_city.csv")


def censusDriver():
    routeHandler = CensusApiRouteHandler()
    dataRetriever = ApiDataRetriever[CensusApiData]()
    data = dataRetriever.getDataFromAPIRequestToPath(
        routeHandler.getListStates())
    # notice the type hint for data
    print(data)


def dataExplorerDriver():
    explorer = CensusStateMappingsDataExplorer(CensusApiRouteHandler())
    while True:
        key = input("Type in a state name or q to quit:\n")
        if key == "q":
            break
        try:
            print(f'State {key} has code {explorer.getStateCode(key)}')
        except KeyError:
            print(f'State {key} does not exist')
    print("end of program")


def main():
    # uncomment the driver function to be run
    # zoriMetroDriver()
    # zoriCityDriver()
    # censusDriver()
    dataExplorerDriver()


main()
