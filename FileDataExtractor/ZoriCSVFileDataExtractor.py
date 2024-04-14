from collections import namedtuple
import csv


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
        self._months = properties[firstMonthIndex:]
        properties = properties[:firstMonthIndex] + ["RentPricesByMonth"]
        listOfData = [line[:firstMonthIndex] +
                      [tuple(line[firstMonthIndex:])] for line in reader if line]
        constructor = namedtuple("ZoriCSVFileDataObject", properties)
        self._data = [constructor._make(data) for data in listOfData]

    def get_data(self):
        return self._data
