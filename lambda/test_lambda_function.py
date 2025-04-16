import json
import pytest
from unittest.mock import patch, MagicMock
from lambdafunc import func

@patch("lambdafunc.func.boto3.resource")
def test_lambda_handler_success(mock_boto3_resource):
    mock_table = MagicMock()
    mock_table.update_item.return_value = {
        'Attributes': {'views': 123}
    }

    mock_boto3_resource.return_value.Table.return_value = mock_table

    response = func.lambda_handler({}, {})

    assert response['statusCode'] == 200
    body = json.loads(response['body'])
    assert body['views'] == 123
    assert response['headers']['Content-Type'] == 'application/json'