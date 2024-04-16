from ApiDataExtractor.ApiDataExtractor import ApiDataExtractor
from ApiDataRetriever.ApiDataRetriever import ApiDataRetriever
from ApiDataRetriever.Census.CensusApiDataType import CensusApiData
from ApiDataRetriever.Census.CensusApiRouteHandler import CensusApiRouteHandler


class CensusStateMappingsApiDataExtractor(ApiDataExtractor):
    def __init__(self) -> None:
        routeHandler = CensusApiRouteHandler()
        dataRetriever = ApiDataRetriever[CensusApiData]()
        super().__init__(dataRetriever, routeHandler.getListStates(), "CensusStateMappingsObject")

    def _getPropertiesFromData(self, data) -> list[str]:
        return data[0]

    def _getListOfValuesFromData(self, data) -> list[list]:
        return data[1:]

    def getStateCode(self, fullStateName: str) -> str:
        filtered = [mapping for mapping in self._getDataObjects(
        ) if mapping.NAME.lower() == fullStateName.lower()]
        if not filtered:
            raise KeyError(f'State {fullStateName} not found')
        return filtered[0].state
