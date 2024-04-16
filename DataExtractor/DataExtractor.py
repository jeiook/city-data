from collections import namedtuple
from typing import Iterable


class DataExtractor:
    def __init__(self, dataTypeName: str) -> None:
        self._sourceData = None
        self._dataTypeName = dataTypeName
        self._dataProperties = []
        self._dataObjectConstructor = None
        self._dataObjects = None

    def _getDataObjectConstructor(self):
        if self._dataObjectConstructor:
            return self._dataObjectConstructor
        if self._dataProperties:
            self._dataObjectConstructor = namedtuple(
                self._dataTypeName, self._dataProperties)
            return self._dataObjectConstructor
        return None

    def _getPropertiesFromSourceData(self, data) -> Iterable[str]:
        raise NotImplementedError("Please implement this method")

    def _getListOfValuesFromSourceData(self, data) -> Iterable[Iterable]:
        raise NotImplementedError("Please implement this method")

    def _getSourceData(self):
        raise NotImplementedError("Please implement this method")

    def _getDataObjects(self):
        if self._dataObjects:
            return self._dataObjects
        data = self._getSourceData()
        self._dataProperties = self._getPropertiesFromSourceData(data)
        constructor = self._getDataObjectConstructor()
        if not constructor:
            raise ValueError(
                f'{self._dataTypeName} constructor not initialized')
        self._dataObjects = [constructor._make(
            valuesList) for valuesList in self._getListOfValuesFromSourceData(data)]
        return self._dataObjects
