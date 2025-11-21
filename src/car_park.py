from display import Display

class CarPark:
    def __init__(self):
        self.display = Display()

    def scanPlates(self):
        pass

    def carIn(self):
        self.scanPlates()
        self.display.showAvailability()

    def carOut(self):
        self.scanPlates()
        self.display.showAvailability()

if __name__ == "__main__":

    cp = CarPark()

    cp.carIn()