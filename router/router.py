from prefix_tree import RoutePrefixTree


class MakeRouter:
    def __init__(self, routes):
        self.routes_tree = RoutePrefixTree()
        for route in routes:
            self.routes_tree.add_route(route)

    def serve(self, path):
        target_route = self.routes_tree.find_route(path)
        if not target_route:
            raise Exception("Incorrect path!")
        pattern_path = target_route.get_pattern_path()
        result = {
            'path': pattern_path,
            'handler': target_route.get_handler(),
            'params': self.get_route_params(path, pattern_path),
        }
        return result

    @staticmethod
    def get_route_params(given_path, pattern_path):
        params = {}
        given_path_parsed = given_path.split('/')
        pattern_path_parsed = pattern_path.split('/')
        for given_path_segment, pattern_path_segment in zip(given_path_parsed, pattern_path_parsed):
            if pattern_path_segment.startswith(":"):
                params.setdefault(pattern_path_segment[1:], given_path_segment)
        return params
