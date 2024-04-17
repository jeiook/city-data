from DataExtractor.SourceDataRetriever.SourceDataRetriever import SourceDataRetriever


class ApiSourceDataRetriever(SourceDataRetriever):
    def getDataFromAPIRequestToPath(self, path: str):
        raise NotImplementedError("Please implement this method")
