from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://root:12345@mongodb')
    return client['world']