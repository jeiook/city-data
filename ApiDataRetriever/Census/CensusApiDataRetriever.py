import requests
from ApiDataRetriever.ApiDataRetriever import ApiDataRetriever
from ApiDataRetriever.Census.CensusApiRouteHandler import CensusApiRouteHandler


class CensusApiDataRetriever(ApiDataRetriever):
    def __init__(self):
        super().__init__(CensusApiRouteHandler())

    def getDataFromAPIRequestToPath(self, path: str):
        response = requests.get(
            self.apiRouteHandler.getFullApiPath(path))
        return response.json()

    def listPlacesInCalifornia(self):
        return self.getDataFromAPIRequestToPath("listPlacesInCalifornia")
