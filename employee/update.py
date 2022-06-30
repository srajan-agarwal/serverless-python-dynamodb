import json
import time
import logging
import os

import boto3
dynamodb = boto3.resource('dynamodb')


def update(event, context):
    data = json.loads(event['body'])

    timestamp = int(time.time() * 1000)

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # update the employee in the database
    result = table.update_item(
        Key={
            'id': event['pathParameters']['id']
        },
        ExpressionAttributeNames={
          '#name': 'name',
        },
        ExpressionAttributeValues={
            ':name': data['name'],
            ':designation':data['designation'],
            ':phonenumber':data['phonenumber'],
            ':updatedAt': timestamp,
        },
        UpdateExpression='SET #name = :name, '
                         'designation = :designation, '
                         'phonenumber=:phonenumber, '                         
                         'updatedAt = :updatedAt',
        ReturnValues='ALL_NEW',
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Attributes'])
    }

    return response