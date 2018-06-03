from scrapy.crawler import CrawlerProcess

import cose23.forum_spider.settings as crawler_settings
import cose23.forum_spider.spiders as ForumSpiders


def load_comments():
    process = CrawlerProcess(vars(crawler_settings))
    process.crawl(ForumSpiders.FlowerswebSpider)
    process.start()  # the script will block here until the crawling is finished
