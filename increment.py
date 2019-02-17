def incrementtotalreturn(moneyin, payinterval, brokerage, interest):
    return incrementpartsreturn(moneyin//(365//payinterval), payinterval, brokerage, interest)

def incrementpartsreturn(pay, interval, brokerage, interest):
    daily = ((interest + 1) ** (1/365)) # - 1
    initialamount = 0
    count = 0
    
    for day in range(365):
        if day % interval == 0 and day != 0:
            initialamount += (pay - brokerage)
            count += 1
        initialamount *= daily
    return initialamount

print(incrementtotalreturn(13000, 14, 10, 0.07))
