def fact(x):
    if x != 0:
        return x * fact(x-1)
    else:
        return 1
m = int(input("Enter a number: "))
print("number is:",m,"factorail is:",fact(m))