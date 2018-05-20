from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
from scrapy.spiders import CrawlSpider


class FlowerswebSpider(CrawlSpider):
    comment_xpath = "//table[contains(@class,'forum-post-table')]"
    fields = {
        'author_name': './@bx-author-name',
        'author_id': './@bx-author-id',
        'date': './/td[contains(@class,"forum-cell-post")]//*[contains(@class,"forum-post-date")]/span/text()',
        'message_text': './/div[@class="forum-post-entry"]/div[@class="forum-post-text"]/text()',
        'message_id': './/div[@class="forum-post-entry"]/div[@class="forum-post-text"]/@id',
    }
    name = 'flowersweb'
    allowed_domains = ['flowersweb.info']
    start_urls = ['http://flowersweb.info/forum/forum1/']
    host = 'http://flowersweb.info'

    def parse(self, response):
        #next_page = response.xpath('//a[contains(@class,"forum-page-next")]/@href')
        return self.parse_forum(response)
        # yield response.follow(response.urljoin(next_page.extract_first()))

    def parse_forum(self, response):
        """
        Used for parsing page with threads names and following links at this page
        :param response:
        :return:
        """
        # find all links at page
        thread_links = [a.extract() for a in response.xpath('//span[contains(@class,"forum-item-title")]/a/@href')]
        # get next page URL
        print("I have found %d treads's links at page %s" % (len(thread_links), response.url))
        for thread_link in thread_links:
            try:
                # follow link
                yield response.follow(response.urljoin(thread_link), self.parse_thread)
            except Exception as e:
                print("Error\n" + e)

    def parse_comment(self, comment, url):
        """
        parse single post from forum
        :param comment: xpath selector with post
        :param url url from which comment has crawled
        :return: parsed PostItem
        """
        d = {}
        for name, xpath in self.fields.items():
            d[name] = comment.xpath(xpath).extract_first()
        d['url'] = url
        return d

    def parse_thread(self, response):
        """
        parse single page from forum
        :param response: response from web-site
        :return: list with post from page
        """

        # extract all comments from page
        comments_list = response.xpath(self.comment_xpath)
        print("Find %d comments at page %s" % (len(comments_list), response.url))
        # parse all comments
        for comment in comments_list:
            yield self.parse_comment(comment, response.url)
        # find link to next page and follow it
        try:
            next_page = response.xpath('//a[contains(@class,"forum-page-next")]/@href').extract_first()
            if next_page:
                yield response.follow(response.urljoin(next_page), callback=self.parse_thread)
        except Exception as e:
            print(e)
