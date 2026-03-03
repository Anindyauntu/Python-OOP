# Polymorphism — same method name, different behavior
# HW -- ANINYA(AUNTU) 18.1.2026
# CLASS 9_HW
class Vehicle:
    def __init__(self):
        print("Vehicle created.")

    def move(self):
        print("Vehicle is moving.")


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        print("Car created.")

    def move(self):
        print("Car is driving on the road.")


class Boat(Vehicle):
    def __init__(self):
        super().__init__()
        print("Boat created.")

    def move(self):
        print("Boat is sailing on water.")


class Plane(Vehicle):
    def __init__(self):
        super().__init__()
        print("Plane created.")

    def move(self):
        print("Plane is flying in the sky.")


v1 = Car()
v2 = Boat()
v3 = Plane()

vehicles = [Car(), Boat(), Plane()]

# Polymorphism in action
for v in vehicles:
    v.move()
