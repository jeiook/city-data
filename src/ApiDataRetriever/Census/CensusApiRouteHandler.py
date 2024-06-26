from dotenv import dotenv_values

from src.ApiDataRetriever.ApiRouteHandler import ApiRouteHandler

_YEAR = 2022
_BASE_API_URL = "https://api.census.gov/data/"

# For a guide on how to use the census.gov API, see: https://www.census.gov/data/developers/guidance/api-user-guide/example-api-queries.html
# For catalogues of API paths, see https://api.census.gov/data.html


class CensusApiRouteHandler(ApiRouteHandler):
    def __init__(self):
        key = dotenv_values(".env.local")["CENSUS_API_KEY"]
        if not key:
            raise KeyError(
                "Could not find CENSUS_API_KEY; is the .env.local file properly set up?")
        super().__init__(key)

    def _getKeyString(self) -> str:
        return "&key=" + self.key

    def _getFullApiPath(self, route: str) -> str:
        return _BASE_API_URL + str(_YEAR) + route + self._getKeyString()

    def getListStates(self):
        return self._getFullApiPath(f'/acs/acs1/subject?get=NAME,S0101_C01_001E&for=state:*')

    def getListPlacesInState(self, stateCode: str):
        return self._getFullApiPath(f'/acs/acs1/subject?get=NAME,S0101_C01_001E&for=place:*&in=state:{stateCode}')

    def getTotalWalkedOfPlaceInState(self, place: str, state: str):
        return self._getFullApiPath(f'/acs/acs1/subject?get=NAME,S0801_C01_010E&for=place:{state}&in=state:{state}')
