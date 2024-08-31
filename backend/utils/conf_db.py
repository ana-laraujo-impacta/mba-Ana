from pymongo import MongoClient
import certifi
import os
from dotenv import load_dotenv


load_dotenv()

def conf_db():
    mongodb_uri = os.getenv("MONGODB_URL")
    database_name = os.getenv("DATABASE_NAME")

    if not mongodb_uri or not database_name:
        raise ValueError("MONGODB_URL ou DATABASE_NAME não está definido no ambiente.")

    client = MongoClient(mongodb_uri, tlsCAFile=certifi.where())
    
    # Garantir que o nome do banco de dados seja uma string válida
    if not isinstance(database_name, str) or not database_name:
        raise TypeError("DATABASE_NAME deve ser uma string não vazia.")

    db = client[database_name]
    return db
