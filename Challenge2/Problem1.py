class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"dear coustomer {self.__account_holder_name}. \nYour A/c {self.__account_number}can be created with Rs: {amount}\ntotal balance {self.__account_balance}")
        else:
            print("Invalid deposit amount. Please deposit a positive amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            print(f"dear {self.__account_holder_name}. \nYour A/c {self.__account_number}. Depited by {amount} \nTotal balance {self.__account_balance}")
        else:
               print("Invalid withdrawal amount or insufficient balance.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name} Rs : {self.__account_balance}")


account1 = BankAccount("*your regno"*, *"your name"*, 1000)


account1.display_balance()
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(1500)
