import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Step 1: List all buckets
print("S3 Buckets:")
response = s3.list_buckets()
for bucket in response['Buckets']:
    print(f" - {bucket['Name']}")

# Step 2: Upload a file
file_name = "sample.txt"
bucket_name = "mybuctask"  # Make sure this is your actual bucket name
object_name = "sample.txt"  # This will be the name in the bucket

try:
    s3.upload_file(file_name, bucket_name, object_name)
    print(f"\n✅ Uploaded {file_name} to bucket {bucket_name} as {object_name}")
except Exception as e:
    print(f"\n❌ Upload failed: {e}")
# Download the file from S3
s3.download_file(bucket_name, object_name, 'downloaded_sample.txt')
print(f"✅ Downloaded {object_name} from bucket {bucket_name} as downloaded_sample.txt")
# Delete the file from the S3 bucket
s3.delete_object(Bucket=bucket_name, Key=object_name)
print(f"✅ Deleted {object_name} from bucket {bucket_name}")

