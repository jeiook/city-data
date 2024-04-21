from typing import Iterable
from ApiDataRetriever.ApiDataRetriever import ApiDataRetriever
from ApiDataRetriever.Census.CensusApiRouteHandler import CensusApiRouteHandler
from src.DataExtractor.DataExtractor import DataExtractor


class CensusStateMappingsApiDataExtractor(DataExtractor):
    def __init__(self) -> None:
        # sourceDataRetriever: SourceDataRetriever
        # dataObjectBuilder: DataObjectBuilder
        routeHandler = CensusApiRouteHandler()
        dataRetriever = ApiDataRetriever()
        super().__init__(dataRetriever, routeHandler.getListStates())

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
