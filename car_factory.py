from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine

from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery

from car import Car

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import Octoprime_Tire

class CarFactory():
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        # Capulet Engine, Spindler Battery
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire([0,0,0,0,0,0])
        car = Car(engine, battery, tire)
        return car
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        # Willoughby Engine, Spindler Battery
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = CarriganTire([0,0,0,0,0,0])
        car = Car(engine, battery, tire)
        return car
    
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        # Willoughby Engine, Nubbin Battery
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = Octoprime_Tire([0,1,0,1,0,0])
        car = Car(engine, battery, tire)
        return car

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        # Capulet Engine, Nubbin Battery
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)
        tire = Octoprime_Tire([0,1,0,1,0,0])
        car = Car(engine, battery, tire)
        return car
    
    def create_palindrome(current_date, last_service_date, warning_light_on):
        # Sternman Engine, Spindler Battery
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)
        tire = Octoprime_Tire([0,0,0,0,0,0])
        car = Car(engine, battery, tire)
        return car