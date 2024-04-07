class FileReader:
    def __init__(self, fileName: str):
        self.fileName = fileName

    def splitLineIntoTokens(self, line: str) -> list[str]:
        raise NotImplementedError("Please implement this method")

    def getDataDictFromFile(self):
        file = open(self.fileName, "r")
        columns = self.splitLineIntoTokens(file.readline())
        rows = []
        for line in file:
            if line.strip():
                rows.append(self.splitLineIntoTokens(line))
        file.close()
        dataDict = dict()
        dataDict["columns"] = columns
        dataDict["rows"] = rows
        return dataDict
