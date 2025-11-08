def Countdown(num1):
    if num1 == 0:
        return 0
    print(num1)
    return Countdown(num1-1)    
    