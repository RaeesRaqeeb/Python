from operator import truediv
from pickle import FALSE, TRUE


def checker(values):
    first_letter=''
    for x,values2 in enumerate(values):
        if(values2==' '):
            if(values[0]==values[x+1]):
            
                return True
            else:
                return False
            

#Main function
print("Calling the function")
value=checker('two to')
print(value)