class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    def account_no_validation(self):
        print(len(self.account_no))
        if len(self.account_no)==14:
            print("Valid account number")
        else:
            print("Invalid account number")
    def deposit(self):
        self.balance=self.balance+int(input("Enter the amount to deposit:"))
        print("Balance after deposit:",self.balance)
    def withdraw(self):
        amount=int(input("Enter the amount to withdraw:"))
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance=self.balance-amount
            print("Balance after withdraw:",self.balance)
a=Account(10000,"12345678901245")
a.account_no_validation()
a.deposit()
a.withdraw()