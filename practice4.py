# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
def Shoes_management(num_shoes,size_Dictionary,Num_customers,customer_input_size,price):
    for key,value in size_Dictionary.items():
        if(customer_input_size == key): 
            size_Dictionary[key]-=1
            if(size_Dictionary[key]==0):
                size_Dictionary.pop(key)
            return int(price)
    
    return 0
            #when the size is not available or out of stock
pass
            

#Main function
#if __ name __ ==' __ main __':

num_shoes=input()
num_shoes=int(num_shoes)
size_list=list(map(int,input().split()))
size_dictio=Counter(size_list)
num_customer=input()

x=0
total1=0
total=[]
while(x!=int(num_customer)):
    input_values=input()
    customer_size,price=input_values.split()
    customer_size=int(customer_size)
    price=int(price)
    total1=Shoes_management(num_shoes,size_dictio,num_customer,customer_size,price)
    if(total1==0):
        pass
    total.append(total1)
    x+=1
sum=0
for x in total:
    sum+=x
print(sum)

