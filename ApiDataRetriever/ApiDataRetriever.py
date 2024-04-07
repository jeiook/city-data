import requests


class ApiDataRetriever:
    def getDataFromAPIRequestToPath(self, path: str):
        return requests.get(path).json()
