from typing import Iterable


class SourceDataRetriever:
    def getPropertiesFromSourceData(self) -> Iterable[str]:
        raise NotImplementedError("Please implement this method")

    def getListOfValueListsFromSourceData(self) -> Iterable[Iterable]:
        raise NotImplementedError("Please implement this method")
