# === exercise 1 ===

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Hello, i'm {self.name}, {self.age} years old, lives in {self.city}")

    def have_birthday(self):
        self.age += 1
        print(f"Happy birthday! Now i'm {self.age} years old.")

tzvi = Person("Tzvi", 30, "Bney Brak")
israel = Person("Israel", 25, "Netanya")
chaim = Person("Chaim", 50, "Ramat Gan")

tzvi.introduce()
israel.introduce()
chaim.introduce()

tzvi.have_birthday()
tzvi.introduce()