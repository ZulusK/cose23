import services
from db.driver.db_driver import *

# from machinelearning.data_processor import *

# load_comments()

commentsDB = DBDriver("comments")
data = commentsDB.get_all()[0:10]
print(data[0].keys())
comment_list = []
for record in data:
    comment_list.append(record["text"])

data = services.normalize_data(comment_list)
print(list(data))
# ml_service = DataProcessor(normalization_service.normalize_text())

# ml_service.generate_cloud()
