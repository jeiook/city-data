import csv
from typing import Iterable
from DataExtractor.SourceDataRetriever.SourceDataRetriever import SourceDataRetriever


class CsvFileSourceDataRetriever(SourceDataRetriever):
    def __init__(self, fileName) -> None:
        super().__init__()
        reader = csv.reader(open(fileName))
        self._properties = (next(reader))
        self._listOfDataValues = [line for line in reader if line]

    def getPropertiesFromSourceData(self) -> Iterable[str]:
        return self._properties

    def getListOfValueListsFromSourceData(self) -> Iterable[Iterable]:
        return self._listOfDataValues
