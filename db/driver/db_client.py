from pymongo import MongoClient
from .settings import MONGODB_URI, MONGODB_DATABASE


class DBClient:
    
    class _Client:
        def __init__(self):
            self.client = MongoClient(MONGODB_URI)
            self.db = self.client[MONGODB_DATABASE]

        def __del__(self):
            self.client.close()
    
    _instance = None
    
    def __init__(self):
        if not DBClient._instance:
            DBClient._instance = DBClient._Client()
    
    def get_collection(self, collection):
        return DBClient._instance.db[collection]