class Rocket :
    def __init__(self,name,height,mass,engines,thrust,max_speed,company,fuel):
        self.name = name
        self.height = height
        self.mass = mass
        self.engines = engines
        self.thrust = thrust
        self.max_speed = max_speed
        self.company = company
        self.fuel = fuel
        
        print(f"{self.company} {self.name} is prepared to be launched ...")
        
    def launch_rocket(self):
        print(f"{self.name} has been launched ...")
        print(f"{self.name} has reached {self.max_speed} km/h")
        self.fuel = self.fuel - 31000
        print(f"{self.name}'s fuel level:{self.fuel}")
        print(f"First stage has been detached ...")
        
        in_put = input("Launch Stage-II ? :")
        
        if in_put == "yes" or in_put == "YES" or in_put == "Yes" :
            print("Launching Stage-II ...")
            self.fuel = self.fuel - 100000
            print("                                     ")
            print(f"{self.name}'s current fuel level : {self.fuel}")
            print("                                     ")
            print("REACHED MOON...")
            
        else:
            for i in range(3):
                print("Launch Stage - II ASAP!!!")
                
            inp_ut = input("Launch Stage - II ? :")
            if inp_ut == "yes" or inp_ut == "YES" or inp_ut == "Yes" :
                print("Launching Stage-II ...")
                self.fuel = self.fuel - 100000
                print(f"{self.name}'s current fuel level : {self.fuel}")
                    
            else :
                self.fuel = self.fuel - self.fuel
                print(f"{self.name}'s fuel level: {self.fuel}... ROCKET FAILED !!!")
                print(f"RIP {self.company}'s astronauts ...")
                
    def mission_cancel(self):
        self.fuel = 0
        self.thrust = 0
        print(f"{self.company}'s mission cancelled. & fuel : {self.fuel} & thrust : {self.thrust}")
                    
    def mission_delay(self):
        print(f"{self.company}'s mission delayed.")
        
    
        
t = Rocket("Saturn V","42 metres","2970 Tons","5 × J-2 engines",34000000,39000,"NASA",2131000)

print(t.name)
print("                                     ")
print(t.company)
print("                                     ")
print(t.engines)
print("                                     ")
print(t.height)
print("                                     ")
print("                                     ")
#launching ...
t.launch_rocket()
        