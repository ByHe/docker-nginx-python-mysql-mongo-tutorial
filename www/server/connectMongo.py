from pymongo import MongoClient

def getDB():
   client = MongoClient('mongodb://root:12345@mongodb')
   return client['world']