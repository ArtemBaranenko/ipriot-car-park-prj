import unittest
from src.sensor import Sensor
from src.sensor import EntrySensor
from src.car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.sensor = Sensor(1, True, self.car_park)
        self.sensor = EntrySensor(1, True, self.car_park)

    def test_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.sensor, Sensor)
        self.assertEqual(self.sensor.id, 1)
        self.assertEqual(self.sensor.is_active, True)
        self.assertIsInstance(self.car_park, CarPark)

    def test_detect_vehicle_adds_car(self):
        self.assertEqual(len(self.car_park.plates), 0)  # ensure empty

        self.sensor.detect_vehicle()

        self.assertEqual(len(self.car_park.plates), 1)  # car added
        self.assertTrue(self.car_park.plates[0].startswith("FAKE-"))
