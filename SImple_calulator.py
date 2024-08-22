print("Enter two numbers to perform different operation on them\n")

print("Num1:")
num=int(input())
print("Num2:")
num2=int(input())

print("\nWhich operation you want to perform\n")
print(" + - / % * \n")

instru=input()

if(instru== "+"):
    print(num+num2)
elif(instru=="-"):
    print(num-num2)
elif(instru=="/"):
    print(num-num2)
elif(instru=="%"):
    print(num%num2)
elif(instru=="*"):
    print(num*num2)
