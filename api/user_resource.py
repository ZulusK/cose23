import math
from bson.objectid import ObjectId
from flask_restful import Resource, abort, reqparse
from db import UserDB, CommentDB
from .settings import ITEMS_PER_PAGE

db = UserDB()
commentDb = CommentDB()


class UserResource(Resource):
    def get(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('topic_id', type=str)
        args = parser.parse_args()

        query = {
            'user_id': ObjectId(id)
        }
        if args['topic_id'] != None:
            query['topic_id'] = ObjectId(args['topic_id'])

        user = db.get_by_id(id)
        if user == None:
            abort(404, message='No such user with id %s' % (id))
        user['num_of_topics'] = len(user['topic_ids'])
        user.pop('topic_ids', None)
        user['num_of_messages'] = commentDb.count(query)
        return user


class UserTopicsResource(Resource):
    def get(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, default=0)
        args = parser.parse_args()

        user = db.get_by_id(id)
        if user == None:
            abort(404, message='No such user with id %s' % (id))

        responce = {}
        responce['items_per_page'] = ITEMS_PER_PAGE
        responce['page'] = args['page']
        responce['num_of_pages'] = math.ceil(
            len(user['topic_ids'] / ITEMS_PER_PAGE))
        responce['total_num_of_items'] = len(user['topic_ids'])

        first = args['page'] * ITEMS_PER_PAGE
        last = (args['page'] + 1) * ITEMS_PER_PAGE
        responce['topic_ids'] = user['topic_ids'][first:last]
        return responce


def config_user_resources(api):
    api.add_resource(
        UserTopicsResource,
        '/user/<id>/topics'
    )
    api.add_resource(
        UserResource,
        '/user/<id>'
    )
