from datetime import date
from src.DataExtractor.DataExtractor import DataExtractor
from src.DataExtractor.DataObject.DataObjectBuilder.DictionaryDataObjectBuilder import DictionaryDataObjectBuilder
from src.DataExtractor.SourceDataRetriever.CsvFileSourceDataRetriever import CsvFileSourceDataRetriever


class ZoriCityDataExplorer:
    def __init__(self, filename: str) -> None:
        self._dataExtractor = DataExtractor(
            CsvFileSourceDataRetriever(filename),
            DictionaryDataObjectBuilder()
        )
        self._dataDict = {
            (
                data.getValueAtProperty("RegionName"),
                data.getValueAtProperty("StateName")
            ):
                data for data in self._dataExtractor
        }

    def _getLocationTupleFromCityState(self, city: str, stateAbbrev: str) -> tuple[str, str]:
        if " " in city:
            capitalizedWordsInCity = [word.capitalize()
                                      for word in city.split(" ")]
            return (" ".join(capitalizedWordsInCity), stateAbbrev.upper())
        return (city.capitalize(), stateAbbrev.upper())

    def _getDateKeyFromDate(self, date: date) -> str:
        return date.isoformat()

    def getRentsOfRegionOverRange(self, city: str, stateAbbrev: str, startDate: date = date.fromisoformat("2015-01-31"), endDate: date = date.fromisoformat("2024-02-29")):
        data = self._dataDict[self._getLocationTupleFromCityState(
            city, stateAbbrev)]
        rents = []
        startFound = False
        for property in data:
            if not startFound and property != self._getDateKeyFromDate(startDate):
                continue
            startFound = True
            if property == self._getDateKeyFromDate(endDate):
                break
            rents.append(data.getValueAtProperty(property))
        return rents
