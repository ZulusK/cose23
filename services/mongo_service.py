from pymongo import MongoClient
from models.message import Message


class MongoService:

    def __init__(self, collection):
        Client = MongoClient()
        db = Client["Cose2"]
        self.collection = db[collection]

    def insert(self, obj):
        if isinstance(obj, Message):
            self.collection.insert(obj.__dict__)
        else:
            print("wrong type")

    def get(self, key, value):
        response = []
        for rec in self.collection.find({key: value}):
            response.append(rec)
        return response

    def remove(self, id):
        self.collection.remove(id)

    def get_all(self):
        response = []
        for rec in self.collection.find():
            response.append(rec)
        return response

