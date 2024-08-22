#Code By: Tayra RAQEEB 
#Palindrome Checker
import string

def Palindrome_checker(Value):
    num=len(Value)
    num-=1
    count=0
    for x in Value:
        if(x==Value[num]):
            if( count<int(len(Value)/2)):
                count+=1
            else:
                break
        num-=1

    if(count==(int(len(Value)/2))):
        print(Value," is Palindrome")

    
#Main program
        
print("\nEnter any string or interger to find wheather it is palindrome or not\n")
value=(input())
Palindrome_checker(value)