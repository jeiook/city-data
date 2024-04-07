class ZoriDataProcessor:
    def __init__(self, dataDict: dict, offsetForRentNumbers: int):
        self.dataDict = dataDict
        self.offsetForRentNumbers = offsetForRentNumbers
        minYear = self.dataDict["columns"][offsetForRentNumbers].split(
            "-")[0]
        maxYear = self.dataDict["columns"][-1].split("-")[0]
        self.minYear = int(minYear) if minYear else 2016
        self.maxYear = int(maxYear) if maxYear else 2024

    def getAverageZORIOfRowOverRange(self, row: list[str], yearStart: int | None = None, yearEnd: int | None = None):
        if yearStart and yearStart < self.minYear:
            raise ValueError(f'Invalid starting year {yearStart}')
        if yearEnd and yearEnd > self.maxYear:
            raise ValueError(f'Invalid ending year {yearEnd}')
        start = self.offsetForRentNumbers + \
            (yearStart - self.minYear) * \
            12 if yearStart else self.offsetForRentNumbers
        end = min(self.offsetForRentNumbers + (yearEnd - self.minYear + 1) * 12,
                  len(self.dataDict["columns"])) if yearEnd else len(self.dataDict["columns"])
        zoris = list(map(lambda x: float(x) if x else 0,
                     filter(lambda s: len(s), row[start:end])))
        return sum(zoris) / len(zoris)
