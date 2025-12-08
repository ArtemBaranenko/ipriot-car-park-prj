from abc import ABC, abstractmethod
import random

class Sensor:
    """Base class for sensors inside the car park."""

    def __init__(self, id, is_active, car_park):
        """Initialise a sensor with an ID, active state, and linked car park."""
        # Store basic sensor info
        self.id = id
        self.is_active = is_active or False
        self.car_park = car_park

    def __str__(self):
        """Return a readable description of the sensor."""
        return f"Sensor {self.id} is {'Active' if self.is_active else 'Not active'}"

    def __repr__(self):
        return self.__str__()

    @abstractmethod
    def update_car_park(self, plate):
        """Update the car park based on the detected vehicle."""
        pass

    def _scan_plate(self):
        """Generate a fake licence plate."""
        # Create a random fake plate for testing
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        """Scan a plate and update the car park accordingly."""
        # Detect a vehicle and send info to the car park
        plate = self._scan_plate()
        self.update_car_park(plate)


class EntrySensor(Sensor):
    """Sensor detecting vehicles entering the car park."""

    def update_car_park(self, plate):
        """Add the vehicle to the car park and print a message."""
        # Car is entering the car park
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}")


class ExitSensor(Sensor):
    """Sensor detecting vehicles leaving the car park."""

    def update_car_park(self, plate):
        """Remove the vehicle from the car park and print a message."""
        # Car is exiting the car park
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")

    def _scan_plate(self):
        """Select a random existing plate from the car park."""
        # Choose a random plate from currently parked cars
        return random.choice(self.car_park.plates)