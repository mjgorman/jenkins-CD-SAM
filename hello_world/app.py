import boto3
import json


session = boto3.Session()


def lambda_handler(event, context):
    """
        AWS Lambda handler


        This method is invoked by the API Gateway: /<env>/{proxy+} endpoint.

    """
    message = get_message()

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }


def get_message():
    """
        You can create a sub-segment specifically to a function
        then capture what sub-segment that is inside your code
        and you can add annotations that will be indexed by X-Ray
        for example: put_annotation("operation", "query_db")
    """
    return {'hello': 'world_10'}
