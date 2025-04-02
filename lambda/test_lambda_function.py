import json
from lambda_function import lambda_handler

def test_lambda_handler():
    event = {}
    context = None
    result = lambda_handler(event, context)

    assert result['statusCode'] == 200
    body = json.loads(result['body'])
    assert 'views' in body
    assert isinstance(body['views'], int)
