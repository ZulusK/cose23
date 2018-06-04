from bson.objectid import ObjectId
from flask_restful import Resource, abort
from db import TopicDB, CommentDB

db = TopicDB()
commentDb = CommentDB()


class TopicResource(Resource):
    def get(self, id):
        topic = db.get_by_id(id)
        if topic == None:
            abort(404, message='No such topic with id %s' % id)
        topic['num_of_messages'] = commentDb.count({'topic_id': ObjectId(id)})
        return topic


def config_topic_resources(api):
    api.add_resource(
        TopicResource,
        '/topic/<id>'
    )
