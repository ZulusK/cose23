import json
from flask import (
    Flask,
    render_template
)
from services.mongo_service import MongoService
from models.message import Message

app = Flask(__name__)
db = MongoService()


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/posts/<author>', methods=['GET'])
def posts(author):
    posts = db.get('author_name', author)
    return Message.toJSON(posts)