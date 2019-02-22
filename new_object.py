import random


class Train (object):
    def __init__(self, train_color="Black and Green", location="Train Station"):
        self.top_speed = 48  # MPH
        self.length = 90  # in meters
        self.current_passengers = 54
        self.color = train_color
        self.location = location
        self.moving = True

    def stop(self):
        if self.moving:
            self.moving = False
            self.current_passengers = 0
            print("The train has stopped at the passengers' destination.")

    def depart(self):
        self.current_passengers = random.randint(1, 100)
        self.location = input("Where do you want to go?")
        print("The train is now going to %s at 48 MPH" % self.location)
        self.moving = True

