import re
import json


class MakeRouter:
    def __init__(self, routes):
        self.routes = routes
        self.path = None
        self.handler = None
        self.params = None

    def __str__(self):
        router_elements = json.dumps({
            'path': self.path,
            'handler': str(self.handler),
            'params': self.params}
        )
        return router_elements

    def serve(self, path):
        dynamic_placeholder = r'(\w+)'
        slash_escaped = r'\/'
        params = {}

        for route in self.routes:
            pattern_parsed = route['path'].split('/')
            pattern_regex_segments = []
            for pattern_segment in pattern_parsed:
                if pattern_segment and pattern_segment[0] == ':':
                    pattern_regex_segments.append(dynamic_placeholder)
                    params.setdefault(pattern_segment[1:], '')
                else:
                    pattern_regex_segments.append(pattern_segment)
            pattern_regex = f'^{slash_escaped.join(pattern_regex_segments)}$'
            is_match = re.match(pattern_regex, path)
            if is_match:
                path_parsed = path.split('/')
                for pattern_segment, path_segment in zip(pattern_parsed, path_parsed):
                    if pattern_segment[1:] in params.keys():
                        params[pattern_segment[1:]] = path_segment

                self.path = route['path']
                self.handler = route['handler']
                self.params = params

                return self
        raise Exception("Incorrect path!")
