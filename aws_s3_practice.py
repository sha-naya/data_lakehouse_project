import boto3
import pandas as pd
import configparser

config = configparser.ConfigParser()
config.read("/Users/ayan/Desktop/BU/Spring 2023/cs779_keys.ini")

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id=config['s3']['access_key'],
    aws_secret_access_key=config['s3']['secret_key'],
)

for bucket in s3.buckets.all():
    print(bucket.name)

s3.Bucket('cs779').upload_file(Filename='av_vs_arsenal.jpeg', Key='av_vs_arsenal.jpeg')

s3_object = s3.Bucket('cs779').Object('BostonHousing.csv').get()
boston_housing_data = pd.read_csv(s3_object['Body'], index_col=0)
print(len(boston_housing_data))
