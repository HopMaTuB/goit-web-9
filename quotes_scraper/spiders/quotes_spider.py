import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'type': 'quote',
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
            author_url = quote.css('span a::attr(href)').get()
            if author_url:
                yield response.follow(author_url, callback=self.parse_author)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)

    def parse_author(self, response):
        yield {
            'type': 'author',
            'name': response.css('h3.author-title::text').get().strip(),
            'birthdate': response.css('span.author-born-date::text').get(),
            'bio': response.css('div.author-description::text').get().strip(),
        }
