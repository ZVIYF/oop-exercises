# === exercise 1 ===

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Hello, i'm {self.name}, {self.age} years old, lives in {self.city}")

    def