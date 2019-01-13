import csv

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
    return row[2]

def getHigh(row):
    return row[3]

def getLow(row):
    return row[4]

def getClose(row):
    return row[5]

def getVolume(row):
    return row[6]

def getValue(row):
    return row[7]

def getTrades(row):
    return row[8]

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

