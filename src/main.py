from car_park import CarPark
from sensor import Sensor
from display import Display

car_park = CarPark("123 Example Street", 100)
display = Display(1, "Welcome to the car park", True)

display.update({"message": "Goodbye"})

print (display.message)


# добавь уточняющий вопросс при попытке закрыть программу, в момент если действие подтвержденно, перепиши все номера в файл