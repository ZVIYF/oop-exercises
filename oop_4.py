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


# Tzvi = BankAccount("515555", "Tzvi Fisher", 55555)
#
# Tzvi.account_number = "312"
# Tzvi.account_holder = "Chaim schneider"
# Tzvi.balance = 10000000000
#
# print(Tzvi.account_number)
# print(Tzvi._account_holder)
# print(Tzvi.balance)

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

# ford = Car("mustang", "Red", 220)
# ford.speed = 50
# print(ford.speed)

# # # # # # # # # # # # # # # # # # # # # #

class DigitalSafe:
    def __init__(self, safe_id, code, is_locked, attempt_count):
        self._sefe_id = safe_id
        self.__code = code
        self.__is_locked = True
        self.__attempt_count = 3

    def try_unlock(self, code):
        if not self.__is_locked:
            print("Alredy open")
            return
        if self.__attempt_count > 0:
            if code == self.__code:
                self.__is_locked = False
                self.reset_counts()
            else:
                self.__attempt_count -= 1

    def is_locked(self):
        print(f"Is safe locked: {self.__is_locked}")

    def get_attempts_left(self):
        return f"attempts left: {self.__attempt_count}"

    def reset_counts(self):
        if not self.__is_locked:
            self.__attempt_count = 3

# # # # # # # # # # # # # # # # # #

class GameScore:
    def __init__(self, player_name):
        self.player_name = player_name
        self._level = 1
        self.__score = 0
        self._high_score = 0

    def add_points(self, points):
        self.__score += points
        if self._high_score < self.__score:
            self._high_score = self.__score

    def level_up(self):
        self._level += 1

    def get_score(self):
        return f"score is {self.__score}"

    def get_high_score(self):
        return f"High score is {self._high_score}"

    def reset_score(self):
        self.__score = 0