import json
from validate_email_address import validate_email

# import requests
def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e
    body = json.loads(event['body'])
    email = body.get('email')

    if validate_email(email) is None:
        return {
            "statuscode": 400,
            "body": json.dumps({
                "message": "Email no válido",
                # "location": ip.text.replace("\n", "")
            }),
        }
    else:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Email si válido",
                # "location": ip.text.replace("\n", "")
            }),
        }

