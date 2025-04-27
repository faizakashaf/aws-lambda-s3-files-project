import json
import boto3
import os

# Create boto3 clients
sns_client = boto3.client('sns')
secrets_client = boto3.client('secretsmanager')

# Fetch the secret 
secret_response = secrets_client.get_secret_value(SecretId='SNSUploadTopicArn')
secret = json.loads(secret_response['SecretString'])
SNS_TOPIC_ARN = secret['sns_topic_arn']

def lambda_handler(event, context):
    print("Received event:", json.dumps(event))

    if 'Records' not in event:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid event format: Records key missing.')
        }

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    message = f"A new file '{object_key}' was uploaded to bucket '{bucket_name}'."
    
    # Publish to SNS
    response = sns_client.publish(
        TopicArn=SNS_TOPIC_ARN,
        Message=message,
        Subject='New S3 Upload Notification'
    )
    
    print("Message published to SNS:", response)
    return {
        'statusCode': 200,
        'body': json.dumps('Notification sent successfully!')
    }
