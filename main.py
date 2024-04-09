from ApiDataRetriever.ApiDataRetriever import ApiDataRetriever
from ApiDataRetriever.Census.CensusApiRouteHandler import CensusApiRouteHandler
from DataProcessor.CityZoriDataProcessor import CityZoriDataProcessor
from DataProcessor.MetroZoriDataProcessor import MetroZoriDataProcessor
from DataProcessor.PlacesInMetroDataProcessor import PlacesInMetroDataProcessor
from FileReader.CensusFileReader.CensusTsvFileReader import CensusTsvFileReader
from FileReader.ZoriFileReader.ZoriFileReader import ZoriFileReader
from OutputHandler.FileOutputHandler import FileOutputHandler


def zoriMetroDriver():
    fileReader = ZoriFileReader("data/zori_metro.csv")
    dataProcessor = MetroZoriDataProcessor(
        fileReader.getDataDictFromFile())
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
    fileReader = ZoriFileReader("data/zori_city.csv")
    dataProcessor = CityZoriDataProcessor(fileReader.getDataDictFromFile())
    yearStart = 2022
    yearEnd = 2024
    dataProcessor.listAverageZORIOfLocationsInMetroOverRange(
        "los angeles", yearStart, yearEnd)
    print("results from zori_city.csv")


def censusDriver():
    fileReader = CensusTsvFileReader("data/walk_score_of_cities.tsv")
    dataDict = fileReader.getDataDictFromFile()
    citiesInLaMap = map(lambda row: row[0], dataDict["rows"])
    cityZoriFileReader = ZoriFileReader("data/zori_city.csv")
    cityZoriDataProcessor = CityZoriDataProcessor(
        cityZoriFileReader.getDataDictFromFile())
    cityZoris = []
    for cityName in citiesInLaMap:
        cityZoris.append((
            cityName,
            cityZoriDataProcessor.getAverageZORIOfCityOverRange(
                cityName, 2022, 2024)
        ))
    for cityZori in cityZoris:
        print(cityZori[1])
    print(f'{len(cityZoris)} rows')


def main():
    # uncomment the driver function to be run
    # zoriMetroDriver()
    # zoriCityDriver()
    censusDriver()


main()
