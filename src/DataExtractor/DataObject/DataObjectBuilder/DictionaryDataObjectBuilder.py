from typing import Iterable

from src.DataExtractor.DataObject.DataObjectBuilder.DataObjectBuilder import DataObjectBuilder
from src.DataExtractor.DataObject.DataObject import DataObject
from src.DataExtractor.DataObject.DictionaryDataObject import DictionaryDataObject


class DictionaryDataObjectBuilder(DataObjectBuilder):
    def toDataObject(self, properties: Iterable[str], values: Iterable) -> DataObject:
        return DictionaryDataObject(properties, values)
