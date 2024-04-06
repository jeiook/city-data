from dotenv import dotenv_values

from ApiDataRetriever.ApiRouteHandler import ApiRouteHandler

_BASE_API_URL = "https://api.census.gov/data/2022/acs/acsse?get=NAME,K200101_001E"
_API_ROUTES = {
    "listStates": "&for=state:*",
    "listPlacesInCalifornia": "&for=place:*&in=state:06"
}
# See https://api.census.gov/data/2022/acs/acsse/examples.html for examples of full API paths


class CensusApiRouteHandler(ApiRouteHandler):
    def __init__(self):
        key = dotenv_values(".env.local")["CENSUS_API_KEY"]
        if not key:
            raise KeyError(
                "Could not find CENSUS_API_KEY; is the .env.local file properly set up?")
        super().__init__(key)

    def _getKeyString(self) -> str:
        return "&key=" + self.key

    def getFullApiPath(self, route: str) -> str:
        if route not in _API_ROUTES:
            raise ValueError(f'No API route named {route}')
        return _BASE_API_URL + _API_ROUTES[route] + self._getKeyString()
