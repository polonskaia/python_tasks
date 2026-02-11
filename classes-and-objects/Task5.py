class BankAccount:
    def __init__(self, account_number: str, account_holder: str, balance: float):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
            self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print('Insufficient funds')

    def check_balance(self):
        return self.__balance
    
    @property
    def account_holder(self):
        return self.__account_holder
    
account = BankAccount('123456789', 'John Doe', 1000.0)
print(account.account_holder)
print(account.check_balance())

account.deposit(500.0)
print(account.check_balance())

account.withdraw(250.0)
print(account.check_balance())

account.withdraw(5000.0)