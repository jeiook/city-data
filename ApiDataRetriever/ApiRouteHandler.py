class ApiRouteHandler:
    def __init__(self, key: str):
        self.key = key

    def getFullApiPath(self, route: str) -> str:
        raise NotImplementedError("Please implement this method")
