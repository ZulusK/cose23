from . import CommentDB, TopicDB, UserDB


class DBLoader:
    def __init__(self):
        self.comment_db = CommentDB()
        self.topic_db = TopicDB()
        self.user_db = UserDB()

    def add_comment(self, comment_desc):
        user_desc = {
            'name': comment_desc['author_name'],
            'id_from_forum': comment_desc['author_id']
        }
        user = self.user_db.find_one(user_desc)
        user_id = None
        if user != None:
            user_id = user['_id']
        else:
            user_id = self.user_db.insert(user_desc)
        topic_desc = {
            'name': comment_desc['topic_name'],
            'url': comment_desc['url']
        }
        topic = self.topic_db.find_one(topic_desc)
        topic_id = None
        if topic != None:
            topic_id = topic['_id']
        else:
            topic_id = self.topic_db.insert(topic_desc)
        self.user_db.add_topic(user_id, topic_id)
        comment = {
            'id_from_forum': comment_desc['message_id'],
            'text': comment_desc['message_text'],
            'date': comment_desc['date'],
            'user_id': user_id,
            'topic_id': topic_id
        }
        self.comment_db.insert(comment)

    def drop_dbs(self):
        self.comment_db.drop()
        self.topic_db.drop()
        self.user_db.drop()
