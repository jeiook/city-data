from typing import Iterable


class DataObject(Iterable[str]):
    def getValueAtProperty(self, property: str):
        raise NotImplementedError("Please implement this method")
