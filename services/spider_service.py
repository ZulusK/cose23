from scrapy.crawler import CrawlerProcess

import plants.settings as crawler_settings
import plants.spiders as ForumSpiders


def load_comments():
    process = CrawlerProcess(vars(crawler_settings))
    process.crawl(ForumSpiders.FlowerswebSpider)
    process.start()  # the script will block here until the crawling is finished
