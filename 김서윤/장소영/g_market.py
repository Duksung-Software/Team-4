import scrapy
from G_market.items import GMarketItem


class GMarketSpider(scrapy.Spider):
    name = 'g_market'
    start_urls = ['https://browse.gmarket.co.kr/search?keyword=%eb%85%b8%ed%8a%b8%eb%b6%81&s=8']

    def parse(self, response):

        global url

        for i in range(1,101):

            URL = response.xpath(f'//*[@id="section__inner-content-body-container"]/div[2]/div[{i}]/div/div[2]/div[1]/div[1]/span/a')
            div =  response.xpath(f'//*[@id="section__inner-content-body-container"]/div[2]/div[{i}]')
            if (URL !=[]):
                href = div.xpath('./div/div[2]/div[1]/div[1]/span/a/@href')
                url = response.urljoin(href[0].extract())
                yield scrapy.Request(url, callback = self.page_content1)
            
            if (URL ==[]):
                href = div.xpath('./div/div[2]/div[1]/div[2]/span/a/@href')
                url = response.urljoin(href[0].extract())
                yield scrapy.Request(url, callback = self.page_content2)

    def page_content1(self, response):
        item = GMarketItem()
        Price_str = response.xpath('//*[@id="itemcase_basic"]/div[1]/p/span/strong/text()')[0].extract()
        Price_Num = Price_str.split(',')
        Price_List = ''.join(Price_Num)
        Price = int(Price_List)

        if(Price>300000):
            item['Name'] = response.xpath('//*[@id="itemcase_basic"]/div[1]/h1/text()')[0].extract()
            item['Price'] = response.xpath('//*[@id="itemcase_basic"]/div[1]/p/span/strong/text()')[0].extract()
            item['Delivery_Charge'] = response.xpath('//*[@id="container"]/div[3]/div[2]/div[2]/ul/li[1]/div[1]/div[2]/span/text()')[0].extract()
            item['URL'] = url
        return item

    

    def page_content2(self, response):
        item = GMarketItem()
        Price_str = response.xpath('//*[@id="itemcase_basic"]/div[1]/p/span/strong/text()')[0].extract()
        Price_Num = Price_str.split(',')
        Price_List = ''.join(Price_Num)
        Price = int(Price_List)

        if(Price>300000):
            item['Name'] = response.xpath('//*[@id="itemcase_basic"]/div[1]/h1/text()')[0].extract()
            item['Price'] = response.xpath('//*[@id="itemcase_basic"]/div[1]/p/span/strong/text()')[0].extract()
            item['Delivery_Charge'] = response.xpath('//*[@id="container"]/div[3]/div[2]/div[2]/ul/li[1]/div[1]/div[2]/span/text()')[0].extract()
            item['URL'] = url
        return item
       
