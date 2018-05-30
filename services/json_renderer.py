import json
from bson.objectid import ObjectId
from flask_api import renderers


class JSONRenderer(renderers.BaseRenderer):
    media_type = 'application/json'

    def _convertObjectId(self, obj):
        if isinstance(obj, ObjectId):
            obj = str(obj)
        elif isinstance(obj, list):
            for o in obj:
                o = self._convertObjectId(o)
        elif isinstance(obj, dict):
            for key in obj.keys():
                obj[key] = self._convertObjectId(obj[key])
        return obj

    def render(self, data, media_type, **options):
        data = self._convertObjectId(data)
        return json.dumps(data)
