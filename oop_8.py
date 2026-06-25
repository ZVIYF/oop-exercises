from curses.ascii import isdigit


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
        if not isinstance(name, str):
            print("Error: Name has to be a string!")
            return
        if not name.strip():
            print("Error: Name can't be empty!")
            return
        self.__name = name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if not isinstance(new_age, int):
            print("Error: Age has to be an integer!")
        if 0 < new_age < 150:
            self.__age = new_age
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


# haim = Person("haim", 8)
# haim.age += 12
# print(haim.age)
# print(haim.category)

# # # # # # # # # # # # # # #

class User:
    __user_count = 0
    __users_list = []

    def __init__(self, username, e_mail, password):
        self.username = username
        self.email = e_mail
        self.__password_hash = password.__hash_password()
        User.__user_count += 1
        User.__users_list.append(self)

    @staticmethod
    def __hash_password(former_password):
        return str(hash(former_password))

    @staticmethod
    def is_valid_email(email):
        if isinstance(email, str):
            if "@" in email:
                return True
        return False

    @staticmethod
    def is_strong_password(my_pass):
        if len(my_pass) < 8:
            return False
        has_upper, has_lower, has_digits = False
        for char in my_pass: # הקוד לא לוקח בחשבון תווים מיוחדים?
            if isdigit(char):
                has_digits = True
            elif char == char.upper:
                has_upper = True
            elif char == char.lower:
                has_lower = True
        return has_lower and has_upper and has_digits

    @staticmethod
    def creat_user_safely(username, email, password):
        if not User.is_valid_email(email):
            print("Error: Invalid E-mail!"
                  "Please try again...")
            return None
        if not User.is_strong_password(password):
            print("Error: Invalid password.\n"
                  "Password must have:\n"
                  " - at least 8 characters.\n"
                  " - at least 1 upper case.\n"
                  " - at least 1 lower case.\n"
                  " - at least 1 digit.\n"
                  "Please try again.")
            return None
        return User(username, email, password)