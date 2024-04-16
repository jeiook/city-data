from collections import namedtuple
from ApiDataRetriever.ApiDataRetriever import ApiDataRetriever


class ApiDataExtractor:
    def __init__(self, dataRetriever: ApiDataRetriever, route: str, dataTypeName: str) -> None:
        self._dataRetriever = dataRetriever
        self._route = route
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

    def _getPropertiesFromData(self, data) -> list[str]:
        raise NotImplementedError("Please implement this method")

    def _getListOfValuesFromData(self, data) -> list[list]:
        raise NotImplementedError("Please implement this method")

    def _getDataObjects(self):
        if self._dataObjects:
            return self._dataObjects
        data = self._dataRetriever.getDataFromAPIRequestToPath(self._route)
        self._dataProperties = self._getPropertiesFromData(data)
        constructor = self._getDataObjectConstructor()
        if not constructor:
            raise ValueError(
                f'{self._dataTypeName} constructor not initialized')
        self._dataObjects = [constructor._make(
            valuesList) for valuesList in self._getListOfValuesFromData(data)]
        return self._dataObjects
