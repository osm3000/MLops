import json

def lambda_handler(event, context):
    # TODO implement
    print(event)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!'),
        'another_body': "Hello from the other side....",
        'event': event
    }
