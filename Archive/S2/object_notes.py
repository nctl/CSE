import random


class Random:
    @staticmethod
    def special_random():
        return random.randint(1, 100)


class Laptop(object):
    def __init__(self, screen_resolution, storage_available=1000, color="Cobalt"):
        # Everything in this list should be relevant
        self.processor = "Intel i5"
        self.screen_resolution = screen_resolution
        self.battery_remaining = 100
        self.storage_available = storage_available  # Measured in GB
        self.color = color
        self.os = "Windows 10"
        self.functioning = True

    def charge(self, time):
        if self.functioning:
            self.battery_remaining += time  # This restores the battery over time.

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

        else:
            print("Your computer is DEAD. At least you tried.")

    def smash(self):
        self.functioning = False
    print("I took the laptop...")
    print("AND THREW IT ON THE GROUND!!!")

    def use(self, time):
        self.battery_remaining -= time

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #


my_computer = Laptop("1920x1080", 10000, "Black")
your_computer = Laptop("240p", 16, "Orange")
default_computer = Laptop("1920x1080")


my_computer.use(60)
my_computer.charge(20)
my_computer.charge(100)
my_computer.smash()
my_computer.charge(20)
default_computer.charge(20)
