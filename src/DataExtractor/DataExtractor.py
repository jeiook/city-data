from typing import Iterable, Iterator
from src.DataExtractor.DataObject.DataObject import DataObject
from src.DataExtractor.DataObject.DataObjectBuilder.DataObjectBuilder import DataObjectBuilder
from src.DataExtractor.SourceDataRetriever.SourceDataRetriever import SourceDataRetriever


class DataExtractor(Iterable):
    def __init__(self, sourceDataRetriever: SourceDataRetriever, dataObjectBuilder: DataObjectBuilder) -> None:
        self._sourceDataRetriever = sourceDataRetriever
        self._dataObjectBuilder = dataObjectBuilder
        self._dataObjects = None

    def _getDataObjects(self):
        if self._dataObjects:
            return self._dataObjects
        self._dataObjects = [
            self._dataObjectBuilder.toDataObject(
                self._sourceDataRetriever.getPropertiesFromSourceData(),
                valuesIterable
            )
            for valuesIterable
            in self._sourceDataRetriever.getListOfValueListsFromSourceData()
        ]
        return self._dataObjects

    def __iter__(self) -> Iterator[DataObject]:
        return self._getDataObjects().__iter__()
