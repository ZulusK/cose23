import math
import datetime
import functools
from flask_restful import Resource, reqparse
from bson.objectid import ObjectId
from db import CommentDB, UserDB, TopicDB
from .settings import ITEMS_PER_PAGE

db = CommentDB()
userDb = UserDB()
topicDb = TopicDB()

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
        responce['total_num_of_items'] = len(responce)

        first = args['page'] * ITEMS_PER_PAGE
        last = (args['page']+1) * ITEMS_PER_PAGE
        responce['comments'] = comments[first:last]

        for r in responce['comments']:
            r['user_name'] = userDb.get_by_id(r['user_id'])['name']
            r['topic_name'] = userDb.get_by_id(r['topic_id'])['name']

        return responce

class CommentCountResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=str)
        parser.add_argument('topic_id', type=str)
        args = parser.parse_args()

        query = {}
        if args['user_id'] != None:
            query['user_id'] = ObjectId(args['user_id'])
        if args['topic_id'] != None:
            query['topic_id'] = ObjectId(args['topic_id'])

        return db.count(query)

class CommentTimestampResource(Resource):

    def get(self):
        parcer = reqparse.RequestParser()
        parcer.add_argument('user_id', default=None)
        parcer.add_argument('topic_id', default=None)
        args = parcer.parse_args()

        query = {}
        if args['user_id'] != None:
            query['user_id'] = ObjectId(args['user_id'])
        if args['topic_id'] != None:
            query['topic_id'] = ObjectId(args['topic_id'])

        comments = db.find(query)
        responce = []

        for comment in comments:
            date = comment['date'][:comment['date'].find(' ')]
            finded_indexes = [i for i,x in enumerate(responce) if x['date'] == date]
            index = None
            if len(finded_indexes) == 0:
                responce.append({
                    'date': date,
                    'count': 0
                })
                index = len(responce) - 1
            else:
                index = finded_indexes[0]
            responce[index]['count'] += 1

        return sorted(responce, key=functools.cmp_to_key(compare_date))

class CommentTopUsers(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('topic_id', type=str)
        topic_id = parser.parse_args()['topic_id']

        comments = None
        if topic_id != None:
            comments = db.get_by_topic_id(topic_id)
        else:
            comments = db.get_all()

        responce = []

        for comment in comments:
            user_id = comment['user_id']
            finded_indexes = [i for i,x in enumerate(responce) if x['user_id'] == user_id]
            index = None
            if len(finded_indexes) == 0:
                responce.append({
                    'user_id': user_id,
                    'count': 0,
                    'user_name': userDb.get_by_id(user_id)['name']
                })
                index = len(responce) - 1
            else:
                index = finded_indexes[0]
            responce[index]['count'] += 1

        return sorted(responce, key=lambda x: x['count'], reverse=True)

class CommentTopTopics(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=str)
        user_id = parser.parse_args()['user_id']

        comments = None
        if user_id != None:
            comments = db.get_by_user_id(user_id)
        else:
            comments = db.get_all()

        responce = []

        for comment in comments:
            topic_id = comment['topic_id']
            finded_indexes = [i for i,x in enumerate(responce) if x['topic_id'] == topic_id]
            index = None
            if len(finded_indexes) == 0:
                responce.append({
                    'topic_id': topic_id,
                    'count': 0,
                    'topic_name': topicDb.get_by_id(topic_id)['name']
                })
                index = len(responce) - 1
            else:
                index = finded_indexes[0]
            responce[index]['count'] += 1

        return sorted(responce, key=lambda x: x['count'], reverse=True)

def str_to_datetime(date_str):
    date = {}
    strs = date_str.split('.')
    date['year'] = int(strs[2])
    date['month'] = int(strs[1])
    date['day'] = int(strs[0])
    return date

def compare_date(obj1, obj2):
    date1 = str_to_datetime(obj1['date'])
    date2 = str_to_datetime(obj2['date'])
    if date1['year'] == date2['year']:
        if date1['month'] == date2['month']:
            return date1['day'] - date2['day']
        return date1['month'] - date2['month']
    return date1['year'] - date2['year']

def config_comment_resources(api):
    api.add_resource(CommentResource, '/comments')
    api.add_resource(CommentTimestampResource, '/comments/timestamp')
    api.add_resource(CommentTopTopics, '/comments/top/topics')
    api.add_resource(CommentTopUsers, '/comments/top/users')
    api.add_resource(CommentCountResource, '/comments/count')