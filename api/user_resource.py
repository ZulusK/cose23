from flask_restful import Resource, abort
from db import UserDB

db = UserDB()

class UserResource(Resource):
    def get(self, id):
        user = db.get_by_id(id)
        if user == None:
            abort(404, message='No such user with id %s' % (id))
        user.pop('topic_ids', None)
        return user

class UserTopicsResource(Resource):
    def get(self, id):
        user = db.get_by_id(id)
        if user == None:
            abort(404, message='No such user with id %s' % (id))
        return user['topic_ids']

def config_user_resources(api):
    api.add_resource(
        UserTopicsResource,
        '/user/<id>/topics'
    )
    api.add_resource(
        UserResource,
        '/user/<id>'
    )