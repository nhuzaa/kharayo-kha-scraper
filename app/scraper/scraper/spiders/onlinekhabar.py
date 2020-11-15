import scrapy

from scraper.items import News

class OnlinekhabarSpider(scrapy.Spider):
    name = 'onlinekhabar'
    allowed_domains = ['onlinekhabar.com']
    start_urls = ['http://onlinekhabar.com/']

    def parse(self, response):
        featuredNews = []
        fn  = response.xpath('/html/body/div[5]/div[4]/div[1]/main/section').css('a.title__large')
        fnb  = response.xpath('/html/body/div[5]/div[4]/div[1]/main/section').css('a.title__medium')
        # Extending the list 
        fn.extend(fnb)
        for n in fn:
            n_url = n.attrib['href']
            yield scrapy.Request(n_url, callback= self.single_news)


    def single_news(self, response):
        n =  News()
        n['url'] = response.url
        n['title']= response.xpath('//*[@id="main"]/section/div/div[1]/h2/text()').get()
        #  print(n['title'])
        n['excrept']= response.xpath('//*[@id="main"]/section/div/div[2]/div/div/div[4]/p/text()').get()
        yield n

