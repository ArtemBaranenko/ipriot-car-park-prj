import json
from pathlib import Path
from datetime import datetime

from display import Display
from sensor import Sensor


class CarPark:
    """Represents a car park with sensors, displays and logging."""

    def __init__(self, location, capacity, sensors=None, plates=None, displays=None,
                 log_file=Path("log.txt"), config_file=Path("config.json")):
        """Initialise a car park with location, capacity and optional components."""
        # Basic setup for the car park
        self.location = location or "Unknown"
        self.capacity = capacity or 0

        # Lists for storing cars, displays and sensors
        self.plates = plates or []
        self.displays = displays or []
        self.sensors = sensors or []

        # Prepare log file (create it if it doesn’t exist)
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)

        # File where config will be saved
        self.config_file = config_file if isinstance(config_file, Path) else Path(config_file)

    def __str__(self):
        """Return a readable description of the car park."""
        return f"Car park at {self.location}, with {self.capacity} bays."

    def __repr__(self):
        return self.__str__()

    def _log_car_activity(self, plate, action):
        """Write a log entry for a car entering or exiting."""
        # Add a line to the log file with time and action
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")

    def register(self, component):
        """Register a sensor or display with the car park."""
        # Make sure the object is a sensor or display
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        # Add to correct list
        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def write_config(self):
        """Save car park configuration to a JSON file."""
        # Store basic settings in a JSON file
        with self.config_file.open("w") as f:
            json.dump({
                "location": self.location,
                "capacity": self.capacity,
                "log_file": str(self.log_file)
            }, f)

    @classmethod
    def from_config(cls, config_file=Path("config.json")):
        """Load car park configuration from a JSON file and return a new CarPark."""
        # Load config values and build a new CarPark object
        config_file = config_file if isinstance(config_file, Path) else Path(config_file)
        with config_file.open() as f:
            config = json.load(f)
        return cls(config["location"], config["capacity"], log_file=config["log_file"])

    def add_car(self, plate):
        """Add a car to the car park."""
        # Add plate to list and update displays
        self.plates.append(plate)
        self.update_display()
        # Log the entry
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        """Remove a car from the car park."""
        # Remove plate from list and update displays
        self.plates.remove(plate)
        self.update_display()
        # Log the exit
        self._log_car_activity(plate, "exited")

    @property
    def available_bays(self):
        """Return the number of free bays."""
        # If full → return 0, otherwise capacity minus cars
        return 0 if len(self.plates) >= self.capacity else self.capacity - len(self.plates)

    def update_display(self):
        """Update all connected displays with current information."""
        # Build simple data dictionary for the display
        data = {"available_bays": self.available_bays, "temperature": 25}
        
        # Send update to every display
        for display in self.displays:
            display.update(data)


if __name__ == "__main__":
    # Quick test run (placeholder)
    cp = CarPark(location="Test", capacity=50)