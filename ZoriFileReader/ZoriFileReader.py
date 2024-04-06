class ZoriFileReader:
    def __init__(self, fileName):
        self.fileName = fileName

    def getFileHandle(self):
        raise NotImplementedError("Please implement this method")

    def _getColumns(self, file):
        return file.readline()[:-1].split(",")

    def _getRestOfFile(self, file):
        raise NotImplementedError("Please implement this method")

    def _getArrayFromCSVLine(self, line):
        raise NotImplementedError("Please implement this method")

    def getDataDictFromFile(self, file):
        columns = self._getColumns(file)
        restOfFile = self._getRestOfFile(file)
        dataDict = dict()
        dataDict["columns"] = columns
        dataDict["rows"] = []
        for line in restOfFile:
            dataDict["rows"].append(self._getArrayFromCSVLine(line))
        return dataDict
