#!/usr/bin/env/python
import boto3
import logging
from botocore.exceptions import ClientError
from botocore.client import Config

config = Config(
   signature_version = 's3v4'
)

s3 = boto3.resource('s3',
                    endpoint_url='https://weka:9000',
                    aws_access_key_id='s3_key',
                    aws_secret_access_key='s3_secret',
                    config=config)

try:
  # upload a file from local file system 'myfile' to bucket 'mybucket' with 'my_uploaded_object' as the object name.
  s3.Bucket('mybucket').upload_file('myfile','my_uploaded_object')

  # download the object 'piano.mp3' from the bucket 'songs' and save it to local FS as /tmp/classical.mp3
  s3.Bucket('mybucket').download_file('my_uploaded_object', 'my_downloaded_object')

except ClientError as e:
        logging.error(e)

print ("Downloaded 'my_downloaded_object' as 'my_uploaded_object'. ")
"""with open('readme.txt', 'w') as f:
      f.write('readme')
      f.write('\nthis is my json file')"""

"""
client = boto3.client('ec2')

client = boto3.client('ec2', region_name='us-east-2')

response = client.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '',
            'Ebs': {

                'DeleteOnTermination': True,
                'VolumeSize': 8,
                'VolumeType': 'gp2'
            },
        },
    ],
    ImageId='ami-08e2d37b6a0129927',
    InstanceType='t2.micro',
    KeyName= 'vokey',
    MaxCount=1,
    MinCount=1,
    Monitoring={
        'Enabled': False
    },
)
import boto3
"""