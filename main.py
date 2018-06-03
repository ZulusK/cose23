import services
from db.driver.db_driver import *

# load_comments()

commentsDB = DBDriver("comments")
data = commentsDB.get_all({'text': 1})[0:100]
comment_list = []
for record in data:
    comment_list.append(record["text"])
print("Fetched from DB")

data = list(services.normalize_data(comment_list))
print("Normalized")
services.generate_cloud(data)
