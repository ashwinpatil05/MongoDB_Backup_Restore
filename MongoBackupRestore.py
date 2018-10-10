from bson import BSON, decode_all
from pymongo import MongoClient

client = MongoClient()
source_collection = client.db.collection

# Dump.
with open('file.bson', 'wb+') as f:
    for doc in source_collection.find():
        f.write(BSON.encode(doc))

# Restore.
target_collection = client.db.collection
with open('file.bson', 'rb') as f:
    target_collection.insert(decode_all(f.read()))
