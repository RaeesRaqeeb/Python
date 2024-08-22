#concatenating the two lists
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]

list3=list1+list2
print(list3)

#extend list 1 with elements of list 2
list1.extend(list2)
print(list1)

#insertion
list1.insert(3,100)
print(list1)

#Remove the element
list1.remove(4)
print(list1)

#Finding the index of element in the list
i=0
for x in list1:
    if(x==8):
        print("Index of the 8 in the list is",i)
    i+=1

#poping the element in the list

poped=list2.pop(2)
print("THe element which is poped from the list2 is",poped)

#reversing the list
list2.reverse()
print("It is the reversed list:",list2)

#Sorting in descending order
list2.sort()
print("List sorted in asending order;",list2)
list2.sort(reverse=True)
print("Sorted in descending order:",list2)

#Filtering and counting
numbers=[1,2,3,4,5,2,3,6,7,2,8,9,10]
new_list=[x for x in numbers if(x%2==0)]
print(new_list)

print("Number of times 2 occured in the list",numbers.count(2))

#Removing element from the list which occured multiple times
for x in numbers:
    if(x==3):
        numbers.remove(x)

print("3 is removed from the list",numbers)

#Nested Lists
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[1][1])
row1=len(matrix)
col1=len(matrix[0])
for row in range(row1):
    
    for column in range(col1):
            if(matrix[row][column]==8):
                 matrix[row][column]=10
            

print(matrix)

#Printing the third column of the nested list
for row2 in range(row1):
     for column2 in range(col1):
          if(column2==2):
               print(matrix[row2][column2])

#creating new list which contain element which are square of the existing elements
newlist=[]
for x in list1:
     newlist.append(x*x)

print(newlist)

#Creating the list containing the odd number only in new list
newlist2=[x for x in list1 if(x%2!=0)]
print(newlist2)

#Using copy method
copy_list=list1.copy()
print(copy_list)
copy_list.append(6)
print(list1)
print(copy_list)


#Cleaing the list
mylist=[1,2,3,4]
mylist.clear()
print(mylist)

#searching the element
mylist2=[1,2,3,4,5,6,6,6,7,8,2,2,1]
print(mylist2.count(6))








