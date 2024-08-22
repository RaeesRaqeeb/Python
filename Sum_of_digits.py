#CODE BY; TAYRA Raqeeb
#sum of digits of the given integer

def sum_of_digits(num1):
    sum=0
    while(num1>=1):
        sum+=int(num1%10)
        num1/=10
    return sum


#main program
print("\nEnter any integer to find the sum of its digits:")
number=int(input())
print(int(sum_of_digits(number)))
