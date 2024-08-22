# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

def Phase_finder(number):
    print(cmath.phase(number))
    print(abs(number))

    
#main Function
print("\nEnter two values x and y to find polar coordinates:")
complex_number=input("Enter the complex number in this form a+bj: ")
complex_num=complex(complex_number)
print(complex_num)
Phase_finder(complex_num)




