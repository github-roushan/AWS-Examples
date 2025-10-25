import boto3

client = boto3.client("s3")

response = client.create_bucket(
    Bucket = 'test-rous-123123',
    CreateBucketConfiguration = {
        'LocationConstraint': 'ap-south-1'
    }
)

print(response)