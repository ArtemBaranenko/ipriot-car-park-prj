import json

from pathlib import Path
from datetime import datetime

from display import Display
from sensor import Sensor

class CarPark:
    def __init__(self, location, capacity, sensors = None, plates = None, displays = None, log_file=Path("log.txt"), config_file=Path("config.json")):
        self.location = location or "Unknown"
        self.capacity = capacity or 0
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []
        
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)

        self.config_file = config_file if isinstance(config_file, Path) else Path(config_file)

    def __str__(self):
        return f"Car park at {self.location}, with {self.capacity} bays."

    def __repr__(self):
            return self.__str__()
    
    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")
        
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def write_config(self):
        with self.config_file.open("w") as f: 
            json.dump({"location": self.location,
                        "capacity": self.capacity,
                        "log_file": str(self.log_file)}, f)
            
    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])

    def add_car(self, plate):
        self.plates.append(plate)
        self.update_display()
        self._log_car_activity(plate, "entered")
    
    def remove_car(self, plate):
        self.plates.remove(plate)
        self.update_display()
        self._log_car_activity(plate, "exited")

    @property
    def available_bays(self):
        return 0 if len(self.plates)>=self.capacity else self.capacity - len(self.plates)

    def update_display(self):
        data = {"available_bays": self.available_bays, "temperature": 25}
        for display in self.displays: display.update(data)


if __name__ == "__main__":

    cp = CarPark()

    cp.carIn()
