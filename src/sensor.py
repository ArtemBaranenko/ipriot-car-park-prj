from car_park import CarPark

class Sensor:
    def __init__(self):
        self.car_park = CarPark()

    def enter(self):
        self.car_park.carIn()

    def exit(self):
        self.car_park.carOut()

