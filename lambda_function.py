import boto3

mysns = boto3.client("sns")

def lambda_handler(event, context):
    mysns.publish(
        TopicArn="arn:aws:sns:ap-south-1:327719058135:mailwithlambda",
        Subject="SomeThing Uploaded in S3",
        Message="Hi Himanshu, Go and Check the S3 Bucket. Something Uploaded by someone"
        
        )
    print("I am Himanshu and using lambda, and calling SNS testing lambda function..")