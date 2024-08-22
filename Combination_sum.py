


def Combination_Sum(mylist2,target):
    def recursion(start,target,path):
        if(target==0):
            result.append(path)
            return
        for i in range(start,len(mylist2)):
            if(i >start and mylist2[i]==mylist2[i-1]):
                continue
            if(mylist2[i]>target):
                break
            recursion(i,target-mylist2[i],path+[mylist2[i]])



            
        
    
    mylist2.sort()
    result=[]
    recursion(0,target,[])
    return result
    


    pass

if __name__ =='__main__':
    print("\nEnter size of array:")
    size=int(input())
    mylist2=[]
    print("\nEnter the element in the list to find the possible combinations to get to the target:")
    for x in range (size):
        mylist2.append(int(input("\nEnter the value1:")))
    
    print("\nEnter the target value:")
    target=int(input())

    outcome=Combination_Sum(mylist2,target)
    print(outcome)