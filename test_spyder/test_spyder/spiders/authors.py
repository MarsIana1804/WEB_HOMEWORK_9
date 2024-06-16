import scrapy


class AuthorsSpider(scrapy.Spider):
    name = "authors"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        pass

    def parse(self, response):
        # Follow links to author pages
        author_links = response.css('small.author ~ a::attr(href)').getall()
        for link in author_links:
            yield response.follow(link, self.parse_author)

        # Follow pagination links
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        yield {
            'fullname': response.css('h3.author-title::text').get().strip(),
            'born_date': response.css('span.author-born-date::text').get().strip(),
            'born_location': response.css('span.author-born-location::text').get().strip(),
            'description': response.css('div.author-description::text').get().strip(),
        }
