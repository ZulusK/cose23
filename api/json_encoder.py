import json
from bson.objectid import ObjectId


class JSONEncoder():

    @staticmethod
    def _convertObjectId(obj):
        r = None
        if isinstance(obj, ObjectId):
            r = str(obj)
        elif isinstance(obj, list):
            r = list()
            for o in obj:
                r.append(JSONEncoder._convertObjectId(o))
        elif isinstance(obj, dict):
            r = dict()
            for key in obj.keys():
                r[key] = JSONEncoder._convertObjectId(obj[key])
        else:
            r = obj
        return r

    @staticmethod
    def encode(data):
        return json.dumps(JSONEncoder._convertObjectId(data))
