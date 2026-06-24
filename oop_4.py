# # # # # # # # # # # # # #
class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self._account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0:
            self.__balance -= amount

    @property
    def balance(self):
        return f"{self.__balance}"

    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self.deposit(amount)
        else:
            self.withdraw(amount)


Tzvi = BankAccount("515555", "Tzvi Fisher", 55555)

Tzvi.account_number = "312"
Tzvi.account_holder = "Chaim schneider"
Tzvi.balance = 10000000000

print(Tzvi.account_number)
print(Tzvi._account_holder)
print(Tzvi.balance)

# # # # # # # # # # # # # # # #

class Vehicle:
    def __init__(self, model, color):
        self.model = model
        self._color = color
        self.__speed = 0

    def accelerate(self, speed_increase):
        self.__speed += speed_increase

    def brake(self, speed_decrease):
        self.__speed -= speed_decrease

    def get_speed(self):
        print(self.__speed)

    def get_color(self):
        print(self._color)


class Car(Vehicle):
    def __init__(self, model, color, max_speed):
        super().__init__(model, color)
        self.max_speed = max_speed

    def accelerate(self, speed_increase):
        if self.__speed < self.max_speed:
            self.__speed += speed_increase
            if self.__speed > self.max_speed:
                self.__speed = self.max_speed

    def get_max_speed(self):
        print(self.max_speed)
    