# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BoardItem(scrapy.Item):
    Immobilientyp = scrapy.Field()
    Uberschrift = scrapy.Field()
    Kaufpreis = scrapy.Field()
    Telefon = scrapy.Field()
    PLZ = scrapy.Field()
    OBID = scrapy.Field()
    Stadt = scrapy.Field()
    Erstellungsdatum = scrapy.Field()
    Beschreibung = scrapy.Field()
