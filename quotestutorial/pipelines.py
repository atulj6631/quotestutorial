# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import sqlite3
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotestutorialPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect('my_trial_db')
        self.curr = self.conn.cursor()
    
    def create_table(self):
        self.curr.execute("drop table if exists quotes_tb")
        self.curr.execute("create table quotes_tb (quotes text, author text)")

    def execute_statement(self, item):
        statement = "insert into quotes_tb values ( ?, ? )"
        self.curr.execute(statement, (item['quotes'], item['author']))
        self.conn.commit()

    def process_item(self, item, spider):
        self.execute_statement(item)
        return item
