import json


class Message():
    def __init__(self, author_name, author_id, date, message_text, message_id, url):
        self.author_name = author_name
        self.author_id = author_id
        self.date = date
        self.message_text = message_text
        self.message_id = message_id
        self.url = url

    def to_dict(self):
        return vars(self)

    @staticmethod
    def toJSON(var):
        if var is Message:
            return json.dumps(var.to_dict())
        else:
            dicts = []
            for v in var:
                dicts.append(v.to_dict())
            return json.dumps(dicts)

