import scrapy
from scrapy.loader import ItemLoader

from product_scraper.items import *


class product_scraper_Spider(scrapy.Spider):
    name = "product_scraper"

    start_urls = ['https://www.lightinthebox.com/en/p/projector-screen-4k-movie-16-9-hd-60-72-84-100-120-150-inch'
                  '-foldable-and-portable-anti-crease-indoor-outdoor-projection-video-for-home-party-office_p8093466'
                  '.html?prm=1.3.0.2%27']

    def parse(self, response):
        with open('html_file.txt', 'w') as f:
            f.write(str(response.body))

        content_path = '//div[@id="product-info-line-2020"]'

        ## html path of the name
        name_path = content_path + '/div[@class="widget prod-info-title"]/text()'

        id_path = content_path + '/div[@class="widget prod-info-title"]/span/text()'

        price_path = content_path + '/div[@class="price-promotions-parent"]/div[@class="current-price-clearfix"]' \
                                    '/strong[@itemprop="price"]/text()'

        solded_path = content_path + '/div[@id="widget-info-parents"]/div[@id="prod-info-review"]/span[2]/text()'

        product_loader = ItemLoader(item=ProductScraperItem(), response=response)
        product_loader.add_xpath('name', name_path)
        product_loader.add_xpath('id', id_path)
        product_loader.add_xpath('current_price', price_path)
        product_loader.add_xpath('sold_pieces', solded_path)
        product_loader.load_item()

