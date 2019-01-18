from csvtodata import *
from tradeday import Tradeday

class Security:
    def __init__(self, csvfile):
        self.days = []
        for row in csvToList(csvfile):
            day = Tradeday(getCode(row),
                           getDate(row),
                           getOpen(row),
                           getHigh(row),
                           getLow(row),
                           getClose(row),
                           getVolume(row),
                           getValue(row),
                           getTrades(row))

            self.days.append(day)
