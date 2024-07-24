#Checking the List is in Ascending order or not

l1=[1,2,3,19,5,6]

checker=0
value=0
for i in range(0,len(l1)-1):
    if(l1[i]<l1[i+1]):
        checker+=1
        
if(checker==len(l1)-1):
    print('the list is in assending')
else:
    print('list is not in ascending order')
