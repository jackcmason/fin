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
