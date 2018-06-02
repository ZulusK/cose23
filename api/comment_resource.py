import math
from flask_restful import Resource, reqparse
from bson.objectid import ObjectId
from db import CommentDB
from .settings import ITEMS_PER_PAGE

db = CommentDB()

class CommentResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=str)
        parser.add_argument('topic_id', type=str)
        parser.add_argument('page', type=int, default=0)
        args = parser.parse_args()

        comments = None
        if args['user_id'] != None and args['topic_id'] != None:
            comments = db.find({
                'user_id': ObjectId(args['user_id']),
                'topic_id': ObjectId(args['topic_id'])
            })
        elif args['user_id'] != None:
            comments = db.get_by_user_id(args['user_id'])
        elif args['topic_id'] != None:
            comments = db.get_by_topic_id(args['topic_id'])
        else:
            comments = db.get_all()
        
        responce = {}
        responce['page'] = args['page']
        responce['items_per_page'] = ITEMS_PER_PAGE
        responce['num_of_pages'] = math.ceil(len(comments) / ITEMS_PER_PAGE)

        first = args['page'] * ITEMS_PER_PAGE
        last = (args['page']+1) * ITEMS_PER_PAGE
        responce['comments'] = comments[first:last]

        return responce

def config_comment_resources(api):
    api.add_resource(
        CommentResource,
        '/comments'
    )