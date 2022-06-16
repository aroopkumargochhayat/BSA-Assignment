import json
import boto3
import uuid as myuuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('todo-table')

def put_user_data(uuid,title, task):

    response = table.put_item(
       Item={
            'id': uuid,
            'title': title,
            'task': task
        }
    )
    return response
    
def lambda_handler(event, context):
    
    uuid=str(myuuid.uuid4())
    title=event['title']
    task=event['task']
    dynamo_resp = put_user_data(uuid,title,task)
    return {
        'statusCode': 200,
        'body': json.dumps(dynamo_resp)
    }