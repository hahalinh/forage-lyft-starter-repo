import unittest
from datetime import datetime

import os, sys
import sys 
path = os.path.abspath('.')
sys.path.insert(1, path)

from car_factory import CarFactory

'''
5 class for 5 car models
Each class test 4 cases:
    engine should be serviced
    engine should not be serviced
    battery should be serviced
    battery should not be serviced
'''
class TestCalliope(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 40000
        last_service_mileage = 0 
        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 20000
        last_service_mileage = 0 
        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())
    
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 4)
        current_mileage = 20000
        last_service_mileage = 0 
        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 20000
        last_service_mileage = 0 
        car = CarFactory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

class Glissade(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 60000
        last_service_mileage = 0 
        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 20000
        last_service_mileage = 0 
        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())
    
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0 
        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0 
        car = CarFactory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

class Palindrome(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        car = CarFactory.create_palindrome(current_date, last_service_date, True)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        car = CarFactory.create_palindrome(current_date, last_service_date, False)
        self.assertFalse(car.needs_service())
    
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 4)
        car = CarFactory.create_palindrome(current_date, last_service_date, False)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        car = CarFactory.create_palindrome(current_date, last_service_date, False)
        self.assertFalse(car.needs_service())

class Rorschach(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 60000
        last_service_mileage = 0 
        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 40000
        last_service_mileage = 0 
        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())
    
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0 
        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0 
        car = CarFactory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

class Thovex(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 30000
        last_service_mileage = 0 
        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 20000
        last_service_mileage = 0 
        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())
    
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0 
        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year = current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0 
        car = CarFactory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

if __name__ == '__main__':
    unittest.main()
