import scrapy

class QuotesSpider (scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall()
            }
        # 1st Option
        # for href in response.css('ul.pager a::attr(href)'):
        #     yield response.follow(href, callback=self.parse)

        # 2nd Option
        # for a in response.css('ul.pager a'):
        #     yield response.follow(a, callback=self.parse)

        # 3rd Option
        # anchors = response.css('ul.pager a')
        # yield from response.follow_all(anchors, callback=self.parse)

        # 4th Option
        yield from response.follow_all(css='ul.pager a', callback=self.parse)
