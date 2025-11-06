def func1():
    print(msg)

def func2():
    msg = "I am in function2"
    print(msg)
msg = "I like pythone programming"
func1()
func2()
print("after calling func2: ")
print(msg)