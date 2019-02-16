def incrementreturn(fortnight, brokerage, interest):
    daily = ((interest + 1) ** (1/365)) # - 1
    initialamount = 0
    
    for day in range(365):
        if day % 14 == 0:
            initialamount += (fortnight - brokerage)
            print(initialamount)
        initialamount *= daily
    return initialamount
