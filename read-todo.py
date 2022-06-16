import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('todo-table')

def get_data(uuid):

    response = table.get_item(Key={'id': uuid})
    return response

def lambda_handler(event, context):

    uuid = event.get('uuid', None)

    if uuid != None:

      uuid=event['uuid']
      data = get_data(uuid)

    if uuid == None:
      response = table.scan()
      data = response['Items']
      while 'LastEvaluatedKey' in response:
          response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
          data.extend(response['Items'])

    return {
      'statusCode': 200,
      'body': json.dumps(data)
        }
