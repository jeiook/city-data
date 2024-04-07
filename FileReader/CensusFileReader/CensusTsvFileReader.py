from FileReader.FileReader import FileReader


class CensusTsvFileReader(FileReader):
    def __init__(self, fileName: str):
        super().__init__(fileName)

    def splitLineIntoTokens(self, line: str) -> list[str]:
        return line.strip().split("\t")
