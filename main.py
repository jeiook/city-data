from src.DataExplorer.ZoriCityDataExplorer import ZoriCityDataExplorer
from src.DataExplorer.ZoriMetroDataExplorer import ZoriMetroDataExplorer
from src.ApiDataRetriever.ApiDataRetriever import ApiDataRetriever
from src.ApiDataRetriever.Census.CensusApiDataType import CensusApiData
from src.ApiDataRetriever.Census.CensusApiRouteHandler import CensusApiRouteHandler
from src.DataExplorer.CensusStateMappingsDataExplorer import CensusStateMappingsDataExplorer


def zoriMetroDriver():
    metroNames: list[tuple[str, str]] = [
        ("rochester", "ny"),
        ("baltimore", "md"),
        ("madison", "wi"),
        ("st. louis", "mo"),
        ("chicago", "il"),
        ("buffalo", "ny"),
        ("minneapolis", "mn"),
        ("philadelphia", "pa"),
        ("pittsburgh", "pa"),
        ("new york", "ny"),
        ("salt lake city", "ut"),
        ("boston", "ma"),
        ("portland", "or"),
        ("san francisco", "ca"),
        ("seattle", "wa"),
        ("los angeles", "ca"),
        ("austin", "tx")
    ]
    dataExplorer = ZoriMetroDataExplorer("data/zori_metro.csv")
    for city, stateAbbrev in metroNames:
        rents = dataExplorer.getRentsOfRegionOverRange(city, stateAbbrev)
        print(f'rent in {city}:', [rents[0], rents[len(
            rents) // 4], rents[len(rents) // 2], rents[len(rents) * 3 // 4], rents[-1]])
    print("results from zori_metro.csv")


def zoriCityDriver():
    dataExplorer = ZoriCityDataExplorer("data/zori_city.csv")
    cityNames: list[tuple[str, str]] = [
        ("birmingham", "al"),
        ("scottsdale", "az"),
        ("burbank", "ca"),
        ("oakland", "ca"),
        ("pittsburgh", "pa"),
        ("buffalo", "ny")
    ]
    for city, stateAbbrev in cityNames:
        rents = dataExplorer.getRentsOfRegionOverRange(city, stateAbbrev)
        print(f'rent in {city}:', [rents[0], rents[len(
            rents) // 4], rents[len(rents) // 2], rents[len(rents) * 3 // 4], rents[-1]])
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
    zoriCityDriver()
    # censusDriver()
    # dataExplorerDriver()


main()
