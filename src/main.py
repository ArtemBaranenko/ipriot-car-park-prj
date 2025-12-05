from car_park import CarPark
from sensor import Sensor
from display import Display

carPark = CarPark("Location", 1)

sensor = Sensor(1, True)

sensor.enter()
sensor.exit()

display = Display(1, "Display", True)

display.showAmbientTemperature()
display.showWeather()
display.showArbitraryAnnouncements()

# добавь уточняющий вопросс при попытке закрыть программу, в момент если действие подтвержденно, перепиши все номера в файл