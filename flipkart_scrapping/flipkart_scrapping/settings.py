# Scrapy settings for flipkart_scrapping project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'flipkart_scrapping'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['flipkart_scrapping.spiders']
NEWSPIDER_MODULE = 'flipkart_scrapping.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

