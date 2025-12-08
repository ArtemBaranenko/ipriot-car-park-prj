class Display:
    """Display inside the car park."""

    def __init__(self, id, message, is_on):
        """Initialise a display with an ID, message, and power state."""
        # Basic display setup
        self.id = id
        self.message = message or ""
        self.is_on = is_on or False

    def __str__(self):
        """Return a readable description of the display."""
        return f"Display {self.id}: {self.message}"

    def __repr__(self):
        return self.__str__()

    def update(self, data):
        """Update the display with the provided dictionary of key–value pairs."""
        if "message" in data:
            self.message = data["message"]
        # Print each updated value to simulate a real display
        for key, value in data.items():
            print(f"{key}: {value}")

        # Clear data after showing (placeholder behaviour)
        data = []