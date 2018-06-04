from bson.objectid import ObjectId
from .db_client import DBClient


class DBDriver:

    def __init__(self, collection):
        self.collection = DBClient().get_collection(collection)

    def insert(self, obj):
        return self.collection.insert_one(obj).inserted_id

    def find(self, query, fields=None):
        return list(self.collection.find(query, fields))

    def find_one(self, query, fields=None):
        return self.collection.find_one(query, fields)

    def get_all(self, fields=None):
        return list(self.collection.find({}, fields))

    def get_by_id(self, id, fields=None):
        return self.collection.find_one({u'_id': ObjectId(id)}, fields)

    def update_by_id(self, id, changes):
        self.collection.find_one_and_update({u'_id': ObjectId(id)}, changes)

    def count(self, query):
        return self.collection.count(query)

    def drop(self):
        self.collection.drop()
