#Practice of tuples

from more_itertools import first


myTup=(7,"Red","Afgani Pelawo")
print(myTup)

#Tuple unpacking
myTup2=(123,2,3,4,"Raqeeb","Raees")
*list00,first_name,last_name=myTup2
print("My First name:",first_name,"\nMy Last name:",last_name,"\nlist created:",list00)

#Concatenation of the tuple

mytup1=("Going to die")
mytup2=(" No know")
mytup3=mytup1+mytup2
print(mytup3)

#Nesting Tuple

mytuples=(1,(2,"FIght"),[1,3,4,5])
print("First: ",mytuples[0])
print("second: ",mytuples[1][1])
print("Third: ",mytuples[2][3])

#Tuples are immutables

#Tuples Count and idex

mytuple2=(1,2,3,41,1,1,5,6,2,2)
print(mytuple2.count(1))
