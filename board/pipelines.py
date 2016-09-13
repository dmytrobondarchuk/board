# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3
import os


class BoardPipeline(object):
    """ Itsy Bitsy Spider creates the sqlite3 database if one not exists
    and save items into it """

    def __init__(self):
        if not os.path.isfile('scrapped_data.db'):
            self.conn = sqlite3.connect('scrapped_data.db')
            c = self.conn.cursor()
            c.execute('''CREATE TABLE parsed_data
                 (Immobilientyp text,
                 Uberschrift text,
                 Kaufpreis text,
                 Telefon text,
                 PLZ text,
                 OBID text,
                 Stadt text,
                 Erstellungsdatum text,
                 Beschreibung text)''')
        else:
            self.conn = sqlite3.connect('scrapped_data.db')

    def process_item(self, item, spider):
        c = self.conn.cursor()
        Immobilientyp = item["Immobilientyp"]
        Uberschrift = item["Uberschrift"]
        try:
            Kaufpreis = str(item["Kaufpreis"])[:-2]
        except:
            Kaufpreis = item["Kaufpreis"]
        Telefon = item["Telefon"]
        PLZ = item["PLZ"]
        OBID = item["OBID"]
        Stadt = item["Stadt"]
        Erstellungsdatum = item["Erstellungsdatum"]
        Beschreibung = item["Beschreibung"]

        purchases = (Immobilientyp,
                     Uberschrift,
                     Kaufpreis,
                     Telefon,
                     PLZ,
                     OBID,
                     Stadt,
                     Erstellungsdatum,
                     Beschreibung)

        c.execute('''INSERT INTO parsed_data
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', purchases)
        self.conn.commit()
        self.conn.close()

        return item
