class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def start(self):
        print(self.brand, "car started")

    def stop(self):
        print(self.brand, "car stopped")

    def show_speed(self):
        print("Speed:", self.speed, "km/h")


class ElectricCar(Car):
    def __init__(self, brand, speed, battery):
        super().__init__(brand, speed)
        self.battery = battery

    def fuel(self):
        print("Uses electricity")

    def show_battery(self):
        print("Battery:", self.battery, "%")


class SportsCar(Car):
    def __init__(self, brand, speed, turbo=False):
        super().__init__(brand, speed)
        self.turbo = turbo

    def fuel(self):
        print("Uses petrol")

    def turbo_mode(self):
        if self.turbo:
            print("Turbo mode ON")
        else:
            print("Turbo mode OFF")


e_car = ElectricCar("Tesla", 180, 85)
s_car = SportsCar("BMW", 260, True)

e_car.start()
e_car.show_speed()
e_car.fuel()
e_car.show_battery()
e_car.stop()

print()
 
s_car.start()
s_car.show_speed()
s_car.fuel()
s_car.turbo_mode()
s_car.stop()
