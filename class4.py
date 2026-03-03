class GameCharacter :
    health = 100
    score = 0 
    
    def take_damage(self, damage_value):
        self.health = self.health - damage_value
        print(f"Ouch! Health: {self.health}")
        if self.health < 1 :
            print("Dead")
        
    def hit(self):
        self.score = self.score + 5
        print(f"Current Score:{self.score}")
        
    def show_status(self):
        print(f"Current Health: {self.health} & Current Score: {self.score}")
        
        
        
player = GameCharacter()

player.take_damage(100)
        
        