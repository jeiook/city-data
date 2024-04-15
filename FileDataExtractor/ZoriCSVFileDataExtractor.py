from collections import namedtuple
import csv
from datetime import date


class ZoriCSVFileDataExtractor:
    def __init__(self, fileName: str) -> None:
        self._fileName = fileName
        reader = csv.reader(open(self._fileName))
        properties = next(reader)
        firstMonthIndex = -1
        for i, propertyName in enumerate(properties):
            if propertyName[0].isnumeric():
                firstMonthIndex = i
                break
        self._months = [date.fromisoformat(
            monthString) for monthString in properties[firstMonthIndex:]]
        properties = properties[:firstMonthIndex] + ["RentPricesByMonth"]
        listOfDataValues = [line[:firstMonthIndex] +
                            [tuple(line[firstMonthIndex:])] for line in reader if line]
        constructor = namedtuple("ZoriCSVFileDataObject", properties)
        self._dataList = [constructor._make(data) for data in listOfDataValues]

    def _getDataByRegion(self, regionName: str):
        return [data for data in self._dataList if data.RegionName == regionName][0]

    def _findMonthsRangeIndices(self, startDate: date, endDate: date):
        startIndex, endIndex = -1, -1
        for i, dateValue in enumerate(self._months):
            if startIndex != -1 and endIndex != -1:
                break
            if startIndex == -1 and dateValue == startDate:
                startIndex = i
                continue
            if endIndex == -1 and dateValue == endDate:
                endIndex = i
                continue
        if startIndex == -1:
            raise ValueError(f'Invalid starting date {str(startDate)}')
        if endIndex == -1:
            raise ValueError(f'Invalid ending date {str(endDate)}')
        return (startIndex, endIndex)

    def getRentsOfRegionOverRange(self, regionName: str, startDate: date = date.fromisoformat("2015-01-31"), endDate: date = date.fromisoformat("2024-02-29")):
        data = self._getDataByRegion(regionName)
        startIndex, endIndex = self._findMonthsRangeIndices(startDate, endDate)
        return list(map(lambda x: float(x) if x else 0, filter(lambda s: len(s), data.RentPricesByMonth[startIndex:endIndex])))
