class Tradeday:
    def __init__(self, code, date, openprice, high, low, close, volume, value, trades):
        self.code = code
        self.date = date
        self.open = openprice
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.value = value
        self.trades = trades
    def __str__():
        return "Code:{}\nDate:{}\nOpen:{}\nHigh:{}\nLow:{}\nClose:{}\nVolume:{}\nValue:{}\nTrades:{}".format(
            self.code, self.date, self.open, self.high, self.low, self.close, self.volume, self.value, self.trades)
