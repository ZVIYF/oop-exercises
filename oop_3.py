# # # # # # # # # # # # # #

class Vehicle:
    pass

class Engine:
    pass

class Doors:
    pass

class Wings:
    pass

class Motorcicle(Vehicle):
    def __init__(self):
        super().__init__()
        self.engine = Engine

class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.engine = Engine
        self.doors = Doors

class Bicycle(Vehicle):
    def __init__(self):
        super().__init__()

class Airplane:
    def __init__(self):
        self.engine = Engine
        self.doors = Doors
        self.wings = Wings

class Electric_scooter(Vehicle):
    def __init__(self):
        super().__init__()
        self.engine = Engine

# # # # # # # # # # # # # # # #

