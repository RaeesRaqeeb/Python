#Removing Duplicates from the list
checker=0
l1=[1,2,3,1,1,2,2,3,4,5,5]
l3=l1.copy()
l2=[]
checker=0
#[i for i in range(0,len(l1)) for j in range(0,len(l1)) if l1[i]==l1[j] l1.remove(l1(j))]
for i in l1:
    for j in l3:
        if(i==j):
            checker+=1
            if(checker>1):
                l1.remove(j)
    
    checker=0
            

print(l1)
