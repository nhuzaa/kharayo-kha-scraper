# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import firebase_admin
from firebase_admin import db

class FirebasePipeline:

    collection_name = 'news'

    def __init__(self):
        self.firebase = firebase_admin.initialize_app(options={
            'databaseURL': 'https://test1kharayo.firebaseio.com'
         })
        print('firebase', self.firebase.name)

        pass
    #
    def open_spider(self, spider):
        #  CONFIG_FIREBASE = spider.settings.get('CONFIG_FIREBASE')
        self.db = db.reference(self.collection_name)

    def close_spider(self, spider):
        pass
    def process_item(self, item, spider):
        self.db.push(dict(item))
        return item

