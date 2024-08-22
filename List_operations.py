#Code by: Tayra Raqeeb 


def Sorting(mylist):
    index=0
    while(index!=len(mylist)):
        index2=0
        tem=0
        min=mylist[index]
        while(index2!=len(mylist)):
           
            if(min>mylist[index2]):
                min=mylist[index2]
                tem=index2
            index2+=1
        tem2=mylist[index]
        mylist[index]=min
        mylist[tem]=tem2
        index+=1
    return mylist









mylist1=[4,5,3,2,6,9,10,1,8,7]
print(Sorting(mylist1))