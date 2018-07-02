import os
import json
import boto3
import datetime

def Lambda_Handler(event,context):
    client = boto3.client('sns')
    now = datetime.datetime.now()

    client.publish(
        TopicArn=(os.environ['TOPIC_ARN']),
        Subject=('AWS Servive List | ' + str(now.day) + ' ' + now.strftime("%B") + ', ' + str(now.year)),
        Message=ServiceList()
    )

def Convert(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def ServiceList():
    response = {}
    ec2 = boto3.client('ec2')
    s3 = boto3.client('s3')
    lam = boto3.client('lambda')
    dynamo = boto3.client('dynamodb')
    rds = boto3.client('rds')

    response['-------------------EC2-------------------'] = ec2.describe_instances()
    response['-------------------S3-------------------'] = s3.list_buckets()
    response['-------------------Lambda Functions-------------------'] = lam.list_functions()
    response['-------------------DynamoDB Tables-------------------'] = dynamo.list_tables()
    response['-------------------RDS-------------------'] = rds.describe_db_instances()
    return (json.dumps(response, default=Convert, sort_keys=True, indent=4))
