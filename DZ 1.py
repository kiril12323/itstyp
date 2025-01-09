class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"На рахунок {self.account_number} зараховано {amount}. Поточний баланс: {self.balance}.")
        else:
            print("Сума для зарахування повинна бути більше 0.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"З рахунку {self.account_number} знято {amount}. Поточний баланс: {self.balance}.")
            else:
                print(f"Недостатньо коштів на рахунку {self.account_number}. Поточний баланс: {self.balance}.")
        else:
            print("Сума для зняття повинна бути більше 0.")

# Приклад використання
account = BankAccount("12345678", 1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)
