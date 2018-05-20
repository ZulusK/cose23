import scrapy


class CommentItem(scrapy.Item):
    """
        define item structure of comment at forum
    """
    author_id = scrapy.Field()
    author_name = scrapy.Field()
    date = scrapy.Field()
    message_text = scrapy.Field()
    message_id = scrapy.Field()
    url = scrapy.Field()
    topic_id = scrapy.Field()
