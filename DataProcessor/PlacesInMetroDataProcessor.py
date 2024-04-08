from typing import Literal

type DataColumnsTuple = tuple[Literal["city"], Literal["place"]]
type CityName = str
type PlaceId = str
type CityPlaceDataRow = tuple[CityName, PlaceId]
type CityPlaceData = tuple[DataColumnsTuple,
                           list[CityPlaceDataRow]]


class PlacesInMetroDataProcessor:
    def __init__(self, citiesInMetroDataDict: dict[str, list[str]], placesInStateDataDict: dict[str, list[str]]):
        self.citiesInMetro = list(
            map(lambda row: row[0].lower(), citiesInMetroDataDict["rows"]))
        self.placeNamesInState = list(
            map(lambda row: row[0].lower(), placesInStateDataDict["rows"]))
        cityPlaceMappings: list[tuple[str, list]] = list(map(
            lambda city: (city, list(filter(
                lambda row: city in row[0].lower(),
                placesInStateDataDict["rows"]))
            ),
            self.citiesInMetro
        ))
        cityPlaceDataColumns: DataColumnsTuple = ("city", "place")
        cityPlaceDataRows: list[CityPlaceDataRow] = list((map(
            lambda mapping: (mapping[0], mapping[1][0][3]),
            filter(
                lambda mapping: mapping[1],
                cityPlaceMappings
            )
        )))
        self.cityPlaceData: CityPlaceData = (
            cityPlaceDataColumns, cityPlaceDataRows)

    def getCityPlaceData(self):
        return self.cityPlaceData
