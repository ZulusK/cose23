from bson.objectid import ObjectId
from .driver import DBDriver
from .driver import MONGODB_TOPIC_COLLECTION


class TopicDB(DBDriver):

    def __init__(self):
        DBDriver.__init__(self, MONGODB_TOPIC_COLLECTION)
