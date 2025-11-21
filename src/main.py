from car_park import CarPark
from sensor import Sensor
from display import Display

carPark = CarPark()

sensor = Sensor()

sensor.enter()
sensor.exit()

display = Display()

display.showAmbientTemperature()
display.showWeather()
display.showArbitraryAnnouncements()

