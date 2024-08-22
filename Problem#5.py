#Finding prime number up to given number
def Prime_finder(number):
    num_count=0
    prime_number=[]
    for x in range(2,number+1):
        num_count=0
        if(x!=0 or x!=1):
            for n in range(1,x):
                if(x%n==0):
                    num_count+=1
            if(num_count==2):
                prime_number.append(x)
        
    return prime_number

#main function 
print(Prime_finder(10))