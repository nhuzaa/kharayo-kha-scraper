import scrapy

from scraper.items import News

class EkantipurSpider(scrapy.Spider):
    name = 'ekantipur'
    allowed_domains = ['ekantipur.com']
    start_urls = ['http://ekantipur.com/']

    def parse(self, response):
        featuredNews = []
        #  fn  = response.css('section.main-news').xpath('/article/h1/a').get()
        fn  = response.css('section.main-news').xpath('article/h1/a')

        #  print(response.url)
        #  print(response.status)
        #  print(fn)
        for n in fn:
            n_url = n.attrib['href']
            print('####URL', n_url)
            yield scrapy.Request(n_url, callback= self.single_news)


    def single_news(self, response):
        n =  News()
        n['url'] = response.url
        n['title']= response.css('div.article-header').xpath('h1/text()').get()
        print(n['title'])
        n['excrept']= response.css('div.description').xpath(('p/text()')).get()
        yield n

