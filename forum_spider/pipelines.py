import pymongo
from db import DBLoader


class MongoPipeline(object):

    def open_spider(self, spider):
        self.db_loader = DBLoader()
        self.db_loader.drop_dbs()

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        self.db_loader.add_comment(item)
        return item