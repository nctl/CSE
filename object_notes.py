class Laptop(object):
    def __init__(self, screen_resolution, storage_available):
        # Everything in this list should be relevant
        self.processor = "Intel i5"
        self.screen_resolution = screen_resolution
        self.battery_remaining = 100
        self.storage_available = storage_available
        self.color = "Black and Silver"
        self.os = "Windows 10"

    def charge(self, time):
        self.battery_remaining += time

        if self.battery_remaining >= 100:
            self.battery_remaining = 100

        # Full charge
        if self.battery_remaining == 100:
            print("Your PC is fully charged.")
            return

        # Low charge
        if self.battery_remaining < 100:
            print("%d power left" % self.battery_remaining)  # needs changing

        # No charge
        else:
            print("%d power left" % self.battery_remaining)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

