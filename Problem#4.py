#User Defined Function

def Spyfunction(mylist):
    zero_count=0
    seven_counts=0
    for x in mylist:
        if(x==7 and zero_count!=2):
            return False
        elif(x==7 and zero_count==2):
            return True
        elif(x==0):
            zero_count+=1
    return False

#main function 
print(Spyfunction([1,2,3,7,4,5,0,6]))