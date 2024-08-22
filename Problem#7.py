#Temperature converter
import string

def reverser(value):
    new_value=''
    length=len(value)
    for x in range(length):
        new_value+=value[length-1]
        length-=1
    return new_value
#main function
str_list=['Khan','Raees','Tahir']
print(list(map(reverser,str_list)))