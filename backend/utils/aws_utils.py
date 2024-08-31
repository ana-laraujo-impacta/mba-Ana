import boto3
import os
from botocore.exceptions import NoCredentialsError


s3_client = boto3.client(
    's3',
    aws_access_key_id= os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key= os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name= os.getenv('REGION_NAME')
)

def upload_to_s3(file, bucket_name, s3_path):
    try:
        # Remover possíveis aspas duplas ou simples no caminho
        s3_path = s3_path.replace('"', '').replace("'", "")

        # Verificar se há barras adicionais ou ausentes e ajustar
        s3_client.upload_fileobj(file, bucket_name, s3_path)
        
        # Garantir que a URL esteja corretamente formatada
        url = f"https://{bucket_name}.s3.amazonaws.com/{s3_path}"
        return url
    except NoCredentialsError:
        return None
    

def delete_from_s3(bucket_name, s3_path):
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=s3_path)
    except NoCredentialsError:
        return None

def delete_folder_from_s3(bucket_name, folder_path):
    try:
        objects_to_delete = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=folder_path)
        delete_keys = {'Objects': [{'Key': obj['Key']} for obj in objects_to_delete.get('Contents', [])]}
        if delete_keys['Objects']:
            s3_client.delete_objects(Bucket=bucket_name, Delete=delete_keys)
    except NoCredentialsError:
        return None