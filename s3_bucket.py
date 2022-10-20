import json
import boto3

s3 = boto3.resource("s3")

def upload_joke_s3(joke_data_to_save):
    with open("joke.json", "w") as file:
            file.write(json.dumps(joke_data_to_save))
    s3.meta.client.upload_file('joke.json', 'chucks3bucketvenv', 'joke.json')












"""import boto3

AWS_REGION = "us-east-2"
client = boto3.client('s3',region_name=AWS_REGION)
location = {'LocationConstraint': AWS_REGION}
client.create_bucket(Bucket="chucks3bucket",CreateBucketConfiguration=location)
"""