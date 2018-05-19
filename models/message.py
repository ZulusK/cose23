import json


class Message():
    def __init__(self, author, date, text, topic_id):
        self.author = author
        self.date = date
        self.text = text
        self.topic_id = topic_id

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=1)
