def larg_value(num1,num2,num3):
    max = num1 if num1>num2 else num2
    max = num2 if num2>num3 else num3
    print("The largest value is: ",max)
    return max
x = int(input("Enter a first number: "))
y = int(input("Enter a second number: "))
z = int(input("Enter a third number:"))
larg_value(x,y,z)