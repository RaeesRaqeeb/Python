def eratosthenes(limit):
    is_prime=[True]*(limit+1)
    is_prime[0],is_prime[1]=False,False

    for x in range(2,int(limit**0.5)+1): #Using square of the limit 
        if(is_prime):

            for j in range(x*x,(limit+1),x) :
                is_prime[j]=False
        
    prime=(x for x in range(2,(limit+1)) if(is_prime[x]))
    return prime



if __name__ == '__main__':
    print("\nEnter any number to find the prime number till it using sieve of Erdtosthenses algorithm:")
    num=int(input())
    result=list(eratosthenes(num))
    print(result)
