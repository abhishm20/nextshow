# -*- coding: utf-8 -*-
import sqlite3 as lite
import os
from datetime import datetime

from settings import DB_PATH


class Pipeline(object):
    def __init__(self):
        self.connection = None
        self.cursor = None
        self.setup_connection()
        self.create_tables()

    def setup_connection(self):
        self.connection = lite.connect(DB_PATH)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        return self.cursor.execute("""
          CREATE TABLE IF NOT EXISTS `imdb_ids` (
              id INTEGER PRIMARY KEY NOT NULL,
              imdb_id TEXT NOT NULL,
              created_at DATETIME NOT NULL,
              is_used TINYINT(1) NULL DEFAULT 0);
        """)

    def close_connection(self):
        self.connection.close()

    def process_item(self, item, spider):
        item['created_at'] = str(datetime.now())
        item['is_used'] = str(False)
        self.store_in_db(item)
        return item

    def store_in_db(self, item):
        self.cursor.execute("\
                        INSERT INTO `imdb_ids`(\
                        imdb_id,\
                        is_used,\
                        created_at\
                        )\
                        VALUES (? , ? ,?)\
                    ", (item['imdb_id'], item['is_used'], item['created_at']))
        print 'stored in db', item
        self.connection.commit()

    def __del__(self):
        self.close_connection()
