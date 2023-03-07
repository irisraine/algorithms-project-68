import pytest
from router import MakeRouter

static_routes = [
    {
        'method': 'GET',
        'path': '/courses',
        'constraints': {},
        'handler': lambda params: 'all courses'
    },
    {
        'method': 'POST',
        'path': '/courses',
        'constraints': {},
        'handler': lambda params: 'add new course'
    },
    {
        'method': 'GET',
        'path': '/courses/python',
        'constraints': {},
        'handler': lambda params: 'python course'
    },
    {
        'method': 'GET',
        'path': '/courses/python/trees',
        'constraints': {},
        'handler': lambda params: 'python course about tree-like structures'
    },

]

static_routing_test_cases = [
    (
        {'path': '/courses', 'method': 'GET'},
        {
            'path': '/courses',
            'method': 'GET',
            'params': {},
            'handler_output': 'all courses'
        },
    ),
    (
        {'path': '/courses', 'method': 'POST'},
        {
            'path': '/courses',
            'method': 'POST',
            'params': {},
            'handler_output': 'add new course'
        },
    ),
    (
        {'path': '/courses/python', 'method': 'GET'},
        {
            'path': '/courses/python',
            'method': 'GET',
            'params': {},
            'handler_output': 'python course'
        },
    ),
    (
        {'path': '/courses/python/trees', 'method': 'GET'},
        {
            'path': '/courses/python/trees',
            'method': 'GET',
            'params': {},
            'handler_output': 'python course about tree-like structures'
        },
    ),
]


@pytest.mark.parametrize('static_request, expected_result', static_routing_test_cases)
def test_static_routes(static_request, expected_result):
    static_router = MakeRouter(static_routes)
    result_raw = static_router.serve(static_request)
    result = {
        'path': result_raw['path'],
        'method': result_raw['method'],
        'params': result_raw['params'],
        'handler_output': result_raw['handler'](result_raw['params'])
    }
    assert result == expected_result
