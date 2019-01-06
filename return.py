import csv

def csvToList(csvfile):
    with open(csvfile, 'r') as f:
        collect = []
        reader = csv.reader(f)
        for row in reader:
            collect.append(row)
    return collect

def intervalReturns(days, data):
    i = 1
    returns = []
    while i + days < len(data):
        try:
            ret = float(data[i+days][5])/float(data[i][5])
            returns.append(ret)
        except:
            pass
        i = i + 1
    return returns

def intervalInstances(interval, length):
    return (length - interval) - 1 #minus 1 for column headers

def positiveReturns(retlist):
    
    returns = 0
    for i in retlist:
        if i > 1: returns += 1
    return returns
    

csvfile = "VAS.csv"
data = csvToList(csvfile)
for i in range(1080):
    print(str(i) + " day interval: ")
    print(positiveReturns(intervalReturns(i, data))/intervalInstances(i, len(data)))
