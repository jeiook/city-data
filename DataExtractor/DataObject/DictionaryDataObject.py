from typing import Iterable
from DataExtractor.DataObject.DataObject import DataObject


class DictionaryDataObject(DataObject):
    def __init__(self, properties: Iterable[str], values: Iterable) -> None:
        super().__init__()
        self._data = dict()
        properties = [property for property in properties]
        for i, value in enumerate(values):
            self._data[properties[i]] = value

    def getValueAtProperty(self, property: str):
        return self._data[property]
