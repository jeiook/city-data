from ZoriFileReader.ZoriFileReader import ZoriFileReader


class MetroZoriFileReader(ZoriFileReader):
    def __init__(self):
        super().__init__("data/zori_metro.csv")

    def getFileHandle(self):
        return open(self.fileName, "r")

    def _getRestOfFile(self, file):
        return file.read().split("\n")[1:-1]

    def _getArrayFromCSVLine(self, line):
        commaSplitLine = line.split(",")
        textInQuotes = line.split("\"")[1]
        return commaSplitLine[:2] + [textInQuotes] + commaSplitLine[4:]
