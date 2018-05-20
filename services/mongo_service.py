from pymongo import MongoClient
from dbSettings import MONGODB_COLLECTION_NAME, MONGODB_DATABASE, MONGODB_URI
from models.message import Message


class MongoService:

    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        db = self.client[MONGODB_DATABASE]
        self.collection = db[MONGODB_COLLECTION_NAME]

    def insert(self, obj):
        if isinstance(obj, Message):
            self.collection.insert(obj.to_dict())
        else:
            print("wrong type")

    def get(self, key, value):
        response = []
        for rec in self.collection.find({key: value}):
            response.append(Message(**rec))
        return response

    def remove(self, id):
        self.collection.remove(id)

    def get_all(self):
        response = []
        for rec in self.collection.find():
            response.append(Message(**rec))
        return response

    def drop(self):
        self.collection.drop()

    def close(self):
        self.client.close()

