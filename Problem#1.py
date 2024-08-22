#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def solving(mylist):
    num=len(mylist)
    for i in range(num):
        if(mylist[i]==3):
            if(mylist[i+1]==3):
                return True
            else:
                return False
    return False


#main function 
print("It will work:")
print(solving([1,2,3,4]))

