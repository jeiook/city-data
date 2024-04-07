from ApiDataRetriever.ApiRouteHandler import ApiRouteHandler


class ApiDataRetriever:
    def __init__(self, apiRouteHandler: ApiRouteHandler):
        self.apiRouteHandler = apiRouteHandler

    def getDataFromAPIRequestToPath(self, path: str):
        raise NotImplementedError("Please implement this method")
