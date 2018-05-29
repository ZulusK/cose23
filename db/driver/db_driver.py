from bson.objectid import ObjectId
from .db_client import DBClient


class DBDriver:
    
    def __init__(self, collection):
        self.collection = DBClient().get_collection(collection)
    
    def insert(self, obj):
        return self.collection.insert_one(obj).inserted_id

    def find(self, query):
        return self.collection.find(query)

    def get_all(self):
        return self.collection.find({})

    def get_by_id(self, id):
        return self.collection.find_one({u'_id': ObjectId(id)})

    def update_by_id(self, id, changes):
        self.collection.find_one_and_update({u'_id': ObjectId(id)}, changes)

    def drop(self):
        self.collection.drop()