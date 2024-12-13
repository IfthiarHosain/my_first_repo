class Bank:
    def __init__(self):
        self.coustomer={}
    def create_account(self,account_number,initial_balance=0):
        if account_number in self.coustomer:
            print("account number already exists")
        else:
            self.coustomer[account_number]=initial_balance
            print("account created successfully")
    def make_deposit(self,account_number,amount):
        if account_number in self.coustomer:
            self.coustomer[account_number] += amount
            print("deposit successfull")
        else:
            print("account dosen't exists")
    def make_withdrawal(self,account_number,amount):
        if account_number in self.coustomer:
            if self.coustomer[account_number]>= amount:
                 self.coustomer[account_number] -= amount
                 print("withdrawal successfull")
            else:
                print("insufficient fund")
        else:
            print("account doesn't exists")
    def check_balance(self,account_number):
        if account_number in self.coustomer:
            balance= self.coustomer[account_number]
            print(f"balance,{balance}")
        else:
            print("account doesn't exists ")
bank=Bank()
account1="Sb-13"
depamount1=1500
print("New account No:",account1,"Deposit Amount", depamount1)
bank.create_account(account1,depamount1)

account2="Sb-15"
depamount2=2500
print("New account No:", account2,"deposit amount", depamount2)
bank.create_account(account2,depamount2)

damnt1=800
print("deposit amount of:",damnt1,"to account No", account1)
bank.make_deposit(account1,damnt1)

wamnt2=400
print("withdrawal amount of:",wamnt2,"to the account No:", account2)
bank.make_withdrawal(account2,wamnt2)

print("check balance of:", account1)
bank.check_balance(account1)

print("check balance:", account2)
bank.check_balance(account2)

wamt3=3000
print("withdrawal amount of:", wamt3)
bank.make_withdrawal(account2,wamt3)

account3="Sb-50"
print("account number:", account3)
bank.check_balance(account3)

