import re


class RoutePrefixTreeNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.is_dynamic = None
        self.endpoint = False
        self.pattern_path = None
        self.handler = None

    def get_pattern_path(self):
        return self.pattern_path

    def get_handler(self):
        return self.handler


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
                current_node.is_dynamic = True if segment.startswith(":") else False
            current_node = current_node.children[segment]
            pattern_path.append(segment)
        current_node.endpoint = True
        current_node.handler = route['handler']
        current_node.pattern_path = '/'.join(pattern_path)

    def find_route(self, route_path):
        current_node = self.root
        segments = route_path.split('/')
        for segment in segments:
            node_has_segment = False
            for node_segment in current_node.children:
                if (segment == node_segment) or (current_node.is_dynamic and re.match(r'(\w+)', segment)):
                    node_has_segment = True
                    current_node = current_node.children[node_segment]
                    break
            if not node_has_segment:
                return None
        return current_node
