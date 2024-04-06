from DataProcessor.ZoriDataProcessor import ZoriDataProcessor
from ZoriFileReader.CityZoriFileReader import CityZoriFileReader


class CityZoriDataProcessor(ZoriDataProcessor):
    def __init__(self):
        fileReader = CityZoriFileReader()
        super().__init__(fileReader, offsetForRentNumbers=8)

    def _getRowsByMetroName(self, metroName: str):
        metroIndex = self.dataDict["columns"].index("Metro")
        return list(
            filter(lambda row: metroName in row[metroIndex].lower(), self.dataDict["rows"]))

    def _getRegionNameOfRow(self, row):
        regionNameIndex = self.dataDict["columns"].index("RegionName")
        return row[regionNameIndex]

    def listAverageZORIOfLocationsInMetroOverRange(self, metroName: str, yearStart: int | None = None, yearEnd: int | None = None):
        rowsInMetro = self._getRowsByMetroName(metroName)
        for row in rowsInMetro:
            region = self._getRegionNameOfRow(row)
            averageZORI = self.getAverageZORIOfRowOverRange(
                row, yearStart, yearEnd)
            print(f'{region} - {averageZORI}')