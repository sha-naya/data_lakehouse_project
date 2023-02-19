import boto3

s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id='', ### PUT ACCESS KEY HERE
    aws_secret_access_key='' ### PUT SECRET KEY HERE
)

for bucket in s3.buckets.all():
    print(bucket.name)

s3.Bucket('cs779').upload_file(Filename='av_vs_arsenal.jpeg', Key='av_vs_arsenal.jpeg')
