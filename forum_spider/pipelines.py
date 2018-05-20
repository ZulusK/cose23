import pymongo
from services.mongo_service import MongoService
from models.message import Message


class MongoPipeline(object):

    def open_spider(self, spider):
        self.db = MongoService()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        self.db.insert(Message(**item))
        return item