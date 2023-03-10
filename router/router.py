from .prefix_tree import RoutePrefixTree


class MakeRouter:
    ALLOWED_HTTP_METHODS = ['GET', 'POST', 'DELETE', 'PUT',
                            'HEAD', 'OPTIONS', 'TRACE', 'CONNECT']

    def __init__(self, routes):
        self.routes_tree = RoutePrefixTree()
        for route in routes:
            self.routes_tree.add_route(route)

    def serve(self, request):
        if request['method'] not in self.ALLOWED_HTTP_METHODS:
            raise Exception("Unrecognized non-HTTP method")
        target_route = self.routes_tree.find_route(request)
        if not target_route:
            raise Exception("Given path doesn't presented in routes list")
        pattern_path = target_route.get_pattern_path()
        result = {
            'path': pattern_path,
            'method': request['method'],
            'handler': target_route.get_handler(request['method']),
            'params': self.get_route_params(request['path'], pattern_path),
        }
        return result

    @staticmethod
    def get_route_params(request_path, pattern_path):
        params = {}
        request_path_parsed = request_path.split('/')
        pattern_path_parsed = pattern_path.split('/')
        paths_mapped = zip(request_path_parsed, pattern_path_parsed)
        for request_path_segment, pattern_path_segment in paths_mapped:
            if pattern_path_segment.startswith(":"):
                param = pattern_path_segment[1:]
                params.setdefault(param, request_path_segment)
        return params
