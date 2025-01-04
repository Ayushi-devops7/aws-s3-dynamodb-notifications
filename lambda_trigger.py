import json
import boto3
import logging

# Initialize the resources
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

# Specify the DynamoDB table name and SNS topic ARN
table = dynamodb.Table('S3EventLogs')  # Replace with your actual table name
sns_topic_arn = 'arn:aws:sns:your-region:your-account-id:S3UploadNotifications'  

def lambda_handler(event, context):
    try:
        # Process each record in the SQS message
        for record in event['Records']:
            # Get the message body
            body = record['body']
            
            # Parse the S3 event from the message body
            s3_event = json.loads(body)
            s3_bucket = s3_event['Records'][0]['s3']['bucket']['name']
            s3_object = s3_event['Records'][0]['s3']['object']['key']
            event_time = s3_event['Records'][0]['eventTime']
            
            # Store the details in DynamoDB
            response = table.put_item(
                Item={
                    'S3Bucket': s3_bucket,      # Partition key
                    'S3Object': s3_object,      # Sort key
                    'EventTime': event_time,    # Additional attribute
                    'MessageBody': body,        # Store the full message body
                }
            )
            
            # Check if the DynamoDB operation was successful
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                # Prepare the SNS message
                sns_message = f'Object "{s3_object}" has been uploaded to bucket "{s3_bucket}" and saved to DynamoDB.'
                
                # Publish the message to SNS
                sns.publish(
                    TopicArn=sns_topic_arn,
                    Message=sns_message,
                    Subject='S3 Object Upload Notification'
                )
            else:
                # Handle the case where DynamoDB storage failed
                logging.error(f'Failed to store data in DynamoDB for {s3_object} in {s3_bucket}.')
        
        return {
            'statusCode': 200,
            'body': json.dumps('Message processed, stored in DynamoDB, and notification sent if successful.')
        }
    
    except Exception as e:
        logging.error(f'Error processing message: {str(e)}')
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
