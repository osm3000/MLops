"""
Implementing basic CI/CD for a AWS lambda function
"""
import json

random_dict = {"first": True, "second": False}

def lambda_handler(event, context):
    """
    My first Lambda function within CI/CD
    """

    print(context)

    return {
        "statusCode": 200,
        "body": json.dumps("Hello from Lambda!"),
        "another_body": "Hello from the other side....",
        "event": event,
    }
