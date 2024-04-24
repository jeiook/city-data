class ApiRouteHandler:
    def __init__(self, key: str):
        self.key = key

    def _getFullApiPath(self, route: str) -> str:
        raise NotImplementedError("Please implement this method")
