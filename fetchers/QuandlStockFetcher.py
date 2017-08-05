#!/usr/bin/python

import urllib
import os

class QuandlStockFetcher:

    def __init__(self, quandleWikiApiUrl, apiKey):
        self.quandleWikiApiUrl = quandleWikiApiUrl
        self.apiKey = apiKey
        self.dataDir = 'data'
        self.createDataDir()

    def fetchStockData(self, tickerSymbol):
        url = self.createApiUrl(tickerSymbol)
        fileName = self.createFileName(tickerSymbol)
        if not self.fileExists(fileName): 
            urllib.urlretrieve(url, fileName)
        return fileName
        
    def createDataDir(self):
        if not os.path.exists(self.dataDir):
            os.makedirs(self.dataDir)

    def fileExists(self, fileName):
        if os.path.exists(fileName):
            print 'File ' + fileName + ' exists, not fetching'
            return True
        print 'File ' + fileName + ' doesnt exists, fetching'
        return False

    def createApiUrl(self, tickerSymbol):
        url = self.quandleWikiApiUrl + '/' + tickerSymbol + '.csv?' + 'api_key=' + self.apiKey
        return url
    
    def createFileName(self, tickerSymbol):
        fileName = self.dataDir + '/' + tickerSymbol + '.csv'
        return fileName

