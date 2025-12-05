from display import Display
from sensor import Sensor

class CarPark:
    def __init__(self, location, capacity, sensors = None, plates = None, displays = None):
        self.location = location or "Unknown"
        self.capacity = capacity or 0
        self.plates = plates 
        self.displays = displays or []
        self.sensors = sensors or []

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."

    def __repr__(self):
            return self.__str__()

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    
    def add_car(self, plate):
        self.plates.append(plate)
        self.update_display()
    
    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_display()

    @property
    def available_bays(self):
        return 0 if len(self.plates)>=self.capacity else self.capacity - len(self.plates)

    def update_display(self):
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays: display.update(data)

        

if __name__ == "__main__":

    cp = CarPark()

    cp.carIn()