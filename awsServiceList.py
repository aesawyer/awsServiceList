import boto3
import os
import datetime

def lambda_handler(event,context):
    client = boto3.client('sns')
    now = datetime.datetime.now()

    client.publish(
        TopicArn=(os.environ['TOPIC_ARN']),
        Subject=('AWS Servive List | ' + str(now.day) + ' ' + now.strftime("%B") + ', ' + str(now.year)),
        Message="It worked"
    )
