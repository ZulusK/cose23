from bson.objectid import ObjectId
from .driver import DBDriver
from .driver import MONGODB_COMMENT_COLLECTION


class CommentDB(DBDriver):

    def __init__(self):
        DBDriver.__init__(self, MONGODB_COMMENT_COLLECTION)

    def insert(self, obj):
        obj['user_id'] = ObjectId(obj['user_id'])
        obj['topic_id'] = ObjectId(obj['topic_id'])
        return DBDriver.insert(self, obj)

    def get_by_user_id(self, user_id):
        return self.find({'user_id': ObjectId(user_id)})

    def get_by_topic_id(self, topic_id):
        return self.find({'topic_id': ObjectId(topic_id)})
