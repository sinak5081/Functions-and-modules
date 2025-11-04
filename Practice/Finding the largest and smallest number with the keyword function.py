def compare(*numbers , case):
    if case:
        result = findmax(numbers)
    else:
        result = findmin(numbers)
    return result

def findmax(numbers):
    max = numbers[0]
    for item in numbers:
        if item > max:
            max = item
    return max
def findmin(number):
    min = number[0]
    for item in number:
        if item < min:
            min = item
    return min
print("max is : ")
print(compare(12,23,5, case = False))
print("min is : ")
print(compare(12,23,5, case = False))