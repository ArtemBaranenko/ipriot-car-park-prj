class Sensor:

    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active or False
        self.car_park = car_park

    def __str__(self):
        return f"Sensor {self.id} is {'Active' if self.is_active else 'Not active'}"

    def __repr__(self):
        return self.__str__()
    
    def detect_vehicle(self):
        pass

    def scan_plate(self):
        pass
    

    class EntrySensor(Sensor):
        pass
        
    class ExitSensor(Sensor):
        pass


