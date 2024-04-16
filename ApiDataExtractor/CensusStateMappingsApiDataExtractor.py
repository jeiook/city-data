from typing import Iterable
from ApiDataExtractor.ApiDataExtractor import ApiDataExtractor
from ApiDataRetriever.ApiDataRetriever import ApiDataRetriever
from ApiDataRetriever.Census.CensusApiDataType import CensusApiData
from ApiDataRetriever.Census.CensusApiRouteHandler import CensusApiRouteHandler


class CensusStateMappingsApiDataExtractor(ApiDataExtractor):
    def __init__(self) -> None:
        routeHandler = CensusApiRouteHandler()
        dataRetriever = ApiDataRetriever[CensusApiData]()
        super().__init__(dataRetriever, routeHandler.getListStates(), "CensusStateMappingsObject")

    def _getPropertiesFromSourceData(self, data) -> Iterable[str]:
        return data[0]

    def _getListOfValuesFromSourceData(self, data) -> Iterable[Iterable]:
        return data[1:]

    def getStateCode(self, fullStateName: str) -> str:
        filtered = [mapping for mapping in self._getDataObjects(
        ) if mapping.NAME.lower() == fullStateName.lower()]
        if not filtered:
            raise KeyError(f'State {fullStateName} not found')
        return filtered[0].state
