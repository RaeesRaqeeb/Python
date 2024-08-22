class account():
    
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def __str__(self,owner,balance2):
        print("Account Owner:",owner,"\nAccount Balance:",balance2)
    def deposit(self, balance3):
        self.balance+=balance3
        print("\nDeposit is successfully completed")
    def withdraw(self, balance4):
        if(balance4>self.balance):
            print("Insefficient balance\n")
        elif(balance4<=self.balance):
            self.balance-=balance4
            print("Balance is withdraw successfully")

#main program 
print("Enter the amount you want to deposit")   
user1=account("Raqeeb",1000)
amount=int(input("\nAMount:"))     
user1.deposit(amount)

print("Enter the amount you want to withdraw:")
amount=int(input())
user1.withdraw(amount)




