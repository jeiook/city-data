import requests
from ApiDataRetriever.ApiDataRetriever import ApiDataRetriever
from ApiDataRetriever.Census.CensusApiRouteHandler import CensusApiRouteHandler


class CensusApiDataRetriever(ApiDataRetriever):
    def getDataFromAPIRequestToPath(self, path: str):
        return requests.get(path).json()
