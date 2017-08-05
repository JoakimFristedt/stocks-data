#!/usr/bin/python

from elasticsearch import Elasticsearch, helpers
from datetime import datetime

class ElasticsearchWriter():

    def __init__(self, elasticUrl, indexName, docType):
        self.elasticUrl = elasticUrl
        self.es = Elasticsearch(elasticUrl)
        self.indexName = indexName
        self.docType = docType

    def bulk(self, stock):
        bulkData = []
        for item in stock.stockData:
            itemWithFields = self.addFields(item, stock)
            bulkData.append(itemWithFields)
        print 'Adding stock data for ' + stock.tickerSymbol
        res = helpers.bulk(self.es, stock.stockData)

    def addFields(self, item, stock):
        item['_type'] = self.docType
        item['_index'] = self.indexName
        item['ticker_symbol'] = stock.tickerSymbol
        return item

