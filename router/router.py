class MakeRouter:
    def __init__(self, routes):
        self.routes = routes

    def serve(self, path):
        for route in self.routes:
            if route['path'] == path:
                return route['handler']
        raise Exception("Incorrect path!")
