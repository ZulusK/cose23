BOT_NAME = 'forum_spider'

SPIDER_MODULES = ['forum_spider.spiders']
NEWSPIDER_MODULE = 'forum_spider.spiders'
ROBOTSTXT_OBEY = True
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'
CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 1
COOKIES_ENABLED = False
ITEM_PIPELINES = {
    'forum_spider.pipelines.MongoPipeline': 300,
}
LOG_ENABLED=False