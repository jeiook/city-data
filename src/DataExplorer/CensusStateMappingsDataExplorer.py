from ApiDataRetriever.ApiDataRetriever import ApiDataRetriever
from ApiDataRetriever.Census.CensusApiRouteHandler import CensusApiRouteHandler
from src.DataExtractor.DataObject.DataObjectBuilder.DictionaryDataObjectBuilder import DictionaryDataObjectBuilder
from src.DataExtractor.SourceDataRetriever.ApiSourceDataRetriever import ApiSourceDataRetriever
from src.DataExtractor.DataExtractor import DataExtractor


class CensusStateMappingsDataExplorer:
    def __init__(self, censusApiRouteHandler: CensusApiRouteHandler) -> None:
        self._dataExtractor = DataExtractor(
            ApiSourceDataRetriever(
                ApiDataRetriever(), censusApiRouteHandler.getListStates()),
            DictionaryDataObjectBuilder()
        )
        self._stateCodes: dict[str, str] | None = None

    def _getPopulatedStateCodes(self):
        if self._stateCodes:
            return self._stateCodes
        self._stateCodes = dict()
        for data in self._dataExtractor:
            self._stateCodes[data.getValueAtProperty(
                "NAME").lower()] = data.getValueAtProperty("state")
        return self._stateCodes

    def getStateCode(self, fullStateName: str) -> str:
        if fullStateName.lower() not in self._getPopulatedStateCodes():
            raise KeyError(f'State {fullStateName} not recognized')
        return self._getPopulatedStateCodes()[fullStateName]
