from .tire import Tire

class CarriganTire(Tire):
    def __init__(self,  tires):
        self.tires = tires
        
    def needs_service(self):
        for t in self.tires:
            if t >= 0.9:
                return True
        
        return False