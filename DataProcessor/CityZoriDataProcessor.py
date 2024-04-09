from DataProcessor.ZoriDataProcessor import ZoriDataProcessor
from FileReader.ZoriFileReader.ZoriFileReader import ZoriFileReader


class CityZoriDataProcessor(ZoriDataProcessor):
    def __init__(self, dataDict):
        super().__init__(dataDict, offsetForRentNumbers=8)

    def _getRowsByMetroName(self, metroName: str):
        metroIndex = self.dataDict["columns"].index("Metro")
        return list(
            filter(lambda row: metroName in row[metroIndex].lower(), self.dataDict["rows"]))

    def _getRegionNameOfRow(self, row):
        regionNameIndex = self.dataDict["columns"].index("RegionName")
        return row[regionNameIndex]

    def _getRowByCityName(self, cityName: str, stateName: str = "CA"):
        regionNameIndex = self.dataDict["columns"].index("RegionName")
        stateNameIndex = self.dataDict["columns"].index("StateName")
        rowsOfCity = list(filter(
            lambda row: row[stateNameIndex] == stateName and cityName.lower(
            ) in row[regionNameIndex].lower(),
            self.dataDict["rows"]
        ))
        if not rowsOfCity:
            raise KeyError(f'No city with name {cityName}')
        return rowsOfCity[0]

    def listAverageZORIOfLocationsInMetroOverRange(self, metroName: str, yearStart: int | None = None, yearEnd: int | None = None):
        rowsInMetro = self._getRowsByMetroName(metroName)
        for row in rowsInMetro:
            region = self._getRegionNameOfRow(row)
            averageZORI = self.getAverageZORIOfRowOverRange(
                row, yearStart, yearEnd)
            print(f'{region} - {averageZORI}')

    def getAverageZORIOfCityOverRange(self, cityName: str, yearStart: int | None = None, yearEnd: int | None = None) -> float:
        return self.getAverageZORIOfRowOverRange(
            self._getRowByCityName(cityName),
            yearStart,
            yearEnd
        )
