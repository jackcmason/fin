import csv
import datetime

CODE = 0
DATE = 1
OPEN = 2
HIGH = 3
LOW = 4
CLOSE = 5
VOLUME = 6
VALUE = 7
TRADES = 8

def csvToList(csvfile):
    with open(csvfile, 'r') as f:
        collect = []
        reader = csv.reader(f)
        for row in reader:
            collect.append(row)
    return collect

def getCode(row):
    return row[CODE]

def getDate(row):
    return time.strptime(row[DATE], "%d/%m/%Y")

def getOpen(row):
    return float(row[OPEN])

def getHigh(row):
    return float(row[HIGH])

def getLow(row):
    return float(row[LOW])

def getClose(row):
    return float(row[CLOSE])

def getVolume(row):
    return int(row[VOLUME])

def getValue(row):
    return float(row[VALUE])

def getTrades(row):
    return int(row[TRADES])

def getDataList(data, index):
    collect = []
    for row in data:
        if index == CODE:
            element = getCode(row)
        elif index == DATE:
            element = getDate(row)
        elif index == OPEN:
            element = getOpen(row)
        elif index == HIGH:
            element = getHigh(row)
        elif index == LOW:
            element = getLow(row)
        elif index == CLOSE:
            element = getClose(row)
        elif index == VOLUME:
            element = getVolume(row)
        elif index == VALUE:
            element = getValue(row)
        elif index == TRADES:
            element = getTrades(row)
        else:
            raise ValueError('index is out of range for data')
        collect.append(element)
    return collect

def getCodeList(data):
    return getDataList(data, CODE)

def getDateList(data):
    return getDataList(data, DATE)

def getOpenList(data):
    return getDataList(data, OPEN)

def getHighList(data):
    return getDataList(data, HIGH)

def getLowList(data):
    return getDataList(data, LOW)

def getCloseList(data):
    return getDataList(data, CLOSE)

def getVolumeList(data):
    return getDataList(data, VOLUME)

def getValueList(data):
    return getDataList(data, VALUE)

def getTradesList(data):
    return getDataList(data, TRADES)

