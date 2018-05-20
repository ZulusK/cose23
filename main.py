from scrapy.crawler import CrawlerProcess

import plants.plants.spiders as ForumSpiders

process = CrawlerProcess({
    'USER_AGENT': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36"
})

process.crawl(ForumSpiders.FlowerswebSpider)
process.start()  # the script will block here until the crawling is finished

print("done")
