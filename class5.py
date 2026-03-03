class Smartphone :
    # function/method which is used to be called when an object is created.
    
    def __init__(self,brand,model,price,storage,color,battery): # Where initial value is set up.
        self.brand = brand
        self.model = model
        self.color = color
        self.battery = battery
        self.price = price
        self.storage = storage
        
        print (f"{self.brand} {self.model}  has been created.")
        
    def take_photo(self):
        if self.battery >= 5 :
            print("Taking a photo ...")
            self.battery =  self.battery - 1
            print(f"your battery after taking this photo : {self.battery}")
        else :
            print(f"Sorry your battery is low... Battery : {self.battery}")
            
    def download_something(self, size):
        if size>self.storage :
            print("Download Failed ...")
            print(f"Available Space:{self.storage}GB only.")
        else:
            print("You can download it easily!")
            print("DOWNLOADED!")
            print(f"Available storage now :{self.storage}")
            
            
# Now creating the actual/main object :-

samsung = Smartphone("Samsung","S25 Ultra",200000,512,"Matte Grey",5000)

samsung.take_photo()
samsung.take_photo()

for i in range(5000):
    samsung.take_photo()
    
