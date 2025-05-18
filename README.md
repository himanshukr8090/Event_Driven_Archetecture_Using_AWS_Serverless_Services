# 📁 Event-Driven Architecture with S3, Lambda, and SNS
This project demonstrates a basic event-driven architecture using AWS S3, Lambda, and SNS (Simple Notification Service). When a file is uploaded to an S3 bucket, a Lambda function is triggered which then publishes a message to an SNS topic, sending an email notification to the subscribed user.

## 🛠️ Tech Stack
- **Amazon S3** – for file uploads
- **AWS Lambda** – for executing backend logic
- **Amazon SNS** – for sending email notifications
- **AWS IAM** – for managing permissions
- **Amazon CloudWatch** – for viewing logs and debugging


## 📦 Prerequisites
- AWS account
- Verified email address (for SNS subscription)
- Basic knowledge of AWS services

## ✅ Step-by-Step Implementation

### Step 1: Create an S3 Bucket
- Go to the **S3** console.
- Click **Create bucket**.
- Give it a name like `my_s3bucket`.
- Keep the rest default and click Create bucket.

### Step 2: Create an SNS Topic
- Go to the **SNS** service.
- Click on **Topics > Create topic.**
- Select Standard type.
- Name your topic, e.g., `mailwithlambda.`
- Click **Create topic**.

### Step 3: Create an SNS Subscription
- Open your created topic.
- Click on **Create subscription.**
- Set:
   - **Protocol**: Email  
   - **Endpoint**: Your email address
- Check your email and confirm the subscription.

### Step 4: Create a Lambda Function
- Go to **Lambda > Create function.**
- Choose Author from scratch.
- Function name: `S3UploadNotifier`
- Runtime: `Python 3.10`
- Choose or create an IAM role with:
  - `AmazonSNSFullAccess`
  - `AmazonS3FullAccess`
- Click Create function.

### Step 5: Add the Lambda Code
- Paste this code in your function:
```python
import boto3 

mysns = boto3.client("sns")

def lambda_handler(event, context):
    mysns.publish(
        TopicArn="arn:aws:sns:ap-south-1:327719058135:mailwithlambda",
        Subject="SomeThing Uploaded in S3",
        Message="Hi Himanshu, Go and Check the S3 Bucket. Something Uploaded by someone"
    )
    print("I am Himanshu and using lambda, and calling SNS testing lambda function..")
```
- Click Deploy after adding the code.

### Step 6: Add an S3 Trigger
- In the Lambda function page, click **Add Trigger.**
- Select **S3.**
- Choose your **S3 bucket.**
- Event type: `All object create events.`
- Click Add.

### Step 7: Test the Setup
- Upload a file (any file) to your S3 bucket.
- Check:
  - Your email inbox for a notification from SNS.
  - **CloudWatch Logs** for the Lambda execution logs.

### 🔐 IAM Role Permissions
- Ensure the Lambda function's IAM Role has:
  - `AmazonSNSFullAccess`
  - `AmazonS3FullAccess`
- You can attach these in IAM > Roles > Your Lambda Role.

### 📊 Monitoring with CloudWatch
- Go to **CloudWatch > Logs > Log groups**.
- Select the log group for your Lambda function.
- View logs to debug or check function execution.

### 📝 Notes
- Always **confirm the SNS email subscription.**
- You can add more subscribers to the SNS topic later.
- Make sure your **Lambda function timeout** is adequate (default is usually enough for this use-case).

### 📧 Output
- On every file upload to S3:
- Lambda triggers
- Lambda publishes a message to SNS
- SNS sends an email to the subscribed address
- CloudWatch logs show Lambda execution details

## Created by Himanshu Kumar Singh


