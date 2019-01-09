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
    return positiveInflationReturns(retlist, 1)

def positiveInflationReturns(retlist, inflation):
    returns = 0
    for i in retlist:
        if i > inflation: returns += 1
    return returns

def sortReturns(retlist):
    retlist.sort()
    return retlist

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

csvfile = "VAS.csv"
data = csvToList(csvfile)
data = sortReturns(intervalReturns(28, data))
quart = split_list(data,12)
for s in quart:
    print(str(s[0]) + "and" + str(s[-1]))
