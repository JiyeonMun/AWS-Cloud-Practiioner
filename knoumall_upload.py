import os, uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

try:
  print("한국방송통신대학교 4학년 2학기 클라우드 컴퓨팅")
  connect_str = "DefaultEndpointsProtocol=https;AccountName=mallblobstorage0001;AccountKey=HVAc4DjBrA9JkYg7SKd02ccX5v5DXX0rEnNeb9G9ixQ/BA6OVg8Kk6MwV0o2zgDqvD5WQp1BFeakH7zn5gVyIw==;EndpointSuffix=core.windows.net"
  blob_service_client = BlobServiceClient.from_connection_string(connect_str)
  container_name = "mall-blob-container"

  local_file_name = "quickstart" + str(uuid.uuid4()) + ".txt" 
  upload_file_path = local_file_name
  
  file = open(upload_file_path,'w') 
  file.write("Hello, World!") 
  file.close( )

  blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
  
  print("\nUploading to Azure Storage as blob:\n\t" + local_file_name)

  # Upload the created file
  with open(upload_file_path, "rb") as data:
    blob_client.upload_blob(data)

except Exception as ex: 
  print('Exception:') 
  print(ex)