class Display:

    def __init__(self, id, message, is_on):
        self.id = id
        self.message = message or ""
        self.is_on = is_on or False 

    def __str__(self):
        return f"Display {self.id}: {self.message}"

    def __repr__(self):
        return self.__str__()

    # def display(self):
    #     pass

    def update(self, data):
        for value in data.values():
            self.message = value