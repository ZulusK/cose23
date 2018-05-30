from flask_restful import Resource, abort
from db import TopicDB

db = TopicDB()

class TopicResource(Resource):
    def get(self, id):
        topic = db.get_by_id(id)
        if topic == None:
            abort(404, message='No such topic with id %s' % id)
        return topic

def config_topic_resources(api):
    api.add_resource(
        TopicResource,
        '/topic/<id>'
    )