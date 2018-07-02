import boto3
import os
import datetime
import json

def lambda_handler(event,context):
    client = boto3.client('sns')
    now = datetime.datetime.now()
    print(serv_list()) #testing purposes
    '''
    client.publish(
        TopicArn=(os.environ['TOPIC_ARN']),
        Subject=('AWS Servive List | ' + str(now.day) + ' ' + now.strftime("%B") + ', ' + str(now.year)),
        Message=serv_list()
    )
    '''
def defauConvert(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def serv_list():
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
    return (json.dumps(response, default=defauConvert, sort_keys=True, indent=4))
