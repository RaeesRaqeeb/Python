# #Exception Handling

# class exception_handling():

#     def __init__(self):
            
#         try:
#             for i in ['a','b','c']:
#                 print(i**2)
#         except:
#             print("Something wrong with the code")   
#         else:
#             print("when i will be print")
#         finally:
#             print("I always print out whatever happened")



# #main program
# obj= exception_handling()


# # 

def ask():

    while True:
        try:
            num=int(input("Enter value 1:"))
            print(num**2)
            break
        except TypeError:
            print("You didn't entered the number:")
            continue
        else:
            print("Else is output:")
        finally:
            print("I always executed")


ask()