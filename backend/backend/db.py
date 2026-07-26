import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)

# Selecciona la base de datos
db = client['gestion_usuarios']
# Selecciona la colección
usuarios_collection = db['usuarios']
