import boto3

s3 = boto3.client('s3')
file = s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')
print(file)

# # if the file is a writable file-like object, you can use the following code:
# s3 = boto3.client('s3')
# with open('FILE_NAME', 'wb') as f:
#     s3.download_fileobj('BUCKET_NAME', 'OBJECT_NAME', f)

