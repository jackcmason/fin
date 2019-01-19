from csvtodata import *
from tradeday import Tradeday

class Security:
    def __init__(self, csvfile):
        self.days = []
        self.filteredDays = []
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
            self.filteredDays.append(day)

    def printDays(self):
        for day in self.days:
            print(day)

    def printFilteredDays(self):
        for day in self.filteredDays:
            print(day)

    def positiveReturns(self):
        self.filteredDays = list(filter(lambda x: x.close > x.open, self.days))

    def numberDays(self):
        return len(self.days)

    def numberFilteredDays(self):
        return len(self.filteredDays)
