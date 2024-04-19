from typing import Iterable
from src.DataExtractor.DataObject.DataObject import DataObject


class DataObjectBuilder:
    def toDataObject(self, properties: Iterable[str], values: Iterable) -> DataObject:
        raise NotImplementedError("Please implement this method")
