from .engine import Engine

class CapuletEngine(Engine):
    def __init__(self,  last_service, current_milage):
        self.last_service = last_service
        self.current_milage = current_milage
        
    def needs_service(self):
        return self.current_milage - self.last_service >= 30000