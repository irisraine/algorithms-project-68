# Router

### Hexlet tests and linter status:
[![Actions Status](https://github.com/irisraine/algorithms-project-68/workflows/hexlet-check/badge.svg)](https://github.com/irisraine/algorithms-project-68/actions)
[![Actions Status](https://github.com/irisraine/algorithms-project-68/workflows/pytest/badge.svg)](https://github.com/irisraine/algorithms-project-68/actions/workflows/pytest.yml)
[![Actions Status](https://github.com/irisraine/algorithms-project-68/workflows/flake8/badge.svg)](https://github.com/irisraine/algorithms-project-68/actions/workflows/flake8.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/e65b65afc40737f43b9c/maintainability)](https://codeclimate.com/github/irisraine/algorithms-project-68/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e65b65afc40737f43b9c/test_coverage)](https://codeclimate.com/github/irisraine/algorithms-project-68/test_coverage)

### Description

The educational project implements a router that uses a prefix tree data structure to efficiently 
match URL addresses to corresponding handler functions. 

The prefix tree is used to store all the available URL addresses and their corresponding handler functions. 
Each node in the tree  represents a prefix of the URL, and contains a list of handler functions that match 
that prefix. To process an incoming request, the router will first extract the URL address from the request. 
It will then traverse the prefix tree, starting at the root node, and following the path that matches the 
extracted address. Once it reaches the leaf node corresponding to the address, it will retrieve the list of 
handler functions stored at that node.
If there are multiple handler functions in the list, the router will select the appropriate one based on 
the HTTP method of the incoming request. For example, if the request is a GET request, the router will 
select the handler function for the GET method.
Finally, the router have an option to call the selected handler function with the request as an argument, 
allowing the handler to process the request and generate a response.