from DataProcessor.MetroZoriDataProcessor import MetroZoriDataProcessor
from ZoriFileReader.ZoriCityFileReader import ZoriCityFileReader


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
    zoriCityFileReader = ZoriCityFileReader()
    fileHandle = zoriCityFileReader.getFileHandle()
    dataDict = zoriCityFileReader.getDataDictFromFile(fileHandle)
    print(dataDict)


def main():
    # zoriMetroDriver()
    zoriCityDriver()


main()
