import boto3

AWS_REGION = "us-east-2"
client = boto3.client('s3',region_name=AWS_REGION)
location = {'LocationConstraint': AWS_REGION}
client.create_bucket(Bucket="chucks3bucket",CreateBucketConfiguration=location)
