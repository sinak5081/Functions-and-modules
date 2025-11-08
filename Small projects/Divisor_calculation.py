def gcd(num1,num2):
    max = 1
    n = min(num1,num2)
    for i in range(1,n+1):
        if(num1%i == 0 and num2%i == 0):
            max = i
    return max
