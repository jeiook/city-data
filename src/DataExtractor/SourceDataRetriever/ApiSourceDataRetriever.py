from typing import Iterable
from src.ApiDataRetriever.ApiDataRetriever import ApiDataRetriever
from src.DataExtractor.SourceDataRetriever.SourceDataRetriever import SourceDataRetriever


class ApiSourceDataRetriever(SourceDataRetriever):
    def __init__(self, apiDataRetriever: ApiDataRetriever, pathname: str) -> None:
        super().__init__()
        self._pathname = pathname
        self._apiDataRetriever = apiDataRetriever
        self._processedSourceData = None

    def getPropertiesFromSourceData(self) -> Iterable[str]:
        if self._processedSourceData:
            return self._processedSourceData[0]
        self._processedSourceData = self._retrieveData()
        return self._processedSourceData[0]

    def getListOfValueListsFromSourceData(self) -> Iterable[Iterable]:
        if self._processedSourceData:
            return self._processedSourceData[1]
        self._processedSourceData = self._retrieveData()
        return self._processedSourceData[1]

    def _retrieveData(self):
        rawData = self._apiDataRetriever.getDataFromAPIRequestToPath(
            self._pathname)
        return (rawData[0], rawData[1:])
