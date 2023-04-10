import pytest
from router import MakeRouter

dynamic_routes = [
    {
        'method': 'GET',
        'path': '/courses/:id',
        'constraints': {'id': r'^(\d+)$'},
        'handler': lambda params: f"show course №{params['id']} contents"
    },
    {
        'method': 'GET',
        'path': '/courses/:id/users',
        'constraints': {'id': r'^(\d+)$'},
        'handler': lambda params: f"list of users enlisted to a course №{params['id']}"
    },
    {
        'method': 'POST',
        'path': '/courses/:id/users',
        'constraints': {'id': r'^(\d+)$'},
        'handler': lambda params: f"add a new student to a course №{params['id']}"
    },
    {
        'method': 'GET',
        'path': '/courses/:id/users/:user-slug',
        'constraints': {'id': r'^(\d+)$', 'user-slug': r'^[a-z0-9]+(?:-[a-z0-9]+)*$'},
        'handler': lambda params: f"show personal info for user {params['user-slug']} "
                                  f"who enlisted to a course №{params['id']}"
    },
    {
        'method': 'DELETE',
        'path': '/courses/:id/users/:user-slug',
        'constraints': {'id': r'^(\d+)$', 'user-slug': r'^[a-z0-9]+(?:-[a-z0-9]+)*$'},
        'handler': lambda params: f"remove user {params['user-slug']} from list of students of a course №{params['id']}"
    },
]

dynamic_routing_test_cases = [
    (
        {'path': '/courses/11', 'method': 'GET'},
        {
            'path': '/courses/:id',
            'method': 'GET',
            'params': {'id': '11'},
            'handler_output': 'show course №11 contents'}
    ),
    (
        {'path': '/courses/11/users', 'method': 'GET'},
        {
            'path': '/courses/:id/users',
            'method': 'GET',
            'params': {'id': '11'},
            'handler_output': 'list of users enlisted to a course №11'
        }
    ),
    (
        {'path': '/courses/11/users', 'method': 'POST'},
        {
            'path': '/courses/:id/users',
            'method': 'POST',
            'params': {'id': '11'},
            'handler_output': 'add a new student to a course №11'
        }
    ),
    (
        {'path': '/courses/11/users/iris-raine', 'method': 'GET'},
        {
            'path': '/courses/:id/users/:user-slug',
            'method': 'GET',
            'params': {'id': '11', 'user-slug': 'iris-raine'},
            'handler_output': 'show personal info for user iris-raine who enlisted to a course №11'
        }
    ),
    (
        {'path': '/courses/11/users/iris-raine', 'method': 'DELETE'},
        {
            'path': '/courses/:id/users/:user-slug',
            'method': 'DELETE',
            'params': {'id': '11', 'user-slug': 'iris-raine'},
            'handler_output': 'remove user iris-raine from list of students of a course №11'
        }
    ),
]


@pytest.mark.parametrize('dynamic_request, expected_result', dynamic_routing_test_cases)
def test_dynamic_routes(dynamic_request, expected_result):
    dynamic_router = MakeRouter(dynamic_routes)
    result_raw = dynamic_router.serve(dynamic_request)
    result = {
        'path': result_raw['path'],
        'method': result_raw['method'],
        'params': result_raw['params'],
        'handler_output': result_raw['handler'](result_raw['params'])
    }
    assert result == expected_result
