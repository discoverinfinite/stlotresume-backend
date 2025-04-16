import boto3
import json

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')  # ✅ Moved inside the function
    table = dynamodb.Table('cloudresume')

    response = table.update_item(
        Key={'id': '1'},
        UpdateExpression='SET #v = if_not_exists(#v, :start) + :inc',
        ExpressionAttributeNames={'#v': 'views'},
        ExpressionAttributeValues={':inc': 1, ':start': 0},
        ReturnValues='UPDATED_NEW'
    )
    
    views = int(response['Attributes']['views'])

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'views': views})
    }
