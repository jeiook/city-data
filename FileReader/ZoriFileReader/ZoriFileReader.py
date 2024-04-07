from FileReader.FileReader import FileReader


class ZoriFileReader(FileReader):
    def __init__(self, fileName: str):
        super().__init__(fileName)

    def _splitLinesWithQuotesIntoTokens(self, line: str) -> list[str]:
        quoteSplitLine = line.strip().split("\"")
        tokens = []
        for i, partialLine in enumerate(quoteSplitLine):
            if i % 2 == 0:
                tokens += partialLine.strip(",").split(",")
                continue
            tokens += [partialLine]
        return tokens

    def splitLineIntoTokens(self, line: str) -> list[str]:
        strippedLine = line.strip()
        if "\"" in strippedLine:
            return self._splitLinesWithQuotesIntoTokens(strippedLine)
        return strippedLine.split(",")
