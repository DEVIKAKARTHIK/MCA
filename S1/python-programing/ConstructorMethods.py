class Account:
    def __init__(self,accountno,name,type,bal):
        self.accountno=accountno
        self.name=name
        self.type=type
        self.bal=bal
    def deposit(self,amount):
        self.bal+=amount
        print(f"{amount} is successfully withdrawed")
    def withdraw(self,amount):
        if amount>self.bal:
            print(f"insufficient bank balance")
        self.bal-=amount
        print(f"{amount} is successfully deposited")
    def display(self):
        print(f"accountno={self.accountno}\t Name={self.name}\t accounttype={self.type}\t balance={self.bal}")
accountno=int(input("Enter the account number="))
type=input("Enter the account type=")
name=input("Enter the account holder name=")
member=Account(accountno,type,name,0)
while True:
   print("1.deposit,2.withdraw,3.display,4.exit")
   transaction=int(input("Enter the choice"))
   if transaction==1:
       amount=int(input("Enter the amount"))
       member.deposit(amount)
   elif transaction==2:
       amount=int(input("Enter the amount"))
       member.withdraw(amount)
   elif transaction==3:
       member.display()
   else:
       exit()
