def swap(a,b):
    a,b = b,a
    return a,b
x = int(input("Enter a number: "))
y = int(input("Enter a number:  "))
x,y=swap(x,y)
print("x = ",x,"y = ",y)