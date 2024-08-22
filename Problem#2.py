#user define function
def Function(values):
    length=len(values)
    new_value=""
    for i,char in enumerate(values):
        for n in range(3):
            new_value+=char
    return new_value

#Main function

print(Function("Raqeeb"))