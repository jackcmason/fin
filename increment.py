def incrementtotalreturn(moneyin, payinterval, brokerage, interest, timeinterval):
    return incrementpartsreturn(moneyin//(365//payinterval), payinterval, brokerage, interest, timeinterval)

def incrementpartsreturn(pay, payinterval, brokerage, interest, timeinterval):
    daily = ((interest + 1) ** (1/365)) # - 1
    initialamount = 0
    count = 0
    
    for day in range(timeinterval):
        if day % payinterval == 0 and day != 0:
            initialamount += (pay - brokerage)
            count += 1
        initialamount *= daily
    return initialamount
