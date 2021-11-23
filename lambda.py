import subprocess,boto3,json

def handler(event, context):

    print("event =" + event)

    return {
        "statusCode" : 200,
        "body" : "Lambda's work is done!"
    }
