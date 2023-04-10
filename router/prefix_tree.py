import re


class RoutePrefixTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_dynamic = False
        self.constraints = {}
        self.endpoint = ''
        self.handlers = {}

    def get_pattern_path(self):
        return self.endpoint

    def get_handler(self, method):
        return self.handlers[method]


class RoutePrefixTree:
    def __init__(self):
        self.root = RoutePrefixTreeNode(None)

    def add_route(self, route):
        current_node = self.root
        segments = route['path'].split('/')
        pattern_path = []
        for segment in segments:
            if segment not in current_node.children:
                current_node.children[segment] = RoutePrefixTreeNode(segment)
                if segment.startswith(":"):
                    current_node.is_dynamic = True
                    current_node.constraints = route['constraints']
            current_node = current_node.children[segment]
            pattern_path.append(segment)
        current_node.handlers.setdefault(
            route['method'],
            route['handler']
        )
        current_node.endpoint = '/'.join(pattern_path)

    def find_route(self, request):  # noqa: C901
        current_node = self.root
        segments = request['path'].split('/')
        for segment in segments:
            node_has_segment = False
            for node_segment in current_node.children:
                if segment == node_segment:
                    node_has_segment = True
                elif current_node.is_dynamic:
                    param = node_segment[1:]
                    param_constraint = current_node.constraints[param]
                    node_has_segment = self.check_constraints(
                        segment, param_constraint
                    )
                if node_has_segment:
                    current_node = current_node.children[node_segment]
                    break
            if not node_has_segment:
                return None
        if request['method'] not in current_node.handlers:
            return None
        return current_node

    @staticmethod
    def check_constraints(segment, constraint):
        if isinstance(constraint, str):
            regex_constraint = re.compile(constraint)
            return True if regex_constraint.match(segment) else False
        elif callable(constraint):
            return constraint(segment)
