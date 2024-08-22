#Function 
def Summer(mylist):
    sum=0
    for x in mylist:
        if((x<6) or (x>9)):
            sum+=x
        elif(x==6):
            pass
    return sum


#main function
print(Summer([1,2,3,4,6,8,9,1]))