from ApiDataRetriever.ApiDataRetriever import ApiDataRetriever
from src.DataExtractor.DataExtractor import DataExtractor


class ApiDataExtractor(DataExtractor):
    def __init__(self, dataRetriever: ApiDataRetriever, route: str) -> None:
        self._dataRetriever = dataRetriever
        self._route = route

    def _getSourceData(self):
        return self._dataRetriever.getDataFromAPIRequestToPath(self._route)
