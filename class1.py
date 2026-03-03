# Topic : Python OBJ-ORI-PRO

# Class : structure/blueprint

class Car:
    wheel = 4
    engine = "450hp"
    color = "matte"
    seat = "leather"
    
mercedes = Car()

print(mercedes.engine)

#editing the class-obj
mercedes.engine = "600hp"
print(mercedes.engine)


BMW = Car()

print(BMW.color)
print(mercedes.seat)

#Make an Animal Class and some objects of it, for example horse, cat, dog etc. 