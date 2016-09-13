# -*- coding: utf-8 -*-

import scrapy
from board.items import BoardItem


class ItsyBitsySpiderSpider(scrapy.Spider):
    name = "itsy_bitsy_spider"
    allowed_domains = ["www.quoka.de/"]

    start_urls = ["http://www.quoka.de/immobilien/bueros-gewerbeflaechen/c2710a171465245/gewerbeeinheit-mit-340m2-vermieten.html",
                  ]

    def parse(self, response):

        item = BoardItem()

        try:
            Immobilientyp = response.xpath(
                './/span[@itemprop="title"]//span[@class="category"]')[1].xpath(
                "text()").extract_first()
            item["Immobilientyp"] = Immobilientyp
        except:
            item["Immobilientyp"] = "Error! I could not parse this data"

        try:
            item["Uberschrift"] = response.css(
                ".headline>h1").xpath("text()").extract_first()
        except:
            item["Uberschrift"] = "Error! I could not parse this data"

        try:
            item["Kaufpreis"] = response.css(
                ".price.has-type>strong>span").xpath("text()").extract_first()
        except:
            item["Kaufpreis"] = "Error! I could not parse this data"

        try:
            item["Telefon"] = response.xpath(
                './/*[@id="Handy1"]/span/text()').extract_first()
        except:
            item["Telefon"] = "Error! I could not parse this data"

        try:
            item["PLZ"] = response.xpath(
                '//main').css(
                "span.postal-code")[0].xpath('text()').extract_first()
        except:
            item["PLZ"] = "Error! I could not parse this data"

        try:
            item["OBID"] = response.css(
                '.date-and-clicks').xpath('strong/text()').extract_first()
        except:
            item["OBID"] = "Error! I could not parse this data"

        try:
            item["Stadt"] = response.xpath(
                '//main').css('.locality')[0].xpath('text()').extract_first()
        except:
            item["Stadt"] = "Error! I could not parse this data"

        try:
            item["Erstellungsdatum"] = response.xpath(
                '//main').css('.today')[0].xpath('text()').extract()
        except:
            item["Erstellungsdatum"] = "Error! I could not parse this data"

        try:
            item["Beschreibung"] = ' '.join(response.xpath(
                '//main').css('.text')[0].xpath('text()').extract())
        except:
            item["Beschreibung"] = "Error! I could not parse this data"

        return item
