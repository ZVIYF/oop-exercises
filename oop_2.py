from oop_1 import Person

## פונקציה שממירה מספר לסטרינג של המספר מתוך רצף. 1 = ראשון.

def to_ordinal_en(num):
    if 11 <= num % 100 <= 13:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(num % 10, 'th')
    return f"{num}{suffix}"

# # # # # # # # # # # # # # #

class Student(Person):
    def __init__(self, name, age, city, student_ID, grade):
        super().__init__(name, age, city)
        self.student_ID = student_ID
        self.grade = grade

    def study(self):
        print(f"{self.name} is in {to_ordinal_en(self.grade)} grade")

    def introduce(self):
        super().introduce()
        print(f", and I'm in {to_ordinal_en(self.grade)}")

    def advance_grade(self):
        self.grade += 1

# ============

class Teacher(Person):
    def __init__(self, name, age, city, subject, experience):
        super().__init__(name, age, city)
        self.subject = subject
        self.experience = experience

    def teaches(self):
        print(f"{self.name} teaches {self.subject} for {self.experience} years")

    def introduce(self):
        super().introduce()
        print(f", teaches {self.subject} for {self.experience} years")

    def gain_experience(self):
        self.experience += 1

# # # # # # # # # # # # # # #

class Principal(Person):
    def __init__(self, name, age, city, years_as_principal):
        super().__init__(name, age, city)
        self.years_as_principal = years_as_principal

    def manage(self):
        print(f"{self.name} manages the mosad for {self.years_as_principal} years")

    def introduce(self):
        super().introduce()
        print(f", the principal of this Mosad for {self.years_as_principal} years")

    def add_management_experience(self):
        self.years_as_principal += 1

# # # # # # # # # # # # # # # # #

israel_meir = Student("Israel Meir", 25, "Karmiel", "55216423", 5)
chaim = Teacher("chaim", 50, "Givat Shmuel", "Philosophy", 4)
yisachar = Principal("yisachar", 65, "Bney Brak", 12)

# israel_meir.introduce()
# chaim.introduce()
# yisachar.introduce()
#
# israel_meir.advance_grade()
# chaim.gain_experience()
# yisachar.add_management_experience()
#
# israel_meir.introduce()
# chaim.introduce()
# yisachar.introduce()
