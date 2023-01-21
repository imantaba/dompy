import boto3

# s3 = boto3.client('s3')
# response = s3.list_buckets()

# # Output the bucket names
# print('Existing buckets:')
# for bucket in response['Buckets']:
#     print(f'  {bucket["Name"]}')

# BUCKET_NAME="social-nightly"
# KEY="images/55b5a00921574253a8998c28ba35e7e5.png"

# s3 = boto3.resource('s3')
# s3.Bucket(BUCKET_NAME).download_file(KEY, 'my-local-image.png')

s3 = boto3.client('s3')
bucket_name="social-nightly"
response = s3.list_objects_v2(Bucket=bucket_name)
files = response.get("Contents")
for file in files:
    key = file['Key']
    if key.startswith("0Gor"):
        print(key)