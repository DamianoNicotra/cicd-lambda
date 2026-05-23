import json
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../lambda')))

import lambda_function

def test_lambda_handler():
    event = {}
    context = {}
    response = lambda_function.lambda_handler(event, context)
    
    assert response['statusCode'] == 200
    assert 'CI/CD pipeline working' in response['body']
