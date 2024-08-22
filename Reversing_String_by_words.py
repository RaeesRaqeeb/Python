#Function which reverse the given string word by word

def Function(Name):
    new_name=""
    new_name2=""
    length=len(Name)-1
    new_length=0
    for i in range(length+1):
        new_name+=Name[length]
        if(Name[length-1]==' ' or length-1<0):
            for i in range(new_length+1):
                new_name2=new_name2+new_name[new_length]
                new_length-=1
                if(new_length-1<0):
                    new_length=0
            new_name2+=" "
            new_name=""
        else:
            new_length+=1
        length-=1
    print(new_name2)
 

#main function
print("Enter any thing which will be given in reverse form word by word: ")
sentence=input()
Function(sentence)