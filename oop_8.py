class BankAccount:
    def __init__(self, account_number, initial_balance = 0):
        self.__account_number = account_number
        self.__balance = initial_balance
        self.__transaction_count = 0

    @property
    def balance(self):
            return f"The balance is {self.__balance}"

    @property
    def account_number(self):
            return f"Account number is {self.__account_number}"

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction_count += 1
        else:
            print("Amount for deposit must be positive!")

    def withdraw(self, amount):
        if amount < 0:
            self.__balance += amount
            self.__transaction_count += 1
        else:
            print("Amount for deposit must be negative!")

    def get_transaction_number(self):
        return f"Transaction number is {self.__transaction_count}"

# tzvi = BankAccount("51555", 20000)
# tzvi.withdraw(-50)
# print(tzvi.balance)

# # # # # # # # # # # # # # # # # # #

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            if name.strip():
                self.__name = name
            else:
                print("Error: Name can't be empty!")
        else:
            print("Error: Name has to be a string!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            print("Error: Age has to be an integer!")

        if 0 < age < 150:
            self.__name = age
        else:
            print("Error: Age is not in legal range!")

    @property
    def category(self):
        if self.__age < 13:
            return "Child"
        if self.__age <= 19:
            return "Teenager"
        if self.__age <= 64:
            return "Adult"
        return "Senior"


haim = Person("haim", 8)
haim.age(18)
print(haim.age)
print(haim.category)