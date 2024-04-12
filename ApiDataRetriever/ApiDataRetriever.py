import requests
from typing import TypeVar, Generic

T = TypeVar("T")


class ApiDataRetriever(Generic[T]):
    def getDataFromAPIRequestToPath(self, path: str) -> T:
        return requests.get(path).json()
