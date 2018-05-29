from bson.objectid import ObjectId
from .driver import DBDriver
from .driver import MONGODB_USER_COLLECTION


class UserDB(DBDriver):
    def __init__(self):
        DBDriver.__init__(self, MONGODB_USER_COLLECTION)

    def insert(self, obj):
        obj['topic_ids'] = []
        return DBDriver.insert(self, obj)

    def add_topic(self, id, topic_id):
        topic_id = ObjectId(topic_id)
        user = self.get_by_id(id)
        for id in user['topic_ids']:
            if id == topic_id:
                return
        self.update_by_id(id, {'$push': {'topic_ids': ObjectId(topic_id)}})
