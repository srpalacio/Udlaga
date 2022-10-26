from Ship import Ship

class bullet:
    
    def __init__(self):
        self.ship=Ship()
        self.condition="Stop"
        self.ybullet=self.ship.y
        
    def shoot (self):
        if self.condition == "Disparo":
            self.ybullet -= 5
        elif self.ship.direction == "Stop":
            pass
    
        
        
        
            
            
        
        
        
        
    