def func(x):
    print("x in func before change: ",x)
    x = 10
    print("x in func after change: ",x)
x = 5
func(x)
print("x caller after call the function: ",x)