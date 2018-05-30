from flask_restful import Resource, reqparse
from bson.objectid import ObjectId
from db import CommentDB

db = CommentDB()
num_of_items_on_page = 10

class CommentResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=str)
        parser.add_argument('topic_id', type=str)
        parser.add_argument('page', type=int, default=0)
        args = parser.parse_args()

        first = args['page']*num_of_items_on_page
        last = (args['page']+1)*num_of_items_on_page
        comments = None
        if args['user_id'] != None and args['topic_id'] != None:
            comments = db.find({
                'user_id': ObjectId(args['user_id']),
                'topic_id': ObjectId(args['topic_id'])
            })[first:last]
        elif args['user_id'] != None:
            comments = db.get_by_user_id(args['user_id'])[first:last]
        elif args['topic_id'] != None:
            comments = db.get_by_topic_id(args['topic_id'])[first:last]
        else:
            comments = db.get_all()[first:last]

        return comments

def config_comment_resources(api):
    api.add_resource(
        CommentResource,
        '/comments'
    )