import json
import logging
import os
import time
import uuid

import boto3

dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])

    timestamp = str(time.time())

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    item = {
        'id': str(uuid.uuid1()),
        'name': data['name'],
        'designation':data['designation'],
        'phonenumber':data['phonenumber'],
        'createdAt': timestamp,
        'updatedAt': timestamp,
    }

    # create the employee to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
