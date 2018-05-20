import json
from flask import (
    Flask,
    render_template
)
from services.mongo_service import MongoService
from models.message import Message

app = Flask(__name__)
db = MongoService("Posts")


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/posts/<author>', methods=['GET'])
def posts(author):
    posts = db.get('author', author)
    ps = []
    for post in posts:
        p = {}
        p['author'] = post.get('author')
        p['date'] = post.get('date')
        p['text'] = post.get('text')
        p['topic_id'] = post.get('topic_id')
        ps.append(p)
    return json.dumps(ps)