from battery.calculate_duration import calculate_duration
from .battery import Battery

class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self):
        return calculate_duration(self.current_date, self.last_service_date, 3)
