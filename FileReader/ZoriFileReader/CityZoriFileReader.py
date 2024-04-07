from FileReader.ZoriFileReader.ZoriFileReader import ZoriFileReader


class CityZoriFileReader(ZoriFileReader):
    def __init__(self):
        super().__init__("data/zori_city.csv")

    def getFileHandle(self):
        return open(self.fileName, "r")

    def _getRestOfFile(self, file):
        return file.read().split("\n")[:-1]

    def _getArrayFromCSVLine(self, line):
        quoteSplitLine = line.split("\"")
        if len(quoteSplitLine) == 1:
            return line.split(",")
        textInQuotes = quoteSplitLine[1]
        commaSplitLine = line.split(",")
        return commaSplitLine[:6] + [textInQuotes] + commaSplitLine[8:]
