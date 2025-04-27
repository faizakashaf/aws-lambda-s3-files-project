📂 **AWS Lambda + S3 + SNS Notification Project**

**Project Overview**
This project demonstrates how to automatically send notifications whenever a file is uploaded to an Amazon S3 bucket, using AWS Lambda and SNS (Simple Notification Service).
It showcases a simple event-driven architecture without using any servers — fully serverless

**Workflow**
A file is uploaded to a specified S3 bucket.
S3 Event Notification triggers a Lambda function.
The Lambda function:
Reads the event metadata (bucket name, file key, etc.).
Publishes a message to an SNS topic.
SNS delivers the notification to its subscribed endpoints (can be email, SMS, etc.).

**Technologies Used**
AWS S3 (Storage)
AWS Lambda (Serverless Compute)
AWS SNS (Messaging Service)
Python (Lambda function code)
IAM Roles and Policies (for permissions)

**Setup Instructions**
1. Create an S3 Bucket
Create a bucket to store files.
Block all public access for security.
2. Create an SNS Topic
Create a topic for notifications.
Subscribe your email/SMS if you want to receive notifications.

**Create the Lambda Function**
Runtime: Python 3.12
Environment Variable: SNS_TOPIC_ARN (your SNS Topic ARN)

**Attach Required IAM Permissions**
Allow the Lambda function to:
Read from S3 events
Publish to SNS topics

**Configure S3 Event Notification**
Go to your bucket → Properties → Event Notifications → Create Event:
Event type: PUT (file upload)
Destination: Lambda function (select your created function)

![image](https://github.com/user-attachments/assets/a70c3bf4-1698-4fd3-b0e8-778ec0b0ef9b)

![image](https://github.com/user-attachments/assets/25504624-8506-4108-a688-a29fa6126710)

![image](https://github.com/user-attachments/assets/aa78fe26-8710-4c47-be22-9ee73be98597)

![image](https://github.com/user-attachments/assets/35e14c9e-dbc7-4ade-afbf-0f154039b4f4)



🧑‍💻 **Author**
Faiza Kashaf
Cloud Enthusiast | DevOps Engineer | AWS Explorer ☁️
