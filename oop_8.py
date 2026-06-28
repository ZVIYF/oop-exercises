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
        self.__password_hash = User.__hash_password(password)
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
        has_upper, has_lower, has_digits = False, False, False
        for char in my_pass: # הקוד לא לוקח בחשבון תווים מיוחדים?
            if char.isdigit():
                has_digits = True
            elif char.isupper():
                has_upper = True
            elif char.islower():
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

    @classmethod
    def get_user_count(cls):
        return cls.__user_count

    @classmethod
    def find_user_by_username(cls, my_username):
        for user in cls.__users_list:
            if user.username == my_username:
                return user
        return None

# User.creat_user_safely("tzvi", "zviyf132@gmail.com", "aa123456A")
# my_user = User.find_user_by_username("tzvi")
# print(my_user.email)
# print(User.get_user_count())

# # # # # # # # # # # # # # # # # # # # # # #

class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, new_height):
        if not new_height >= 0:
            print("Error: Value for height must be positive.")
            return
        self.__height = new_height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, new_width):
        if not new_width >= 0:
            print("Error: Value for width must be positive.")
            return
        self.__width = new_width

    @property
    def area(self):
        return self.__height * self.__width

    @property
    def parameter(self):
        return (self.__width + self.__height) * 2

    @property
    def is_square(self):
        return self.__height == self.__width

    @staticmethod
    def create_square(side):
        return Rectangle(side, side)

    @staticmethod
    def compare_areas(rect1, rect2):
        if rect1.area > rect2.area:
            return f"Rectangle 1 is bigger."
        elif rect1.area < rect2.area:
            return f"Rectangle 2 is bigger."
        else:
            return f"Both are equal."

# my_rect = Rectangle(5, 3)
# not_my_rect = Rectangle(8, 2)
# my_square = Rectangle.create_square(4)
# print(Rectangle.compare_areas(my_square, not_my_rect))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Product:
    TAX_RATES = {
        "food" : 0.0,
        "books" : 0.0,
        "electronics" : 0.17,
        "clothing" : 0.17,
        "other" : 0.17
    }

    def __init__(self, name, base_price, category="other", discount_percent=0.0):
        self.__name = name
        self.__category = category
        self.__base_price = base_price
        self.__discount_percent = discount_percent

    @property
    def name(self):
        return self.__name

    @property
    def base_price(self):
        return self.__base_price

    @base_price.setter
    def base_price(self, new_price):
        if new_price < 0:
            print("Error: Price can't be negative!")
        else:
            self.__base_price = new_price

    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, new_category):
        if new_category in Product.TAX_RATES:
            self.__category = new_category
        else:
            print("Error: Category isn't available.")

    @property
    def discount_percent(self):
        return self.__discount_percent

    @discount_percent.setter
    def discount_percent(self, new_value):
        if 1 > new_value > 0:
            self.__discount_percent = new_value
        else:
            print("Error: Discount percent must be between 0 - 1")

    @property
    def price_after_discount(self):
        return self.__base_price * self.__discount_percent

    @property
    def tax_amount(self):
        return self.price_after_discount * Product.TAX_RATES[self.__category]

    @property
    def final_price(self):
        return self.price_after_discount + self.tax_amount

    @staticmethod
    def get_tax_rate(category):
        if category in Product.TAX_RATES:
            return Product.TAX_RATES[category]
        return Product.TAX_RATES["other"]

    @staticmethod
    def calculate_bulk_discount(quantity, unit_price):
        if quantity >= 100:
            return 0.15 * (quantity * unit_price)
        if quantity >= 50:
            return 0.1 * (quantity * unit_price)
        if quantity >= 10:
            return 0.05 * (quantity * unit_price)
        return 0

