#!/usr/bin/python

from fetchers.QuandlStockFetcher import QuandlStockFetcher
from handlers.CsvReader import CsvReader
from utils.Stock import Stock
from writers.ElasticsearchWriter import ElasticsearchWriter

quandlStockApiUrl = 'https://www.quandl.com/api/v3/datasets/WIKI'
apiKey = ''

fetcher = QuandlStockFetcher(quandlStockApiUrl, apiKey)
csvReader = CsvReader()
es = ElasticsearchWriter('http://localhost:9200', 'stocks', 'default')

stocks = ['AAPL', 'TSLA']

for ticker in stocks:
    stockDataFile = fetcher.fetchStockData(ticker)
    data = csvReader.fetchCsvContent(stockDataFile)
    stock = Stock(ticker, data)
    es.bulk(stock)

