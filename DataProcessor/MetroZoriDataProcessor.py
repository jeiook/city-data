from DataProcessor.ZoriDataProcessor import ZoriDataProcessor


class MetroZoriDataProcessor(ZoriDataProcessor):
    def __init__(self, dataDict):
        super().__init__(dataDict, offsetForRentNumbers=5)

    def getRowByLocationName(self, locationName: str) -> list[str]:
        regionNameIndex = self.dataDict["columns"].index("RegionName")
        rowsWithCityName = list(filter(
            lambda row: locationName in row[regionNameIndex].lower(), self.dataDict["rows"]))
        if len(rowsWithCityName) == 0:
            raise ValueError(f'{locationName} does not exist in the dataset')
        return rowsWithCityName[0]
