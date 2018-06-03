from cose23.services import load_comments
from cose23.db.driver.db_driver import *
from cose23.services.normalization_service import *
from cose23.machinelearning.data_processor import *

# load_comments()

dbdriver = DBDriver("comments")
data = dbdriver.get_all()
comment_list = []
for record in data:
    comment_list.append(record["text"])

normalization_service = NormalizationService(comment_list)
ml_service = DataProcessor(normalization_service.normalize_text())

ml_service.generate_cloud()
