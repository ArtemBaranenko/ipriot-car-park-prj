import unittest
from src.sensor import Sensor
from src.car_park import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.sensor = Sensor(1, True, self.car_park)

    def test_sensor_initialized_with_all_attributes(self):
        self.assertIsInstance(self.sensor, Sensor)
        self.assertEqual(self.sensor.id, 1)
        self.assertEqual(self.sensor.is_active, True)
        self.assertIsInstance(self.car_park, CarPark)
