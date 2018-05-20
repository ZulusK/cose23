BOT_NAME = 'plants'
SPIDER_MODULES = ['plants.spiders']
NEWSPIDER_MODULE = 'plants.spiders'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36'
# ROBOTSTXT_OBEY = True
CONCURRENT_REQUESTS = 32
DOWNLOAD_DELAY = 1
COOKIES_ENABLED = False
ITEM_PIPELINES = {
    'plants.pipelines.MongoPipeline': 300,
}
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = 'plants-comments'
LOG_ENABLED=False