from bson.objectid import ObjectId
from .driver import DBDriver
from .driver import MONGODB_USER_COLLECTION


class UserDB(DBDriver):
    def __init__(self):
        DBDriver.__init__(self, MONGODB_USER_COLLECTION)

    def add_topic(self, id, topic_id):
        self.update_by_id(id, {'$push': {'topic_ids': ObjectId(topic_id)}})
