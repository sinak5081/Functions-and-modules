def maxfind(*par):
    mymax = par[0]
    for item in par[1:]:
        if item > mymax:
            mymax = item
    return mymax
max1 = maxfind(1,2,12,32,4,64)
print("first max is: ",max1)
max2 = maxfind(4,3,12)
print("second max is: ",max2)