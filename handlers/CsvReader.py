#!/usr/bin/python

import csv
import re
import uuid
from datetime import datetime
from Stock import Stock

class CsvReader():
    regexToReplace = '(\.\s)|(\.)' 
    replaceChars = '_'

    def __init__(self, regexToReplace=None, replaceChars=None):
        if regexToReplace is not None:
            CsvReader.regexToReplace = regexToReplace
        if replaceChars is not None:
            CsvReader.replaceChars = replaceChars
    
    def fetchCsvContent(self, fileName):
        data = csv.reader(open(fileName), delimiter=',')
        fields = data.next()
        json = []
        for row in data:
            fields = self.lowerCaseFieldNames(fields)
            fields = self.replaceRegex(CsvReader.regexToReplace, CsvReader.replaceChars, fields)
            items = zip(fields, row)
            item = self.handleRowContent(items)
            json.append(item)
        return json
    
    def handleRowContent(self, items):
        item = {}
        for (name, value) in items:
            item[name] = value.strip()
        item['timestamp'] = datetime.now()
        return item
    
    def lowerCaseFieldNames(self, fields):
        return [field.lower() for field in fields]

    def replaceRegex(self, regexToReplace, replaceChar, fields):
        return [re.sub(regexToReplace, replaceChar, field) for field in fields]

