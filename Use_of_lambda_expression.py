from math import sqrt


mylist=[2,3,4,5,6,7,8,9,23]
print(list(filter(lambda x:x%2!=0,mylist)))
print(list(map(lambda x:sqrt(x),mylist)))
str_list=['Raees','Khan','Raqeeb','civic ']
print(list(map(lambda x:x[::-1],str_list)))
print(list(filter(lambda x:len(x)>=6,str_list)))
print(list(filter(lambda x:x[::-1]==x,str_list)))