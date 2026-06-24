# === exercise 1 ===

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Hello, i'm {self.name}, {self.age} years old, lives in {self.city}", end="")

    def have_birthday(self):
        self.age += 1
        print(f"Happy birthday! Now i'm {self.age} years old.")

# tzvi = Person("Tzvi", 30, "Bney Brak")
# israel = Person("Israel", 25, "Netanya")
# chaim = Person("Chaim", 50, "Ramat Gan")
#
# tzvi.introduce()
# israel.introduce()
# chaim.introduce()
#
# tzvi.have_birthday()
# tzvi.introduce()

# === exercise 2 ===

class Mosad:
    def __init__(self, name, type, students_count, city):
        self.name = name
        self.type = type
        self.students_count = students_count
        self.city = city

    def print_details(self):
        print(f"Mosad name - {self.name}, type - {self.type}, number of students - {self.students_count}, city - {self.city}")

    def add_student(self, num=1):
        self.students_count += num

    def remove_student(self, num=1):
        if self.students_count <= 0:
            print("Student count can't be negative!")
            return
        self.students_count -= num
school = Mosad("Bla Bla", "Bablat", 5, "Petah Tikva")
university = Mosad("Super Bla", "VIP Bla", 200, "Ra'anana")

# school.print_details()
# university.print_details()
# school.add_student(50)
# university.remove_student(20)
# school.print_details()
# university.print_details()