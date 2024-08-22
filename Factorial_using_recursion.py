# finding factorial
num2 = 0

def recursion(value1, value2):
    global num2
    value1 -= 1
    if value1 > 0:
        num2 = value2 * value1
       
        recursion(value1, num2)
    return num2

num1 = 10
print(recursion(num1, num1))
