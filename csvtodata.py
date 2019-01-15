import csv

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
    return row[0]

def getDate(row):
    return row[1]

def getOpen(row):
    return float(row[2])

def getHigh(row):
    return float(row[3])

def getLow(row):
    return float(row[4])

def getClose(row):
    return float(row[5])

def getVolume(row):
    return int(row[6])

def getValue(row):
    return float(row[7])

def getTrades(row):
    return int(row[8])

def getDataList(data, index):
    collect = []
    for row in data:
        element = row[index]
        collect.append(element)
    return collect

def getCodeList(data):
    return getDataList(data, 0)

def getDateList(data):
    return getDataList(data, 1)

def getOpenList(data):
    return getDataList(data, 2)

def getHighList(data):
    return getDataList(data, 3)

def getLowList(data):
    return getDataList(data, 4)

def getCloseList(data):
    return getDataList(data, 5)

def getVolumeList(data):
    return getDataList(data, 6)

def getValueList(data):
    return getDataList(data, 7)

def getTradesList(data):
    return getDataList(data, 8)

