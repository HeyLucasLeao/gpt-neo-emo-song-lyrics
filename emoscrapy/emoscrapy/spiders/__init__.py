# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.


import scrapy

class EmoScrapy(scrapy.Spider):
    name = 'letras'
    banda = 'evanescence'
    start_urls = [f'https://www.letras.mus.br/{banda}/']

    def parse(self, response):
        for link in response.css('a.song-name::attr(href)'):
            yield response.follow(link.get(), callback=self.parse_lyrics)

    def parse_lyrics(self, response):
        yield {
            'titulo': response.css('h1::text').get(),
            'letra': response.css('div.cnt-letra.p402_premium p::text').getall(),
            'link': response.url,
        }