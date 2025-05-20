import scrapy


class PhilConcertSpiderSpider(scrapy.Spider):
    name = 'phil_concert_spider'

    def start_requests(self):

            # GET request
            yield scrapy.Request("https://quotes.toscrape.com/js/",
            meta={"playwright": True})

            # POST request
            #yield scrapy.FormRequest(
            #    url="https://httpbin.org/post",
            #    formdata={"foo": "bar"},
            #    meta={"playwright": True},
            #)

    def parse(self, response):
            # 'response' contains the page as seen by the browser
            for quote in response.css('div.quote'):
                quote_item = QuoteItem()
                quote_item['text'] = quote.css('span.text::text').get()
                quote_item['author'] = quote.css('small.author::text').get()
                quote_item['tags'] = quote.css('div.tags a.tag::text').getall()

                yield quote_item