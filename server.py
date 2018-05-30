from flask import Flask, make_response
from flask_restful import Api, Resource
from api import JSONEncoder
from api import config_user_resources
from api import config_topic_resources
from api import config_comment_resources

app = Flask(__name__)
api = Api(app=app, default_mediatype='application/json')

@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(JSONEncoder.encode(data), code)
    resp.headers.extend(headers or {})
    return resp

config_user_resources(api)
config_topic_resources(api)
config_comment_resources(api)

if __name__ == "__main__":
    app.run(debug=True)