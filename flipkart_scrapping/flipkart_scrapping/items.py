# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class FlipkartScrappingItem(Item):
    # define the fields for your item here like:
    # name = Field()
    text=Field()
    link=Field()
    
    pass
