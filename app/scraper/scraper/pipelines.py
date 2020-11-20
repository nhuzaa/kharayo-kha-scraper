# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import firebase_admin
from firebase_admin import firestore

import datetime


class FirebasePipeline:


    def __init__(self):
        self.firebase = firebase_admin.initialize_app(options={ 'projectId': 'test1kharayo' })
        print('firebase', self.firebase.name)
        self.collection_name = 'featured_news'
        print(self.collection_name)
        pass

    def open_spider(self, spider):
        #  CONFIG_FIREBASE = spider.settings.get('CONFIG_FIREBASE')
        store = firestore.client()
        self.db = store.collection(self.collection_name) 

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        uuid = item['url'].rsplit('/', 1)[-1]
        x = datetime.datetime.now()
        date = x.strftime("%m-%d-%Y")
        self.db.document(spider.name).collection(date).document(uuid).set(dict(item))
        return item

